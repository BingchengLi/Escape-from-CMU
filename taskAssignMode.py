# Task Assign Mode (story)
# After Library Story
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    #-------------------PART 1---------------------
    # sprite sheet created using Google slide and TexturePacker
    # logo source: https://www.buytshirtdesigns.net/t-shirt-design/squid-game-3d-fx/

    # To Squid Game: Thank you so much for inspiration!
    # To whoever is reviewing my code now, if you haven't watched Squid Game...
    # Please watch it. It's quite fun!

    # taskStoryLine 1 -- invitation accepted
    app.displayTaskStory1 = True
    app.taskStoryLine1_spritestrip = app.loadImage("img/taskStoryMode/story1_img.png")
    app.taskStory1_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(16):
        sprite = app.taskStoryLine1_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.taskStory1_sprites.append(sprite)
    
    app.taskStory1_spriteCounter = 0

    #-------------------PART 2---------------------
    # taskStoryLine 2 -- task assign
    app.displayTaskStory2 = False
    app.taskStoryLine2_spritestrip = app.loadImage("img/taskStoryMode/story2_img.png")
    app.taskStory2_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(8):
        sprite = app.taskStoryLine2_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.taskStory2_sprites.append(sprite)
    
    app.taskStory2_spriteCounter = 0

    #-------------------PART 3---------------------
    # taskStoryLine 3 -- life heart info
    app.displayTaskStory3 = False
    app.taskStoryLine3_spritestrip = app.loadImage("img/taskStoryMode/story3_img.png")
    app.taskStory3_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(7):
        sprite = app.taskStoryLine3_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.taskStory3_sprites.append(sprite)
    
    app.taskStory3_spriteCounter = 0

    print("Successfully imported taskAssignMode.")

#################################################
# timerFired
#################################################
def timerFired(app):
    # when displaying task story part 1
    if app.displayTaskStory1:
        # adjusting animation speed
        if 1 <= app.taskStory1_spriteCounter < 3:
            app.taskStory1_spriteCounter += 0.8
        elif 5 <= app.taskStory1_spriteCounter < 6:
            app.taskStory1_spriteCounter += 0.06
        elif 12 <= app.taskStory1_spriteCounter < 13:
            app.taskStory1_spriteCounter += 2
        elif app.taskStory1_spriteCounter <= 15:
            app.taskStory1_spriteCounter += 0.08

    # when displaying task story part 2
    elif app.displayTaskStory2:
        # adjusting animation speed
        if 4 <= app.taskStory2_spriteCounter < 5:
            app.taskStory2_spriteCounter += 0.05
        elif app.taskStory2_spriteCounter <= 7:
            app.taskStory2_spriteCounter += 0.1
    
    # when displaying task story part 3
    elif app.displayTaskStory3:
        # adjusting animation speed
        if 4 <= app.taskStory3_spriteCounter < 5:
            app.taskStory3_spriteCounter += 0.1
        elif app.taskStory3_spriteCounter <= 6:
            app.taskStory3_spriteCounter += 0.07

#################################################
# keyPressed
#################################################
def keyPressed(app, event):
    if event.key == "Enter":
        if app.displayTaskStory2 and app.taskStory2_spriteCounter > 6:
            app.displayTaskStory3 = True
            app.displayTaskStory2 = False
        if app.displayTaskStory3 and app.taskStory3_spriteCounter > 6:
            app.displayLifeHeart = True
            app.mode = "escapeMode"
            app.escapePlayer.playerLocationInMap = [2213, 2654]
            app.campusMap.initializeDisplayRange(app)
    
#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.displayTaskStory1:
        if 155 <= event.x <= 460 and 388 <= event.y <= 472:
            app.displayTaskStory2 = True
            app.displayTaskStory1 = False
    
#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    if app.displayTaskStory1:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.taskStory1_sprites
                                            [int(app.taskStory1_spriteCounter)]))
    elif app.displayTaskStory2:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.taskStory2_sprites
                                            [int(app.taskStory2_spriteCounter)]))
    elif app.displayTaskStory3:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.taskStory3_sprites
                                            [int(app.taskStory3_spriteCounter)]))