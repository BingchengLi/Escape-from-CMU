# Main Menu Mode
from cmu_112_graphics import *

#################################################
# __init__
#################################################
def init(app):
    # mainMenu_img background source: https://www.dreamstime.com/dark-shadow-hands-body-behind-opaque-glass-makes-look-scary-halloween-concept-shadows-very-image168411496
    # made by: Hannah Chen (AndrewID: ziqic2)
    app.mainMenu_img = app.loadImage("img/mainMenu_img.jpeg")
    app.mainMenu_img = app.scaleImage(app.mainMenu_img, 1/2)

    print("Successfully imported mainMenuMode.")

#################################################
# mousePressed
#################################################
def mousePressed(app, event):
    if 200 <= event.x <= 295 and 365 <= event.y <= 415:
        app.mode = "libStoryMode"
    elif 415 <= event.x <= 475 and 430 <= event.y <= 475:
        app.mode = "creditMode"

#################################################
# view -- draw
#################################################
def drawAll(app, canvas):
    canvas.create_image(0, 0, 
                    anchor = "nw", image=ImageTk.PhotoImage(app.mainMenu_img))
