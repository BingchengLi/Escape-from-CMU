# YOU WIN!
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    #--------------------Images----------------------
    # image source:
    # https://www.shutterstock.com/image-vector/letter-sketch-envelope-drawing-mail-image-75011134
    # https://stock.adobe.com/search?k=thank+you

    app.winMode_img0 = app.loadImage("img/winMode/Term Project Story Line (0).png")
    app.winMode_img1 = app.loadImage("img/winMode/Term Project Story Line (1).png")
    app.winMode_img2 = app.loadImage("img/winMode/Term Project Story Line (2).png")
    app.winMode_img3 = app.loadImage("img/winMode/Term Project Story Line (3).png")
    app.winMode_img4 = app.loadImage("img/winMode/Term Project Story Line (4).png")
    app.winMode_img5 = app.loadImage("img/winMode/Term Project Story Line (5).png")
    app.winMode_img6 = app.loadImage("img/winMode/Term Project Story Line (6).png")
    app.winMode_img7 = app.loadImage("img/winMode/Term Project Story Line (7).png")
    app.winMode_img8 = app.loadImage("img/winMode/Term Project Story Line (8).png")
    app.winMode_img9 = app.loadImage("img/winMode/Term Project Story Line (9).png")
    app.winMode_img10 = app.loadImage("img/winMode/Term Project Story Line (10).png")
    app.winMode_img11 = app.loadImage("img/winMode/Term Project Story Line (11).png")
    app.winMode_img12 = app.loadImage("img/winMode/Term Project Story Line (12).png")
    
    app.winMode_sprites = ([app.winMode_img1] + [app.winMode_img2] + 
                [app.winMode_img3] +[app.winMode_img4] +[app.winMode_img5] 
                +[app.winMode_img6] +[app.winMode_img7] +[app.winMode_img8] 
                +[app.winMode_img9] +[app.winMode_img10] +[app.winMode_img11] 
                +[app.winMode_img12])

    app.winMode_spriteCounter = 0

#################################################
# keyPressed
#################################################
def keyPressed(app, event):
    if event.key == "Enter":
        if app.winMode_spriteCounter == 4 or app.winMode_spriteCounter == 12:
            return
        
        app.winMode_spriteCounter += 1

#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.winMode_spriteCounter == 14:
        if 360 <= event.x <= 475 and 430 <= event.y <= 490:
                app.mode = "escapeMode"
                app.enemyPresented = True
                app.escapePlayer.playerLocationInMap = [4202, 1213]
                app.campusMap.initializeDisplayRange(app)
                
    
#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    canvas.create_image(0, 0, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.winMode_sprites
                                            [int(app.winMode_spriteCounter)]))