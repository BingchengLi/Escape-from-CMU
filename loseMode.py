# lose screen
# display lose screen.....
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    # image source: https://www.cmu.edu/piper/news/archives/2017/may/leah-nock.html
    # lose screen made by: Lois Yun (AndrewID: Rahyun Yun)
    app.loseScreen_spritestrip = app.loadImage("img/lose_img.png")
    app.loseScreen_sprites = []
    
    # modified from class notes: https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#newImagesAndImageDraw
    for _ in range(11):
        sprite = app.loseScreen_spritestrip.crop((1000 * _, 0, 1000 * ( _ + 1), 1000))
        sprite = app.scaleImage(sprite, 1/2)
        app.loseScreen_sprites.append(sprite)
    
    app.loseScreen_spriteCounter = 0

    print("Successfully imported loseMode.")

#################################################
# timerFired
#################################################
def timerFired(app):
    # adjusting animation speed
    if 0 <= app.loseScreen_spriteCounter < 4:
        app.loseScreen_spriteCounter += 0.7
    elif app.loseScreen_spriteCounter <= 10:
        app.loseScreen_spriteCounter += 0.1

#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.loseScreen_spriteCounter >= 10:
        if 346 <= event.x <= 450 and 410 <= event.y <= 460:
            app.mode = "mainMenuMode"
        elif 40 <= event.x <= 140 and 410 <= event.y <= 460:
            app.mode = "creditMode"

#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.loseScreen_sprites
                                            [int(app.loseScreen_spriteCounter)]))
