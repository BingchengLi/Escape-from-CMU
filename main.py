#################################################
# Escape from CMU.py
# Term Project
# Christine Li (bingchel)
#################################################

import cv2
import numpy as np
from cmu_112_graphics import *
import decimal, math
import mainMenuMode, libStoryMode, taskAssignMode, escapeMode, huntToConnectorMode
import jumpToMIMode, enterMIMode, mazeMode, loseMode, backToCampusMode, winMode

#################################################
# __init__
#################################################
def appStarted(app):
    app.mode = "enterMIMode"
    resetAll(app)

def resetAll(app):
    # models for mainMenuMode
    mainMenuMode.init(app)

    # models for libStoryMode
    libStoryMode.init(app)

    # models for taskAssignMode
    taskAssignMode.init(app)

    # models for escapeMode (i.e. campus mode)
    escapeMode.init(app)

    # models for taskAssignMode
    huntToConnectorMode.init(app)

    # models for jumpToMIMode
    jumpToMIMode.init(app)

    # models for enterMIMode
    enterMIMode.init(app)

    # models for mazeMode
    mazeMode.init(app)

    # models for loseMode
    loseMode.init(app)

    # models for backToCampusMode
    backToCampusMode.init(app)

    # models for winMode
    winMode.init(app)

    # life heart system
    # image source: https://opengameart.org/content/platform-pack
    app.life = 3
    app.displayLifeHeart = True
    app.lifeHeartFull_img = app.loadImage("img/Platform pack/PNG/Items/LifeHearth_Full.png")
    app.lifeHeartEmpty_img = app.loadImage("img/Platform pack/PNG/Items/LifeHearth_Empty.png")
    app.lifeHeartWidth, app.lifeHeartHeight = app.lifeHeartFull_img.size
    app.timerDelay = 100

#################################################
# mousePressed
#################################################
def mainMenuMode_mousePressed(app, event):
    mainMenuMode.mousePressed(app, event)

def libStoryMode_mousePressed(app, event):
    libStoryMode.mousePressed(app, event)

def taskAssignMode_mousePressed(app, event):
    taskAssignMode.mousePressed(app, event)

def huntToConnectorMode_mousePressed(app, event):
    huntToConnectorMode.mousePressed(app, event)

def enterMIMode_mousePressed(app, event):
    enterMIMode.mousePressed(app, event)

def backToCampusMode_mousePressed(app, event):
    backToCampusMode.mousePressed(app, event)

#################################################
# keyPressed
#################################################
def libStoryMode_keyPressed(app, event):
    libStoryMode.keyPressed(app, event)

def taskAssignMode_keyPressed(app, event):
    taskAssignMode.keyPressed(app, event)

def escapeMode_keyPressed(app, event):
    escapeMode.keyPressed(app, event)

def huntToConnectorMode_keyPressed(app, event):
    huntToConnectorMode.keyPressed(app, event)

def jumpToMIMode_keyPressed(app, event):
    jumpToMIMode.keyPressed(app, event)

def enterMIMode_keyPressed(app, event):
    enterMIMode.keyPressed(app, event)

def mazeMode_keyPressed(app, event):
    mazeMode.keyPressed(app, event)

def backToCampusMode_keyPressed(app, event):
    backToCampusMode.keyPressed(app, event)

def winMode_keyPressed(app, event):
    winMode.keyPressed(app, event)

#################################################
# timerFired
#################################################
def libStoryMode_timerFired(app):
    libStoryMode.timerFired(app)

def taskAssignMode_timerFired(app):
    taskAssignMode.timerFired(app)

def taskAssignMode_timerFired(app):
    taskAssignMode.timerFired(app)

def jumpToMIMode_timerFired(app):
    jumpToMIMode.timerFired(app)
    # determine life status here
    if app.life == 0:
        app.mode = "loseMode"
        resetAll(app)

def mazeMode_timerFired(app):
    mazeMode.timerFired(app)
    # determine life status here
    if app.life == 0:
        app.mode = "loseMode"
        resetAll(app)

def loseMode_timerFired(app):
    loseMode.timerFired(app)

def escapeMode_timerFired(app):
    escapeMode.timerFired(app)

def huntToConnectorMode_timerFired(app):
    huntToConnectorMode.timerFired(app)

#################################################
# redrawAll
#################################################

def mainMenuMode_redrawAll(app, canvas):
    mainMenuMode.drawAll(app, canvas)

def libStoryMode_redrawAll(app, canvas):
    libStoryMode.drawAll(app, canvas)

def taskAssignMode_redrawAll(app, canvas):
    taskAssignMode.drawAll(app, canvas)
    drawLife(app, canvas)

def escapeMode_redrawAll(app, canvas):
    escapeMode.drawAll(app, canvas)
    drawLife(app, canvas)

def huntToConnectorMode_redrawAll(app, canvas):
    huntToConnectorMode.drawAll(app, canvas)
    drawLife(app, canvas)

def jumpToMIMode_redrawAll(app, canvas):
    jumpToMIMode.drawAll(app, canvas)
    drawLife(app, canvas)

def enterMIMode_redrawAll(app, canvas):
    enterMIMode.drawAll(app, canvas)
    drawLife(app, canvas)

def mazeMode_redrawAll(app, canvas):
    mazeMode.drawAll(app, canvas)
    drawLife(app, canvas)

def loseMode_redrawAll(app, canvas):
    loseMode.drawAll(app, canvas)
    drawLife(app, canvas)

def backToCampusMode_redrawAll(app, canvas):
    backToCampusMode.drawAll(app, canvas)
    drawLife(app, canvas)

def winMode_redrawAll(app, canvas):
    winMode.drawAll(app, canvas)
    drawLife(app, canvas)

def drawLife(app, canvas):
    if app.displayLifeHeart:
        canvas.create_image(app.mazeMargin, app.mazeMargin, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.lifeHeartEmpty_img))
        canvas.create_image(app.mazeMargin + app.lifeHeartWidth, app.mazeMargin, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.lifeHeartEmpty_img))
        canvas.create_image(app.mazeMargin + 2 * app.lifeHeartWidth, app.mazeMargin, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.lifeHeartEmpty_img))

        if app.life == 1 or app.life == 2 or app.life == 3:
            canvas.create_image(app.mazeMargin, app.mazeMargin, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.lifeHeartFull_img))
        
        if app.life == 2 or app.life == 3:
            canvas.create_image(app.mazeMargin + app.lifeHeartWidth, app.mazeMargin, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.lifeHeartFull_img))
        
        if app.life == 3:
            canvas.create_image(app.mazeMargin + 2 * app.lifeHeartWidth, app.mazeMargin, anchor = "nw", 
                            image=ImageTk.PhotoImage(app.lifeHeartFull_img))

#################################################
# main
#################################################
def playGame():
    runApp(width=500, height=500)

def main():
    playGame()

main()