# Now back to campus
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    #--------------------Images----------------------
    # image source: 
    # https://rickandmorty.fandom.com/wiki/Portal_Gun
    app.backToCampus_img1 = app.loadImage("img/backToCampus/Term Project Story Line (1).png")
    app.backToCampus_img2 = app.loadImage("img/backToCampus/Term Project Story Line (2).png")
    app.backToCampus_img3 = app.loadImage("img/backToCampus/Term Project Story Line (3).png")
    app.backToCampus_img4 = app.loadImage("img/backToCampus/Term Project Story Line (4).png")
    app.backToCampus_img5 = app.loadImage("img/backToCampus/Term Project Story Line (5).png")
    app.backToCampus_img6 = app.loadImage("img/backToCampus/Term Project Story Line (6).png")
    app.backToCampus_img7 = app.loadImage("img/backToCampus/Term Project Story Line (7).png")
    app.backToCampus_img8 = app.loadImage("img/backToCampus/Term Project Story Line (8).png")
    app.backToCampus_img9 = app.loadImage("img/backToCampus/Term Project Story Line (9).png")
    app.backToCampus_img10 = app.loadImage("img/backToCampus/Term Project Story Line (10).png")
    app.backToCampus_img11 = app.loadImage("img/backToCampus/Term Project Story Line (11).png")
    app.backToCampus_img12 = app.loadImage("img/backToCampus/Term Project Story Line (12).png")
    app.backToCampus_img13 = app.loadImage("img/backToCampus/Term Project Story Line (13).png")
    app.backToCampus_img14 = app.loadImage("img/backToCampus/Term Project Story Line (14).png")
    app.backToCampus_img15 = app.loadImage("img/backToCampus/Term Project Story Line (15).png")

    app.backToCampus_sprites = ([app.backToCampus_img1] + [app.backToCampus_img2] + 
        [app.backToCampus_img3] +[app.backToCampus_img4] +[app.backToCampus_img5] 
        +[app.backToCampus_img6] +[app.backToCampus_img7] +[app.backToCampus_img8] 
        +[app.backToCampus_img9] +[app.backToCampus_img10] +[app.backToCampus_img11] 
        +[app.backToCampus_img12] +[app.backToCampus_img13] +[app.backToCampus_img14] 
        +[app.backToCampus_img15])

    app.backToCampus_spriteCounter = 0
#################################################
# keyPressed
#################################################
def keyPressed(app, event):
    if event.key == "Enter":
        if app.backToCampus_spriteCounter == 14:
            return
        if app.backToCampus_spriteCounter == 3:
            app.backToCampus_spriteCounter += 2
        else:
            app.backToCampus_spriteCounter += 1

#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if app.backToCampus_spriteCounter == 14:
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
                            image=ImageTk.PhotoImage(app.backToCampus_sprites
                                            [int(app.backToCampus_spriteCounter)]))