# Escape from CMU -- escape mode
import cv2
import numpy as np
from cmu_112_graphics import *
import math
import random

#################################################
# __init__
#################################################
def init(app):
    #--------------------Images----------------------
    app.mapScaleFactor = 1/3
    app.pixelsPerDisplayElement = 1 / app.mapScaleFactor

    # map source: Hannah Chen (AndrewID: ziqic2) -- Thank you so much Hannah ❤️
    app.map_img = app.loadImage("img/map.jpg")
    app.map_img = app.scaleImage(app.map_img, app.mapScaleFactor)
    app.numpy_map_img = cv2.imread(("img/map.jpg"))
    app.walkableBGR = [113, 107, 94]

    # image source: https://opengameart.org/content/platform-pack
    app.escape_player_img1 = app.loadImage("img/Platform pack/PNG/Characters/LightBlue_Front1.png")
    app.escape_player_img1 = app.scaleImage(app.escape_player_img1, 1/5)
    app.escape_player_img2 = app.loadImage("img/Platform pack/PNG/Characters/LightBlue_Front2.png")
    app.escape_player_img2 = app.scaleImage(app.escape_player_img2, 1/5)
    app.escape_player_img3 = app.loadImage("img/Platform pack/PNG/Characters/LightBlue_Front3.png")
    app.escape_player_img3 = app.scaleImage(app.escape_player_img3, 1/5)
    app.escape_player_img_sprites = [app.escape_player_img1] + [app.escape_player_img2] + [app.escape_player_img3]
    app.escape_player_img_spritesCounter = 0

    # image source: https://svg-clipart.com/black/NPjwC5U-men-in-black-clipart
    app.menInBlack_img = app.loadImage("img/menInBlack_img.png")
    app.menInBlack_img = app.scaleImage(app.menInBlack_img, 1/14)

    # image source: https://opengameart.org/content/platform-pack
    app.TA_img1 = app.loadImage("img/Platform pack/PNG/Characters/Red_Front1.png")
    app.TA_img1 = app.scaleImage(app.TA_img1, 1/5)
    app.TA_img2 = app.loadImage("img/Platform pack/PNG/Characters/Red_Front2.png")
    app.TA_img2 = app.scaleImage(app.TA_img2, 1/5)
    app.TA_img3 = app.loadImage("img/Platform pack/PNG/Characters/Red_Front3.png")
    app.TA_img3 = app.scaleImage(app.TA_img3, 1/5)
    app.TA_img_sprites = [app.TA_img1] + [app.TA_img2] + [app.TA_img3]
    app.TA_img_spritesCounter = 0

    #--------------------Map-------------------------
    # parameters of map
    # shape returns (height, width, mode)
    pixelHeight, pixelWidth = app.numpy_map_img.shape[:2] 

    app.boardRows = 20
    app.boardCols = 20
    app.pixelsPerRow = int(app.height * app.pixelsPerDisplayElement / app.boardRows)
    app.pixelsPerCol = int(app.width * app.pixelsPerDisplayElement / app.boardCols)
    app.fullBoardRows = int(pixelHeight / app.pixelsPerRow)
    app.fullBoardCols = int(pixelWidth / app.pixelsPerCol)

    app.scrollMargin = 5

    #----------------Create Instance----------------
    # introduce player into escape mode
    app.escapePlayer = escapeModePlayer(app)

    # introduce instance map
    app.campusMap = Map(app)
    app.campusMap.initializeDisplayRange(app)
    app.campusMap.checkWalkablePosition(app)

    #----------------Men In Black-------------------
    app.blackMen = MenInBlack(app)

    #-------------------Enemy-----------------------
    app.enemyPresented = False

    app.enemyTA1 = Enemy(app, (24, 39), 9)
    app.enemyTA2 = Enemy(app, (16, 24), 5)
    app.enemyTA3 = Enemy(app, (27, 7), 6)
    app.nodeSet = app.campusMap.getNodeSet(app)
    app.chasingTimerCount = 0

    #----------------Back To Campus-----------------
    app.carryHat = False

    #---------------Instructions--------------------
    app.instructionButton_img = app.loadImage("img/instuction_img.png")
    app.instructionButton_img = app.scaleImage(app.instructionButton_img, 1/6)

    print("Successfully imported escapeMode.")
 
