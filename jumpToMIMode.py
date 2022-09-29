# Jump to Mellon Institue Mode
from cmu_112_graphics import *
import random
import copy

#################################################
# __init__
#################################################
def init(app):
    #-------------------jumpToMI---------------------
    # jumpToMI Game Stage Setting
    app.generateInitPlatform = True
    app.playerJump = True
    app.playerJumpStage = 12

    # jumpToMI parameters
    app.jumpMargin = 30
    app.heightLevelInterval = 50
    app.scrollScreen = 0
    app.heightPerScroll = 10
    app.scrollCount = 0
    app.jumpingHeight = 965
    app.timeCount = 0

    # load img for jumpToMI
    loadImage(app)

    # app.jump set up -- create an instance 
    app.jump = JumpToMI(app)
    app.jump.generatePlatform(app)
    app.jump.initPlayerLocation()

# image source: https://opengameart.org/content/platform-pack
# bg photo: https://www.pinterest.com/pin/155444624629706321/
def loadImage(app):
    app.player_img = app.loadImage("img/Platform pack/PNG/Characters/LightBlue_Front1.png")
    app.player_img = app.scaleImage(app.player_img, 1/4)
    app.block_img = app.loadImage("img/Platform pack/PNG/Items/FloatingBar_Brown.png")
    app.bg_img = app.loadImage("img/bg_img.jpeg")

