# Meet with this men in black
# After Task Assign Mode (story)
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    #-------------------PART 1---------------------
    # sprite sheet created using Google slide and TexturePacker

    # connectorStoryLine 1 -- introduce himself
    app.displayConnectorStory1 = True
    app.connectorStoryLine1_spritestrip = app.loadImage("img/connectorStoryLine/story1_img.png")
    app.connectorStory1_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(5):
        sprite = app.connectorStoryLine1_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory1_sprites.append(sprite)
    
    app.connectorStory1_spriteCounter = 0

    #-------------------PART 2---------------------
    # connectorStoryLine 2 -- answer question
    app.displayConnectorStory2 = False
    app.connectorStoryLine2_spritestrip = app.loadImage("img/connectorStoryLine/story2_img.png")
    app.connectorStory2_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(8):
        sprite = app.connectorStoryLine2_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory2_sprites.append(sprite)
    
    app.connectorStory2_spriteCounter = 0

    #-------------------PART 3---------------------
    # connectorStoryLine 3 -- more info about hat
    app.displayConnectorStory3 = False
    app.connectorStoryLine3_spritestrip = app.loadImage("img/connectorStoryLine/story3_img.png")
    app.connectorStory3_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(6):
        sprite = app.connectorStoryLine3_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory3_sprites.append(sprite)
    
    app.connectorStory3_spriteCounter = 0

    #-------------------PART 4---------------------
    # connectorStoryLine 4 -- more info about hat
    app.displayConnectorStory4 = False
    app.connectorStoryLine4_spritestrip = app.loadImage("img/connectorStoryLine/story4_img.png")
    app.connectorStory4_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(2):
        sprite = app.connectorStoryLine4_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory4_sprites.append(sprite)
    
    app.connectorStory4_spriteCounter = 0

    #-------------------PART 5---------------------
    # connectorStoryLine 5 -- hat info page
    app.displayConnectorStory5 = False
    app.connectorStoryLine5_spritestrip = app.loadImage("img/connectorStoryLine/story5_img.png")
    app.connectorStory5_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part5.html#newImagesAndImageDraw
    for _ in range(4):
        sprite = app.connectorStoryLine5_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory5_sprites.append(sprite)
    
    app.connectorStory5_spriteCounter = 0

    #-------------------PART 6---------------------
    # connectorStoryLine 6 -- hat info page
    app.displayConnectorStory6 = False
    app.connectorStoryLine6_spritestrip = app.loadImage("img/connectorStoryLine/story6_img.png")
    app.connectorStory6_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part6.html#newImagesAndImageDraw
    for _ in range(11):
        sprite = app.connectorStoryLine6_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory6_sprites.append(sprite)
    
    app.connectorStory6_spriteCounter = 0

    #-------------------PART 7---------------------
    # connectorStoryLine 7 -- hat info page
    app.displayConnectorStory7 = False
    app.connectorStoryLine7_spritestrip = app.loadImage("img/connectorStoryLine/story7_img.png")
    app.connectorStory7_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part7.html#newImagesAndImageDraw
    for _ in range(7):
        sprite = app.connectorStoryLine7_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.connectorStory7_sprites.append(sprite)
    
    app.connectorStory7_spriteCounter = 0

    #-------------------PART 8---------------------
    # connectorStoryLine 8 -- hat info page
    app.displayConnectorStory8 = False
    
    app.connectorStory8 = app.loadImage("img/connectorStoryLine/story8_img.png")
    app.connectorStory8 = app.scaleImage(app.connectorStory8, 1/2)

    print("Successfully imported huntToConnectorMode.")

#################################################
# timerFired
#################################################
def timerFired(app):
    # when displaying connector story part 1
    if app.displayConnectorStory1:
        if app.connectorStory1_spriteCounter <= 4:
            app.connectorStory1_spriteCounter += 0.08

    # when displaying connector story part 2
    elif app.displayConnectorStory2:
        # adjusting animation speed
        if 0 <= app.connectorStory2_spriteCounter <= 1:
            app.connectorStory2_spriteCounter += 0.2
        elif app.connectorStory2_spriteCounter <= 7:
            app.connectorStory2_spriteCounter += 0.08
    
    # when displaying connector story part 3
    elif app.displayConnectorStory3:
        if app.connectorStory3_spriteCounter <= 5:
            app.connectorStory3_spriteCounter += 0.06
    
    # when displaying connector story part 4
    elif app.displayConnectorStory4:
        if app.connectorStory4_spriteCounter <= 1:
            app.connectorStory4_spriteCounter += 0.09
    
    # when displaying connector story part 5
    elif app.displayConnectorStory5:
        if app.connectorStory5_spriteCounter <= 3:
            app.connectorStory5_spriteCounter += 0.06
    
    # when displaying connector story part 6
    elif app.displayConnectorStory6:
        if app.connectorStory6_spriteCounter <= 10:
            app.connectorStory6_spriteCounter += 0.09
    
    # when displaying connector story part 7
    elif app.displayConnectorStory7:
        if app.connectorStory7_spriteCounter <= 6:
            app.connectorStory7_spriteCounter += 0.1
    
            
#################################################
# keyPressed
#################################################
def keyPressed(app, event):
    if app.displayConnectorStory2 and app.connectorStory2_spriteCounter > 7:
            app.displayConnectorStory3 = True
            app.displayConnectorStory2 = False
    elif app.displayConnectorStory3 and app.connectorStory3_spriteCounter > 5:
            app.displayConnectorStory4 = True
            app.displayConnectorStory3 = False
    elif app.displayConnectorStory5 and app.connectorStory5_spriteCounter > 3:
            app.displayConnectorStory6 = True
            app.displayConnectorStory5 = False
    elif app.displayConnectorStory6 and app.connectorStory6_spriteCounter > 10:
            app.displayConnectorStory7 = True
            app.displayConnectorStory6 = False
    elif app.displayConnectorStory7 and app.connectorStory7_spriteCounter > 6:
            app.displayConnectorStory8 = True
            app.displayConnectorStory7 = False
        
#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.displayConnectorStory1:
        if 150 <= event.x <= 460 and 388 <= event.y <= 490:
            app.displayConnectorStory2 = True
            app.displayConnectorStory1 = False
    elif app.displayConnectorStory4:
        if 150 <= event.x <= 460 and 388 <= event.y <= 490:
            app.displayConnectorStory5 = True
            app.displayConnectorStory4 = False
    elif app.displayConnectorStory8:
        if 360 <= event.x <= 475 and 430 <= event.y <= 490:
            app.timerDelay = 32
            app.mode = "jumpToMIMode"

#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    if app.displayConnectorStory1:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory1_sprites
                                            [int(app.connectorStory1_spriteCounter)]))
    elif app.displayConnectorStory2:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory2_sprites
                                            [int(app.connectorStory2_spriteCounter)]))
    elif app.displayConnectorStory3:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory3_sprites
                                            [int(app.connectorStory3_spriteCounter)]))
    elif app.displayConnectorStory4:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory4_sprites
                                            [int(app.connectorStory4_spriteCounter)]))
    elif app.displayConnectorStory5:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory5_sprites
                                            [int(app.connectorStory5_spriteCounter)]))
    elif app.displayConnectorStory6:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory6_sprites
                                            [int(app.connectorStory6_spriteCounter)]))
    elif app.displayConnectorStory7:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory7_sprites
                                            [int(app.connectorStory7_spriteCounter)]))
    elif app.displayConnectorStory8:
        canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.connectorStory8))
                                            

