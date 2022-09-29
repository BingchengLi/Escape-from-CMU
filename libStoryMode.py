# Library Story Mode (story)
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    #-------------------PART 1---------------------
    # sprite sheet created using Google slide and TexturePacker

    # libStoryLine 1 -- waking up in hunt library
    app.displayLibStory1 = True
    app.libStoryLine1_spritestrip = app.loadImage("img/libStoryMode/story1_img.png")
    app.libStory1_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(4):
        sprite = app.libStoryLine1_spritestrip.crop((500 * _, 0, 500 * ( _ + 1), 500))
        app.libStory1_sprites.append(sprite)
    
    app.libStory1_spriteCounter = 0

    #-------------------PART 2---------------------
    # illustration background source: https://www.shutterstock.com/image-vector/vector-illustration-character-tired-businessman-sleeping-630538022
    # made by: Hannah Chen (AndrewID: ziqic2)
    # libStoryLine 2 -- life sucks
    app.displayLibStory2 = False
    app.libStoryLine2_spritestrip = app.loadImage("img/libStoryMode/story2_img.png")
    app.libStory2_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(17):
        sprite = app.libStoryLine2_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.libStory2_sprites.append(sprite)
    
    app.libStory2_spriteCounter = 0

    #-------------------PART 3---------------------
    # image source (phone screen): https://www.shutterstock.com/image-vector/smartphone-mock-application-game-web-page-1569924421
    # image source (invitation): https://www.amazon.com/You-Want-Play-Game-Convention/dp/1691404284
    # libStoryLine 3 -- do you wanna play a game
    app.displayLibStory3 = False
    app.libStoryLine3_spritestrip = app.loadImage("img/libStoryMode/story3_img.png")
    app.libStory3_sprites = []

    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(8):
        sprite = app.libStoryLine3_spritestrip.crop((500 * _, 0, 500 * ( _ + 1), 500))
        app.libStory3_sprites.append(sprite)
    
    app.libStory3_spriteCounter = 0

    print("Successfully imported libStoryMode.")

#################################################
# timerFired
#################################################
def timerFired(app):
    # when displaying libstory part 1
    if app.displayLibStory1:
        # adjusting animation speed
        if 1<= app.libStory1_spriteCounter < 2:
            app.libStory1_spriteCounter += 0.08
        elif app.libStory1_spriteCounter <= 3:
            app.libStory1_spriteCounter += 0.1

    # when displaying libstory part 2
    elif app.displayLibStory2:
        # adjusting animation speed
        if 1 <= app.libStory2_spriteCounter <= 5:
            app.libStory2_spriteCounter += 0.4
        elif 6 <= app.libStory2_spriteCounter <= 7:
            app.libStory2_spriteCounter += 0.6
        elif 10 <= app.libStory2_spriteCounter < 11:
            app.libStory2_spriteCounter += 0.05
        elif 11 <= app.libStory2_spriteCounter <= 12:
            app.libStory2_spriteCounter += 0.5
        elif app.libStory2_spriteCounter <= 16:
            app.libStory2_spriteCounter += 0.1
    
    # when displaying libstory part 3
    elif app.displayLibStory3:
        # adjusting animation speed
        if 3 <= app.libStory3_spriteCounter <= 5:
            app.libStory3_spriteCounter += 0.8
        elif app.libStory3_spriteCounter <= 7:
            app.libStory3_spriteCounter += 0.1

#################################################
# keyPressed
#################################################
def keyPressed(app, event):
    if event.key == "Enter":
        if app.displayLibStory1 and app.libStory1_spriteCounter > 3:
            app.displayLibStory2 = True
            app.displayLibStory1 = False
        elif app.displayLibStory2 and app.libStory2_spriteCounter > 7:
            app.displayLibStory3 = True
            app.displayLibStory2 = False
    
#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.displayLibStory3:
        if 160 <= event.x <= 230 and 350 <= event.y <= 380:
            app.mode = "taskAssignMode"
        elif 245 <= event.x <= 316 and 350 <= event.y <= 380:
            app.mode = "loseMode"
    
#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    if app.displayLibStory1:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.libStory1_sprites
                                            [int(app.libStory1_spriteCounter)]))
    elif app.displayLibStory2:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.libStory2_sprites
                                            [int(app.libStory2_spriteCounter)]))
    elif app.displayLibStory3:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.libStory3_sprites
                                            [int(app.libStory3_spriteCounter)]))
    