#################################################
# Map Class
#################################################
class Map(object):
    def __init__(self, app):
        # initialize map display range using pixels
        self.displayStartLocation = [0, 0]

        # initialize board 
        # purpose of board: marking player location and whether a place is walkable
        self.mapBoard = make2dList(app.fullBoardRows, app.fullBoardCols, False)
        self.displayBoard = make2dList(app.boardRows, app.boardCols, [])

    # loop throught every pixel -- check whether the cell is walkable
    # not perfect check but filter out most of the non-path part
    def checkWalkablePosition(self, app):
        for row in range(app.fullBoardRows):
            for col in range(app.fullBoardCols):
                # color how many randomly picked point has road color
                colorCount = 0

                pixelStart_y, pixelStart_x = row * app.pixelsPerRow, col * app.pixelsPerCol
                pixelEnd_y, pixelEnd_x = pixelStart_y + app.pixelsPerRow, pixelStart_x + app.pixelsPerCol
                # iterate through each pixel in the range
                # check whether it contains walkable color
                for pixel_x in range(pixelStart_x,pixelEnd_x, 10):
                    for pixel_y in range(pixelStart_y, pixelEnd_y, 10):
                        # use np.any to compare two arrays 
                        if np.array_equal(app.numpy_map_img[pixel_y][pixel_x], 
                                                            app.walkableBGR):
                            colorCount += 1
                            # if find eight points with road color
                            if colorCount >= 8:
                                self.mapBoard[row][col - 1] = True
                                break

        # manually adjusr some weird cell due to color pick
        for _ in range(18, 24):
            self.mapBoard[17][_] = False
        
        self.mapBoard[15][17] = False
        self.mapBoard[16][17] = False
        self.mapBoard[28][12] = False
        self.mapBoard[33][7] = False
        self.mapBoard[29][23] = False
        self.mapBoard[36][28] = False
        self.mapBoard[17][28] = False
        self.mapBoard[21][28] = False
        self.mapBoard[19][26] = False
        self.mapBoard[19][30] = False
        self.mapBoard[17][27] = False
        self.mapBoard[17][29] = False
        self.mapBoard[14][18] = True
        self.mapBoard[5][30] = False
        self.mapBoard[9][29] = False
        self.mapBoard[8][28] = False
        self.mapBoard[10][30] = False

        for _ in range(33, 42):
            if _ == 33 or _ == 35 or _ == 36 or _ == 37 or _ == 40 or _ == 41:
                self.mapBoard[_][23] = False
        
        for _ in range(25, 31):
            self.mapBoard[25][_] = False
        
        for _ in range(33, 48):
            self.mapBoard[25][_] = False

        for _ in range(33, 53):
            self.mapBoard[17][_] = False
        
        for _ in range(8, 25):
            self.mapBoard[26][_] = True

        for _ in range(26, 31):
            self.mapBoard[12][_] = False
    
    def getNodeSet(self, app):
        result = set()
        for row in range(app.fullBoardRows):
            for col in range(app.fullBoardCols):
                if self.mapBoard[row][col]:
                    result.add((row, col))
        return result
    
    def initializeDisplayRange(self, app):
        self.displayStartLocation = [app.escapePlayer.playerLocationInMap[0] 
                                - app.width * app.pixelsPerDisplayElement / 2,
                                    app.escapePlayer.playerLocationInMap[1] 
                                - app.height * app.pixelsPerDisplayElement / 2]
          
    #-------------------Method-----------------------
    # given player's current location -- return player's relative row and col in board
    def getPlayerLocationInBoard(self, player, app):
        col = int((player.playerLocationInMap[0] - self.displayStartLocation[0]) / app.pixelsPerCol)
        row = int((player.playerLocationInMap[1] - self.displayStartLocation[1]) / app.pixelsPerRow)
        return (row, col)
    
    # given player's current location -- return player's absolute row and col in full board
    def getPlayerLocationInFullBoard(self, app, playerLocation_x, playerLocation_y):
        col = int(playerLocation_x / app.pixelsPerCol)
        row = int(playerLocation_y / app.pixelsPerRow)
        return (row, col)

    #-------------------View-------------------------
    def drawMap(self, app, canvas):
        # find the nw corner coordinates (x,y) of the map
        x = - self.displayStartLocation[0] / app.pixelsPerDisplayElement
        y = - self.displayStartLocation[1] / app.pixelsPerDisplayElement
        canvas.create_image(x, y, 
                        anchor = "nw", image=ImageTk.PhotoImage(app.map_img))

    # drawGrid -- helpful features
    # modified from Tetris HW
    def drawGrid(self, app, canvas):
        for row in range(app.boardRows):
            for col in range(app.boardCols):
                self.drawCell(app, canvas, row, col)       

    # helper function for drawGrid() -- modified fro Tetris hw
    def drawCell(self, app, canvas, row, col):
        def getCellBounds(app, row, col):
            # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
            x0 = app.width / app.boardRows * col
            x1 = x0 + app.width / app.boardRows
            y0 = app.height / app.boardCols * row
            y1 = y0 + app.height / app.boardCols
            return (x0, y0, x1, y1)
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_rectangle(x0, y0, x1, y1,
                                    outline = "grey", width = 2)
    
    # to manually adjust the walkable attribute board
    # -- since hand painting is not accurate 
    # -- and checkWalkablePosition doesn't check every pixel (to save time)
    def markWalkable(self, app, canvas):
        canvasStartRow = int(self.displayStartLocation[1] / app.pixelsPerRow)
        canvasStartCol = int(self.displayStartLocation[0] / app.pixelsPerCol)

        cellWidth = app.width / app.boardRows
        cellHeight = app.width / app.boardCols
        
        for row in range(app.fullBoardRows):
            for col in range(app.fullBoardCols):
                if self.mapBoard[row][col]:
                    rowInCanvas, colInCanvas = row - canvasStartRow, col - canvasStartCol
                    y0, x0 = rowInCanvas * cellWidth, colInCanvas * cellHeight
                    y1, x1 = y0 + cellHeight, x0 + cellWidth
                    canvas.create_oval(x0, y0, x1, y1, outline = "red",
                                                                    width = 3)
                    
