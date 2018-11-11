#!/usr/bin/python

try:
    # for Python2
    from Tkinter import *   ## notice capitalized T in Tkinter 
except ImportError:
    # for Python3
    from tkinter import *   ## notice lowercase 't' in tkinter here
   
def ScoreOutput( param, displayLength ):
    return "0" * (displayLength - len(str(param))) + str(param)

def UpdateTotalScore( score ):
    scoreText.delete(1.0, END)
    scoreText.insert(INSERT, ScoreOutput(score, 8))
    root.update()
    return

def UpdateVodkaScore( score ):
    vodkaText.delete(1.0, END)
    vodkaText.insert(INSERT, ScoreOutput(score, 2))
    root.update()
    return

def UpdateRumScore( score ):
    rumText.delete(1.0, END)
    rumText.insert(INSERT, ScoreOutput(score, 2))
    root.update()
    return

def UpdateWhiskeyScore( score ):
    whiskeyText.delete(1.0, END)
    whiskeyText.insert(INSERT, ScoreOutput(score, 2))
    root.update()
    return

xOffset = 0
yOffset = 0
mainColor = "#138c08"
titleFont = "Arial Std Black"
mainFont = "DJB Get Digital"
largeFontSize = 130
smallFontSize = 90
lowerYPosLabel = 900;
lowerYPosText = 700;
root=Tk()
root.attributes("-fullscreen", True)
root.title("ROBOEXOTICA")
root.configure(background='black')
roboLabel = Label(root, text="ROBOEXOTICA", font=(titleFont, largeFontSize, 'bold'), background='black', fg = mainColor, pady = 100)
roboLabel.pack()

scoreLabel = Label(root, text="Total Score:", font=(mainFont, 28), background='black', fg = mainColor)
vodkaLabel = Label(root, text="VODKA", font=(mainFont, smallFontSize), background='black', fg = mainColor)
rumLabel = Label(root, text="RUM", font=(mainFont, smallFontSize), background='black', fg = mainColor)
whiskeyLabel = Label(root, text="WHISKEY", font=(mainFont, smallFontSize), background='black', fg = mainColor)

scoreLabel.place(x=450 + xOffset, y=450 + yOffset)
vodkaLabel.place(x=300 + xOffset, y=lowerYPosLabel + yOffset)
rumLabel.place(x=860 + xOffset, y=lowerYPosLabel + yOffset)
whiskeyLabel.place(x=1250 + xOffset, y=lowerYPosLabel + yOffset)

scoreText = Text(root)
scoreText.configure(background='black', fg = mainColor, font=(mainFont, smallFontSize + 20), width=8, height=1)
scoreText.place(x=670 + xOffset, y=420 + yOffset)

vodkaText = Text(root)
vodkaText.configure(background='black', fg = mainColor, font=(mainFont, smallFontSize), width=2, height=1)
vodkaText.place(x=400 + xOffset, y=lowerYPosText + yOffset)

rumText = Text(root)
rumText.configure(background='black', fg = mainColor, font=(mainFont, smallFontSize), width=2, height=1)
rumText.place(x=900 + xOffset, y=lowerYPosText + yOffset)

whiskeyText = Text(root)
whiskeyText.configure(background='black', fg = mainColor, font=(mainFont, smallFontSize), width=2, height=1)
whiskeyText.place(x=1350 + xOffset, y=lowerYPosText + yOffset)

UpdateTotalScore(0)
UpdateVodkaScore(0)
UpdateRumScore(0)
UpdateWhiskeyScore(0)