#################################################
# Game class
#################################################
class JumpToMI(object):
    #-------------------Model------------------------
    def __init__(self, app):
        self.platformLocations = [[-100, -100]]
        self.playerLocation = [[-100, -100]]
        self.lastLand = [[-100, -100]]

    # initialize player location when calling it
    # make sure player stand on the first platform
    def initPlayerLocation(self):
        self.platformLocations.remove([-100, -100])
        self.playerLocation = copy.deepcopy(self.platformLocations[0])
        self.lastLand = copy.deepcopy(self.playerLocation)

    #-------------------Controller--------------------
    # randomly generate initial platforms
    def generatePlatform(self, app):
        # get platform parameters from app.block_img
        platformWidth = app.block_img.size[0]
        
        # make sure there's only one block in the ground level
        buttomPlatformMid = random.randint(app.jumpMargin + int(platformWidth/2), 
                            app.width - app.jumpMargin - int(platformWidth/2))
        self.platformLocations.append([buttomPlatformMid, 
                                                app.height - app.jumpMargin])

        # iterate through each height level -- append platform location to list
        for heightLevel in range(app.height - app.jumpMargin - app.heightLevelInterval,
                                 - app.jumpMargin -1, - app.heightLevelInterval):
            # Note: the range covers one level above the screen
            # so the new level will always show up when we move down
            platformNum = self.generateHeightLevel(app, heightLevel)
            
            # clear the area above buttom platform
            # check through the buttom three levels
            if (heightLevel == app.height - app.jumpMargin - app.heightLevelInterval
                or heightLevel == app.height - app.jumpMargin - 2 * app.heightLevelInterval
                or heightLevel == app.height - app.jumpMargin - 3 * app.heightLevelInterval):
                # iterate through each platform locations
                for index in range(platformNum):
                    platformX = self.platformLocations[- index - 1][0]
                    # when the platform is above buttomPlatform
                    while (buttomPlatformMid - platformWidth < platformX
                        < buttomPlatformMid + platformWidth):
                        # randomly move to clear the area
                        sign = random.choice([+1, -1])
                        platformX += sign * platformWidth
                    self.platformLocations[- index - 1][0] = platformX

    def generateHeightLevel(self, app, heightLevel):
        # get platform parameters from app.block_img
        platformWidth = app.block_img.size[0]

        # use random.randint() as a generator and assign platformNum to result
        platformNumGen = random.randint(1, 5)
        # 1/8 chance to place 0 platform 
        # 1/4 chance to place 1 platform or 3 platforms
        # 3/8 chance to place 2 platforms
        if platformNumGen == [1, 2]:
            platformNum = 1
        elif platformNumGen in [3, 4]:
            platformNum = 2
        else:
            platformNum = 3

        # based on randomly-generated platformNum -- place platforms
        # no platform -- pass
        if platformNum == 0:
            pass

        # one or two platform -- randomly place
        elif platformNum == 1:
            platformMid = random.randint(app.jumpMargin + int(platformWidth/2), 
                                app.width - app.jumpMargin - int(platformWidth/2))
            self.platformLocations.append([platformMid, heightLevel])

        elif platformNum == 2:
            platform1Mid = random.randint(app.jumpMargin + int(platformWidth/2), 
                        app.width - app.jumpMargin - 3 * int(platformWidth/2))
            self.platformLocations.append([platform1Mid, heightLevel])
            platform2Mid = random.randint(platform1Mid + platformWidth, 
                            app.width - app.jumpMargin - int(platformWidth/2))
            self.platformLocations.append([platform2Mid, heightLevel])

        # three platforms -- relatively evenly distributed
        elif platformNum == 3:
            platform1Mid = random.randint(int(platformWidth/2 + app.jumpMargin),
                                int(app.width / 3 - platformWidth/2- app.jumpMargin))
            self.platformLocations.append([platform1Mid, heightLevel])
            platform2Mid = random.randint(platform1Mid + int(platformWidth/2), 
                                    int(app.width * 2 / 3 - platformWidth/2))
            self.platformLocations.append([platform2Mid, heightLevel])
            platform3Mid = random.randint(int(app.width * 2 / 3), 
                            int(app.width - app.jumpMargin - platformWidth/2))
            self.platformLocations.append([platform3Mid, heightLevel])
        
        return platformNum

    def playerJumpUp(self, app):
        # based on the formula: vt**2 - v0**2 = 2g*distance
        if app.playerJump:
            self.playerLocation[1] -= 0.8 * (app.playerJumpStage**2 - 
                                                (app.playerJumpStage - 1)**2)
            app.playerJumpStage -= 1
            if app.playerJumpStage == 0:
                app.playerJump = False
        
        else:
            app.playerJumpStage -= 1
            playerFallingStage = - app.playerJumpStage
            self.playerLocation[1] += 0.8 * (playerFallingStage**2 - 
                                                (playerFallingStage - 1)**2)
            
            # return True when collide with a platform
            def collisionWithPlatform(self, app):
                for platformX, platformY in self.platformLocations:
                    playerX, playerY = self.playerLocation
                    playerWidth, playerHeight = app.player_img.size
                    
                    # if collide with the platform (in the collision range)
                    if (platformX - 0.8 * playerWidth < playerX < platformX + 0.8 * playerWidth
                        and platformY - 0.2 * playerHeight < playerY <= platformY + 0.4 * playerHeight):
                        if (platformY != app.height - app.jumpMargin 
                                                and app.playerJumpStage != -12):
                            # add to app.scrollScreen
                            # keep track on mission that needs to complete
                            intervalNum = int((app.height - app.jumpMargin - app.heightLevelInterval - platformY) / 
                                                            app.heightPerScroll)
                            app.scrollScreen = intervalNum
                        
                        return True
                return False
                
            if collisionWithPlatform(self, app):
                app.playerJumpStage = 12
                app.playerJump = True
    
    def playerMove(self, app, drow):
        playerWidth = app.player_img.size[0]
        if (playerWidth <= self.playerLocation[0] + drow * 8 
                                                    <= app.width - playerWidth): 
            self.playerLocation[0] += drow * 8

    def scrollScreen(self, app):
        if app.scrollScreen == 0:
            return

        else:
            # move player
            self.playerLocation[1] += app.heightPerScroll

            # iterate through all platforms and move
            index = 0
            while index < len(self.platformLocations):
                self.platformLocations[index][1] += app.heightPerScroll
                # remove out of screen platforms
                if self.platformLocations[index][1] > app.width:
                    self.platformLocations.pop(index)
                else:
                    index += 1

            # keep count of scrolls
            app.scrollScreen -= 1
            app.jumpingHeight -= 4
            app.scrollCount = (app.scrollCount + 1) % 5

            # generate new height level when scrolled for five times
            if app.scrollCount == 0:
                self.generateHeightLevel(app, - app.jumpMargin)
            
    #-------------------View-------------------------
    def drawBackground(self, app, canvas):
        canvas.create_image(app.width/2, 0, 
                        anchor = "n", image=ImageTk.PhotoImage(app.bg_img))

    def drawPlatform(self, app, canvas):
        for platformLocationX, platformLocationY in self.platformLocations:
            if platformLocationY >= 2 * app.jumpMargin:
                canvas.create_image(platformLocationX, platformLocationY, 
                            anchor = "n", image=ImageTk.PhotoImage(app.block_img))
    
    def drawPlayer(self, app, canvas):
        playerLocationX, playerLocationY = self.playerLocation
        canvas.create_image(playerLocationX, playerLocationY, 
                        anchor = "s", image=ImageTk.PhotoImage(app.player_img))

    def drawDistance(self, app, canvas):
        canvas.create_text(app.width / 2, app.jumpMargin, anchor = "n", 
                text = f"Distance to Mellon Institute: {app.jumpingHeight} m", 
                font = "Arial 16 bold", fill = "white")

    def drawAll(self, app, canvas):
        self.drawBackground(app, canvas)
        self.drawPlatform(app, canvas)
        self.drawPlayer(app, canvas)
        self.drawDistance(app, canvas)

#################################################
# jumpToMIMode_keyPressed
#################################################
def keyPressed(app, event):
    if (event.key == 'Left'): 
        app.jump.playerMove(app, -1)
    elif (event.key == 'Right'): 
        app.jump.playerMove(app, +1)

#################################################
# jumpToMIMode_timerFired
#################################################
def timerFired(app):
    app.timeCount += 1
    app.jump.playerJumpUp(app)
    app.jump.scrollScreen(app)

    if app.jump.playerLocation[1] > app.height + 3 * app.jumpMargin:
        app.life -= 1
        init(app)

    if app.jumpingHeight <= 0:
        app.mode = "enterMIMode"
        app.timerDelay = 100
    
#################################################
# Model to View -- drawing functions
#################################################
def drawAll(app, canvas):
    app.jump.drawAll(app, canvas)