#################################################
# Player Class
#################################################
class escapeModePlayer(object):
    def __init__(self, app):
        # initialize player location -- area near soccer field
        self.playerLocationInMap = [4180, 1223]
        self.playerLocationInBoard = [app.boardRows // 2, app.boardCols//2]
    
    #-------------------Method-----------------------
    def getPlayerLocationInCanvas(self, map, app):
        return map.getPlayerLocationInBoard(self, app)
    
    def getPlayerLocationInFullBoard(self, map, app, playerLocation_x, playerLocation_y):
        return map.getPlayerLocationInFullBoard(app, playerLocation_x, playerLocation_y)
    
    # based on row and col -- return player's center in board
    def getPlayerCenter(self, app, row, col):
        cellWidth = app.width / app.boardRows
        cellHeight = app.width / app.boardCols
        cx = (col + 1/2) * cellWidth
        cy = (row + 1/2) * cellHeight
        return (cx, cy)

    # move player based on key pressed
    def movePlayer(self, app, drow, dcol):
        nextPositionInMap_x = self.playerLocationInMap[0] + dcol * app.pixelsPerRow
        nextPositionInMap_y = self.playerLocationInMap[1] + drow * app.pixelsPerCol

        # update player's location when the move is legal
        if self.isLegalMove(app, nextPositionInMap_x, nextPositionInMap_y):
            # update player's absolute position
            self.playerLocationInMap[0] += dcol * app.pixelsPerRow
            self.playerLocationInMap[1] += drow * app.pixelsPerCol
            # update player's relative position
            self.playerLocationInBoard[0] += drow
            self.playerLocationInBoard[1] += dcol
        
        self.updateDisplayRange(app)

    # update display range after each move
    def updateDisplayRange(self, app):
        playerRow, playerCol = self.getPlayerLocationInCanvas(app.campusMap, app)
        
        if app.scrollMargin > playerCol:
            app.campusMap.displayStartLocation[0] -= app.pixelsPerCol
            # redo the change when out of range
            if app.campusMap.displayStartLocation[0] < 0:
                app.campusMap.displayStartLocation[0] += app.pixelsPerCol

        elif app.scrollMargin > playerRow:
            app.campusMap.displayStartLocation[1] -= app.pixelsPerRow
            # redo the change when out of range
            if app.campusMap.displayStartLocation[1] < 0:
                app.campusMap.displayStartLocation[1] += app.pixelsPerRow

        elif playerCol >= app.boardCols - app.scrollMargin:
            app.campusMap.displayStartLocation[0] += app.pixelsPerCol
            # redo the change when out of range
            if app.campusMap.displayStartLocation[0] > (- app.width 
                                        + app.fullBoardCols * app.pixelsPerCol):
                app.campusMap.displayStartLocation[0] -= app.pixelsPerCol

        elif playerRow >= app.boardRows - app.scrollMargin:
            app.campusMap.displayStartLocation[1] += app.pixelsPerRow
            # redo the change when out of range
            if app.campusMap.displayStartLocation[1] > (- app.height
                                        + app.fullBoardRows * app.pixelsPerRow):
                app.campusMap.displayStartLocation[1] -= app.pixelsPerRow

    # check whether the move is legal using the full board
    # return True when the cell containing pixelPosition is walkable
    def isLegalMove(self, app, playerLocation_x, playerLocation_y):
        fullBoardRow, fullBoardCol = self.getPlayerLocationInFullBoard(app.campusMap, 
                                            app, playerLocation_x, playerLocation_y)
        #print("playerLocation", fullBoardRow, fullBoardCol)
        return app.campusMap.mapBoard[fullBoardRow][fullBoardCol]

    #-------------------View-------------------------
    def drawPlayer(self, app, canvas):
        row, col = self.getPlayerLocationInCanvas(app.campusMap, app)
        cx, cy = self.getPlayerCenter(app, row, col)
        canvas.create_image(cx, cy, anchor = "center", 
                                    image=ImageTk.PhotoImage(app.escape_player_img_sprites[app.escape_player_img_spritesCounter]))

#################################################
# Enemy Class
#################################################
class Enemy(escapeModePlayer):
    def __init__(self, app, initLocation, detectRange):
        self.location = initLocation
        self.detectRange = detectRange

    #-------------------Method-----------------------
    # get enemy center based on enery location in full map
    def getCenter(self, map, app, row, col):
        canvasStartRow = int(map.displayStartLocation[1] / app.pixelsPerRow)
        canvasStartCol = int(map.displayStartLocation[0] / app.pixelsPerCol)
        
        rowInCanvas, colInCanvas = row - canvasStartRow, col - canvasStartCol

        cellWidth = app.width / app.boardRows
        cellHeight = app.width / app.boardCols
        cx = (colInCanvas + 1/2) * cellWidth
        cy = (rowInCanvas + 1/2) * cellHeight

        return (cx, cy)

    # when player in detect range -- chase player
    def chasePlayer(self, app, player):
        path, targetNode = self.findPath(app, player)
        if len(path) >= 2:
            self.location = path[1]
        elif len(path) == 1:
            self.location = targetNode

    # Using Dijkstra's Algorithm to find the shortest path
    # Algorithm learned from TA mini lecture
    def findPath(self, app, player):
        # start node: self.location
        # end node: player location
        startNode = self.location
        targetNode = app.escapePlayer.getPlayerLocationInFullBoard(app.campusMap, app, 
                                            app.escapePlayer.playerLocationInMap[0],
                                            app.escapePlayer.playerLocationInMap[1])
        
        unvisitedNodeSet = copy.copy(app.nodeSet)
        distanceDict = dict()
        prevsDict = dict()

        # initialize the distanceDict
        for node in unvisitedNodeSet:
            if node != startNode:
                distanceDict[node] = float('inf')
            else:
                distanceDict[node] = 0

        # initialize the prevsDict
        for node in unvisitedNodeSet:
            prevsDict[node] = None

        # repeat until the current node is target node
        currNode = startNode

        while currNode != targetNode:
            minDistance = float('inf')
            nodeWithMinDistance = (-1, -1)
            # pick the unvisited node with min distance
            for node in unvisitedNodeSet:
                if distanceDict[node] < minDistance:
                    minDistance = distanceDict[node]
                    nodeWithMinDistance = node
            currNode = nodeWithMinDistance

            # remove currNode from unvisited node set
            unvisitedNodeSet.remove(currNode)

            # iterate through the neighbors -- update when getting greater distance
            # vertical/horizontal move -- distance 10
            for neighborDirection in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
                neighborNode = (currNode[0] + neighborDirection[0], currNode[1] + neighborDirection[1])
                if neighborNode in unvisitedNodeSet:
                    neighborDistance = distanceDict[neighborNode]
                    if neighborDistance > distanceDict[currNode] + 10:
                        distanceDict[neighborNode] = distanceDict[currNode] + 10
                        prevsDict[neighborNode] = currNode
            
            # diagonal move -- distance 14
            for neighborDirection in [(-1, +1), (+1, -1), (-1, -1), (+1, +1)]:
                neighborNode = (currNode[0] + neighborDirection[0], currNode[1] + neighborDirection[1])
                if neighborNode in unvisitedNodeSet:
                    neighborDistance = distanceDict[neighborNode]
                    if neighborDistance > distanceDict[currNode] + 14:
                        distanceDict[neighborNode] = distanceDict[currNode] + 14
                        prevsDict[neighborNode] = currNode

        # reconstruct the path
        path = []
        currNode = targetNode
        while currNode != startNode:
            nextNode = prevsDict[currNode]
            path.insert(0, nextNode)
            currNode = nextNode

        return path, targetNode

    # return True when player is in detect range
    def inDetectRange(self, app, player, enemy):
        enemyNode = enemy.location
        playerNode = player.getPlayerLocationInFullBoard(app.campusMap, app, 
                                            app.escapePlayer.playerLocationInMap[0],
                                            app.escapePlayer.playerLocationInMap[1])
        
        def getDistance(playerNode, enemyNode):
            distance = math.sqrt((playerNode[0] - enemyNode[0])**2 + 
                                                (playerNode[1] - enemyNode[1])**2)
            return distance
        
        return getDistance(playerNode, enemyNode) <= self.detectRange

    # enemy just walk around the campus when not in the detect range
    def walkAround(self, app):
        currNode = self.location
        walkableNeighbors = []
        for neighborDirection in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:
            neighborNode = (currNode[0] + neighborDirection[0], currNode[1] + neighborDirection[1])

            if neighborNode in app.nodeSet:
                walkableNeighbors.append(neighborNode)
        
        self.location = random.choice(walkableNeighbors)

    # return True if enemy caught player
    def catchPlayer(self, app, player):
        enemyNode = self.location
        playerNode = player.getPlayerLocationInFullBoard(app.campusMap, app, 
                                            app.escapePlayer.playerLocationInMap[0],
                                            app.escapePlayer.playerLocationInMap[1])
        
        return enemyNode == playerNode
    
    #-------------------View-------------------------
    def drawEnemy(self, app, canvas):
        row, col = self.location
        cx, cy = self.getCenter(app.campusMap, app, row, col)
        canvas.create_image(cx, cy, anchor = "center", 
            image=ImageTk.PhotoImage(app.TA_img_sprites[app.TA_img_spritesCounter]))
        self.drawDetectRange(app, canvas, cx, cy)
    
    def drawDetectRange(self, app, canvas, cx, cy):
        cellWidth = app.width / app.boardRows
        radius = self.detectRange * cellWidth
        canvas.create_oval(cx - radius, cy - radius, cx + radius, cy + radius,
                            outline = "red", width = 4)


#################################################
# escapeMode_timerFired
#################################################
def timerFired(app):
    app.TA_img_spritesCounter = (app.TA_img_spritesCounter + 1) % 3
    
    if app.enemyPresented:
        app.chasingTimerCount = (app.chasingTimerCount + 1) % 5
        if (app.enemyTA1.catchPlayer(app, app.escapePlayer) or 
            app.enemyTA2.catchPlayer(app, app.escapePlayer) or
            app.enemyTA3.catchPlayer(app, app.escapePlayer) ):
            app.life -= 1
            init(app)
            app.enemyPresented = True
            app.escapePlayer.playerLocationInMap = [4202, 1213]
            app.campusMap.initializeDisplayRange(app)

#################################################
# MenInBlack Class
#################################################
'''Note: I may add more features to MenInBLACK so I wrote a class'''
class MenInBlack(escapeModePlayer):
    def __init__(self, app):
        self.playerLocationInMap = [1921, 521]
        self.playerLocationInBoard = [app.boardRows // 2, app.boardCols//2]
    
    def drawMen(self, app, canvas):
        row, col = self.getPlayerLocationInCanvas(app.campusMap, app)
        cx, cy = self.getPlayerCenter(app, row, col)
        canvas.create_image(cx, cy, anchor = "center", 
                                image=ImageTk.PhotoImage(app.menInBlack_img))


#################################################
# escapeMode_keyPressed
#################################################
def keyPressed(app,event):
    if (event.key == 'Up'):      
        app.escapePlayer.movePlayer(app, -1, 0)
    elif (event.key == 'Down'):  
        app.escapePlayer.movePlayer(app, +1, 0)
    elif (event.key == 'Left'): 
        app.escapePlayer.movePlayer(app, 0, -1)
    elif (event.key == 'Right'): 
        app.escapePlayer.movePlayer(app, 0, +1)
    
    # when the player meets MenInBlack
    if (app.blackMen.getPlayerLocationInFullBoard(app.campusMap, app, 
        app.blackMen.playerLocationInMap[0], app.blackMen.playerLocationInMap[1])
        == app.escapePlayer.getPlayerLocationInFullBoard(app.campusMap, app, 
            app.escapePlayer.playerLocationInMap[0], app.escapePlayer.playerLocationInMap[1])):
        
        if not app.enemyPresented:
            app.mode = "huntToConnectorMode"
        else:
            app.mode = "winMode"

#################################################
# escapeMode_redrawAll
#################################################
def drawAll(app, canvas):
    app.campusMap.drawMap(app, canvas)
    # app.campusMap.drawGrid(app, canvas)
    # app.campusMap.markWalkable(app, canvas)
    app.escapePlayer.drawPlayer(app, canvas)
    app.blackMen.drawMen(app, canvas)
    drawInstuctionButton(app, canvas)
    if app.enemyPresented:
        app.enemyTA1.drawEnemy(app, canvas)
        app.enemyTA2.drawEnemy(app, canvas)
        app.enemyTA3.drawEnemy(app, canvas)
        if app.chasingTimerCount == 0:
            # for app.enemyTA1
            if app.enemyTA1.inDetectRange(app, app.escapePlayer, app.enemyTA1):
                app.enemyTA1.chasePlayer(app, app.escapePlayer)
            else:
                app.enemyTA1.walkAround(app)
            # for app.enemyTA2
            if app.enemyTA2.inDetectRange(app, app.escapePlayer, app.enemyTA2):
                app.enemyTA2.chasePlayer(app, app.escapePlayer)
            else:
                app.enemyTA2.walkAround(app)
            # for app.enemyTA3
            if app.enemyTA3.inDetectRange(app, app.escapePlayer, app.enemyTA3):
                app.enemyTA3.chasePlayer(app, app.escapePlayer)
            else:
                app.enemyTA3.walkAround(app)

def drawInstuctionButton(app, canvas):
    canvas.create_image(20, app.height - 10, anchor = "nw", 
                                    image=ImageTk.PhotoImage(app.instructionButton_img))

#################################################
# Helper
#################################################
# return a 2d list with "fill" in each cell
# modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def make2dList(rows, cols, fill):
    return [ ([fill] * cols) for row in range(rows)]
