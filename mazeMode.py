# Find Taylor's Hat -- maze mode
from cmu_112_graphics import *
import random

'''
Based on Depth-first Search Algorithm from Wikipedia:
https://en.wikipedia.org/wiki/Maze_generation_algorithm
'''

#################################################
# __init__
#################################################
def init(app):
    #--------------------Maze------------------------
    # parameters of maze
    app.mazeRows = 25
    app.mazeCols = 25
    app.mazeTopMargin = 30
    app.mazeMargin = 10

    # create a maze
    app.maze = Maze(app.mazeRows, app.mazeCols)
    app.maze.generateMaze(app)

    #--------------------Images----------------------
    # bg photo source: https://www.pinterest.com/pin/155444624629706321/
    app.maze_bg_img = app.loadImage("img/bg_img2.jpeg")
    # image source: https://opengameart.org/content/platform-pack
    app.maze_player_img = app.loadImage("img/Platform pack/PNG/Characters/LightBlue_Front1.png")
    app.maze_player_img = app.scaleImage(app.maze_player_img, 1/9)

    # target hat photo
    # created by: Hannah Chen (AndrewID: ziqic2)
    app.maze_hat_img = app.loadImage("img/hat_img.png")
    app.maze_hat_img = app.scaleImage(app.maze_hat_img, 1/16)

    # create a player and target
    app.mazePlayer = PlayerInMaze(app, 0, 0)
    app.mazeHat = MazeHat(app)

    # timer
    app.mazeTimer = 60000 # 60s to finish
    app.timerDelay = 500

    # game state
    app.mazeGameOver = False
    app.hintDisplay = False

    # maze solution
    app.solution = []
    app.maze.solveMaze(app)
    app.displaySolution = False

    print("Successfully imported mazeMode.")

