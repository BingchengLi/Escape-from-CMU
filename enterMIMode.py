# Enter MI Mode
# Finish the jumping stage and assign maze task
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    #--------------------Images----------------------
    app.enterMI_img1 = app.loadImage("img/enterMI/1.png")
    app.enterMI_img1 = app.scaleImage(app.enterMI_img1, 1/2)
    app.enterMI_img2 = app.loadImage("img/enterMI/2.png")
    app.enterMI_img2 = app.scaleImage(app.enterMI_img2, 1/2)
    app.enterMI_img3 = app.loadImage("img/enterMI/3.png")
    app.enterMI_img3 = app.scaleImage(app.enterMI_img3, 1/2)
    app.enterMI_img4 = app.loadImage("img/enterMI/4.png")
    app.enterMI_img4 = app.scaleImage(app.enterMI_img4, 1/2)
    app.enterMI_img5 = app.loadImage("img/enterMI/5.png")
    app.enterMI_img5 = app.scaleImage(app.enterMI_img5, 1/2)
    app.enterMI_img6 = app.loadImage("img/enterMI/6.png")
    app.enterMI_img6 = app.scaleImage(app.enterMI_img6, 1/2)
    app.enterMI_img7 = app.loadImage("img/enterMI/7.png")
    app.enterMI_img7 = app.scaleImage(app.enterMI_img7, 1/2)

    app.enterMI_sprites = [app.enterMI_img1] + [app.enterMI_img2] + [app.enterMI_img3] + [app.enterMI_img4] + [app.enterMI_img5] +[app.enterMI_img6] +[app.enterMI_img7]    
    app.enterMI_spriteCounter = 0

#################################################
# keyPressed
#################################################
def keyPressed(app, event):
    if event.key == "Enter":
        if app.enterMI_spriteCounter == 6:
            return
        app.enterMI_spriteCounter += 1

#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.enterMI_spriteCounter == 6:
        if 360 <= event.x <= 475 and 430 <= event.y <= 490:
                app.mode = "mazeMode"
                app.timerDelay = 100
                
#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.enterMI_sprites
                                            [int(app.enterMI_spriteCounter)]))
    