#################################################
# Maze class
#################################################
class Maze(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        
        # create maze board
        self.board = make2dList(rows, cols, [])

        # place cell into each position 
        for row in range(rows):
            for col in range (cols):
                self.board[row][col] = Cell(row, col)

    #---------------Maze Generation------------------
    # generate a maze based on Depth-first search algorithm
    def generateMaze(self, app):
        # start with a random cell
        currRow, currCol = (random.randint(0, app.mazeRows - 1), 
                                            random.randint(0, app.mazeCols- 1))
        currCell = self.board[currRow][currCol]
        currCell.isVisited = True

        # based on randomly-picked currentCell -- generate maze
        self.generateMazeFromCell(currRow, currCol)

    def generateMazeFromCell(self, currRow, currCol):
        neighborsDirection = self.findUnvisitedNeighbors(currRow, currCol)
        # Base case
        if neighborsDirection == None:
            if self.isAllVisited(): 
                return
            else:
                return None
        # Recursive Case
        else:
            # shuffle the neighborsDirection directions and iterate through it
            random.shuffle(neighborsDirection)
            for drow, dcol in neighborsDirection:
                nextRow, nextCol = currRow + drow, currCol + dcol
                
                # recheck the neighbors condition of currCell
                if self.findUnvisitedNeighbors(currRow, currCol) != None:
                    # distructively create path between current cell and next cell
                    currCell = self.board[currRow][currCol]
                    nextCell = self.board[nextRow][nextCol]
                    currCell.connect(nextCell)

                    # mark next cell as visited
                    nextCell.isVisited = True
                    
                    result = self.generateMazeFromCell(nextRow, nextCol)
                    
                    if result != None:
                        # if every cell has all been visited
                        # maze generation -- DONE
                        return
    
    # helper function for generateMaze() -- return a list of unvisted neighbor direction
    def findUnvisitedNeighbors(self, currRow, currCol):
        result = []
        for (drow, dcol) in [(-1,0), (+1, 0), (0, -1), (0, +1)]:
            neighborRow, neighborCol = currRow + drow, currCol + dcol

            # helper function for generateMaze() -- return True when cell is on board 
            def isOnBoard(self, row, col):
                return (0 <= row < self.rows) and (0 <= col < self.cols)
        
            if isOnBoard(self, neighborRow, neighborCol):
                neighborCell = self.board[neighborRow][neighborCol]
                if not neighborCell.isVisited:
                    result.append((drow, dcol))
        
        # return None when neighbor cells have all been visited
        if result == []:
            return None
        else:
            return result

    # helper function for generateMaze() -- return True when all cells have been visted
    def isAllVisited(self):
        for row in range(self.rows):
            for col in range (self.cols):
                if not self.board[row][col].isVisited:
                    return False
        return True
    
    # helper function for player class -- determine whether a move is Legal
    def isLegalMove(self, app, currRow, currCol, newRow, newCol):
        drow, dcol = newRow - currRow, newCol - currCol

        currCell = self.board[currRow][currCol]

        if (drow, dcol) == (-1, 0): # going UP
            return not currCell.wallDict["North"]
        elif (drow, dcol) == (+1, 0): # going DOWN
            return not currCell.wallDict["South"] 
        elif (drow, dcol) == (0, -1): # going LEFT
            return not currCell.wallDict["West"] 
        elif (drow, dcol) == (0, +1): # going Right
            return not currCell.wallDict["East"]

    #---------------Maze Solving---------------------
    # based on the maze solving algorithm in class notes
    # recursion part 2: https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html#mazeSolving
    def solveMaze(self, app):
        targetRow, targetCol = app.mazeRows - 1, app.mazeCols - 1
        
        def solve(app, row, col):
            # Base Case
            if (row,col) in app.solution: 
                return False

            # Recursive case
            else:
                app.solution.append((row, col))
                if (row ,col) == (targetRow ,targetCol): 
                    return True
                
                # iterate through each direction
                for drow, dcol in ((-1, 0), (+1, 0), (0, -1), (0, +1)):
                    if self.isLegalMove(app, row, col, row + drow, col + dcol):
                        if solve(app, row + drow, col + dcol): 
                            return True

                app.solution.pop()
                return False

        solve(app, 0, 0)

    #-------------------View-------------------------
    def drawBoard(self, app, canvas):
        for row in range(self.rows):
            for col in range (self.cols):
                self.board[row][col].drawCell(app, canvas, row, col)

    def drawBackground(self, app, canvas):
        canvas.create_image(app.width/2, 0, 
                        anchor = "n", image=ImageTk.PhotoImage(app.maze_bg_img))
    
    def getCenter(self, app, location):
        cellWidth = (app.width - 2 * app.mazeMargin) / app.mazeCols
        cellHeight = (app.height - app.mazeMargin - app.mazeTopMargin) / app.mazeRows
    
        row, col = location
        x = app.mazeMargin + cellWidth * (col + 1/2)
        y = app.mazeTopMargin + cellHeight * (row + 1/2)
        
        return (x, y)

    def drawSolution(self, app, canvas):
        steps = len(app.solution) - 1
        for step in range(steps):
            currLocation = app.solution[step]
            nextLocation = app.solution[step + 1]

            start_x, start_y = self.getCenter(app, currLocation)
            endRow_x, endCol_y = self.getCenter(app, nextLocation)

            canvas.create_line(start_x, start_y, endRow_x, endCol_y, fill = "red", width = 2)

#################################################
# Cell class
#################################################
class Cell(object):
    def __init__(self, row, col):
        self.row = row
        self.col = col

        # wallDict -- initialize all walls to be true
        self.wallDict = {"North": True, "South": True, "West": True, "East": True}
        
        # mark as not visited
        self.isVisited = False
    
    #--------------MazeGeneration--------------------
    # given self and other -- connect them by setting the adjacent wall as False
    def connect(self, other):
        drow = other.row - self.row
        dcol = other.col - self.col

        if (drow, dcol) == (-1, 0): # going UP
            self.wallDict["North"] = False
            other.wallDict["South"] = False
        elif (drow, dcol) == (+1, 0): # going DOWN
            self.wallDict["South"] = False
            other.wallDict["North"] = False
        elif (drow, dcol) == (0, -1): # going LEFT
            self.wallDict["West"] = False
            other.wallDict["East"] = False
        elif (drow, dcol) == (0, +1): # going Right
            self.wallDict["East"] = False
            other.wallDict["West"] = False

    #-------------------View-------------------------
    # inspired by Tetris HW
    # drawCell based on the given row and col
    def drawCell(self, app, canvas, row, col):
        # iterate through all directions in wallDict
        for direction in self.wallDict:
            # if True -- draw that wall
            if self.wallDict[direction]:
                self.drawWall(app, canvas, row, col, direction)
    
    # drawWall based on the given row, col, and direction
    def drawWall(self, app, canvas, row, col, direction):
        (x0, y0, x1, y1, x2, y2, x3, y3) = self.getCellBound(app, row, col)
        
        # Based on the direction -- assign wallStart and wallEnd coordinates
        if direction == "North":
            wallStartRow, wallStartCol, wallEndRow, wallEndCol = (x0, y0, x1, y1)
        elif direction == "South":
            wallStartRow, wallStartCol, wallEndRow, wallEndCol = (x2, y2, x3, y3)
        elif direction == "West":
            wallStartRow, wallStartCol, wallEndRow, wallEndCol = (x0, y0, x2, y2)
        elif direction == "East":
            wallStartRow, wallStartCol, wallEndRow, wallEndCol = (x1, y1, x3, y3)
        
        # draw wall based on starting point and ending point
        canvas.create_line(wallStartRow, wallStartCol, wallEndRow, wallEndCol, 
                                                    fill = "white", width = 3)
    
    # returns (x0, y0, x1, y1, x2, y2, x3, y3) bounding box of given cell in grid
    # modified from Tetris HW
    def getCellBound(self, app, row, col):
        cellWidth = (app.width - 2 * app.mazeMargin) / app.mazeCols
        cellHeight = (app.height - app.mazeMargin - app.mazeTopMargin) / app.mazeRows

        # Note: 0,1,2,3 correspond to:
        # upper-left, upper-right, lower-left, lower-right respectively
        x0 = app.mazeMargin + cellWidth * col
        x2 = x0
        x1 = x0 + cellWidth
        x3 = x1

        y0 = app.mazeTopMargin + cellHeight * row
        y1 = y0
        y2 = y0 + cellHeight
        y3 = y2
        return (x0, y0, x1, y1, x2, y2, x3, y3)

#################################################
# Player class
#################################################
class PlayerInMaze(object):
    def __init__(self, app, row, col):
        self.location = [row, col]
        self.stepWidth = (app.width - 2 * app.mazeMargin) / app.mazeCols
        self.stepHeight = (app.height - app.mazeMargin - app.mazeTopMargin) / app.mazeRows
    
    # return player center -- to make drawing easier
    def getPlayerCenter(self, app):
        row, col = self.location
        x = app.mazeMargin + self.stepWidth * (col + 1/2)
        y = app.mazeTopMargin + self.stepHeight * (row + 1/2)
        return (x, y)
    
    # move player based on key pressed
    def movePlayer(self, app, drow, dcol):
        currRow, currCol = self.location
        newRow, newCol = currRow + drow, currCol + dcol

        # return whether the player move is Legal based on the board
        def isLegalMove(app, currRow, currCol, newRow, newCol):
            return app.maze.isLegalMove(app, currRow, currCol, newRow, newCol)

        if isLegalMove(app, currRow, currCol, newRow, newCol):
            self.location = [newRow, newCol]

    def drawPlayer(self, app, canvas):
        playerLocationX, playerLocationY = self.getPlayerCenter(app)
        canvas.create_image(playerLocationX, playerLocationY, 
                anchor = "center", image=ImageTk.PhotoImage(app.maze_player_img))

    def drawTimer(self, app, canvas):
        time = "00:" + str(app.mazeTimer // 1000)
        canvas.create_text(app.width - app.mazeMargin, app.mazeMargin, anchor = "ne", 
                text = f"Time: {time}", font = "Arial 12 bold", fill = "#faed27")
    
#################################################
# Hat class
#################################################
'''
I may make the hat super annoying by letting it move around the board after MVP 
so I just made a class for it:)
'''
class MazeHat(object):
    def __init__(self, app):
        self.location = [app.mazeRows - 1, app.mazeCols - 1]
    
    def getHatCenter(self, app):
        cellWidth = (app.width - 2 * app.mazeMargin) / app.mazeCols
        cellHeight = (app.height - app.mazeMargin - app.mazeTopMargin) / app.mazeRows
    
        row, col = self.location
        x = app.mazeMargin + cellWidth * (col + 1/2)
        y = app.mazeTopMargin + cellHeight * (row + 1/2)
        
        return (x, y)
    
    def drawHat(self, app, canvas):
        hatCenter_x, hatCenter_y = self.getHatCenter(app)
        canvas.create_image(hatCenter_x, hatCenter_y, 
                anchor = "center", image=ImageTk.PhotoImage(app.maze_hat_img))

#################################################
# mazeMode_timerFired
#################################################
def timerFired(app):
    app.mazeTimer -= 100
    if app.mazeTimer <= 0:
        app.mazeGameOver = True
        app.life -= 1
        init(app)

#################################################
# mazeMode_keyPressed
#################################################
def keyPressed(app,event):
    if (event.key == 'Up'):      
        app.mazePlayer.movePlayer(app, -1, 0)
    elif (event.key == 'Down'):  
        app.mazePlayer.movePlayer(app, +1, 0)
    elif (event.key == 'Left'): 
        app.mazePlayer.movePlayer(app, 0, -1)
    elif (event.key == 'Right'): 
        app.mazePlayer.movePlayer(app, 0, +1)
    
    if (event.key == 'h'):      
        app.displaySolution = True
        app.life -= 1
    
    if app.mazePlayer.location == app.mazeHat.location:
        app.mode = "backToCampusMode"

#################################################
# mazeMode_redrawAll
#################################################
def drawAll(app, canvas):
    app.maze.drawBackground(app, canvas)
    app.maze.drawBoard(app, canvas)
    app.mazePlayer.drawPlayer(app, canvas)
    app.mazePlayer.drawTimer(app, canvas)
    app.mazeHat.drawHat(app, canvas)

    if app.displaySolution:
        app.maze.drawSolution(app, canvas)

#################################################
# Helper
#################################################
# return a 2d list with "fill" in each cell
# modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def make2dList(rows, cols, fill):
    return [ ([fill] * cols) for row in range(rows)]

