#Main file from which to run the chemSketch program

from __future__ import division, print_function
from elements import *
from checkStructure import *
from draw import *
from visual import *
import wx
import math

def stop(evt):
    Draw.isPaused = True

def start(evt):
    Draw.isPaused = False

def reveal(evt):
    Draw.showLabels = True

def cover(evt):
    Draw.showLabels = False

text = None
def infoReveal(details):
    #displays information regarding molecule on screen
    global text
    if text != None:
        text.Hide()
    info = "Molecule Information:\n"
    if Molecule.isLegal == True: 
        for key in details: 
            info = info + str(key) + " = " + str(details[key]) + "\n"
        text = wx.StaticText(p, pos=(L,150), size=(200,600), label=info,
                      style=wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE)

def getInstructions(evt): #creates instruction box
    message = """
Enter the formula of a molecule with one center atom.
Use the format "MgCl2".
Do not type in resonance structures or single atoms.
    """
    wx.MessageBox(message,'Instructions', wx.OK | wx.ICON_INFORMATION)

def leave(evt): # called on "Exit under program control" button event
    exit()

def chemSketch(event,inputMol):
    #program that runs once enter is clicked
    #when new formula is enterd, remove previous structure and add new one
    for obj in Draw.objects:
        obj.visible = False
        del obj
    #when new formula is enterd, remove previous labels and add new ones
    for label in Draw.labels:
        label.visible = False
        del label
    run(inputMol) #creates actual molecule
    infoReveal(Molecule.details)
    if Molecule.isLegal == False:
        message = "Invalid input. Please try again."
        wx.MessageBox(message,'Instructions', wx.OK | wx.ICON_INFORMATION)

L = 320 #arbitrary size

#create wxpython window
w = window(width=2*(L+window.dwidth), 
           height=L+window.dheight+window.menuheight,
           menus=True, title='ChemSketch',
           style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | 
           wx.CAPTION | wx.CLOSE_BOX)

# Place a 3D display widget in the left half of the window.
d = 20
disp = display(window=w, x=d, y=d, width=L-2*d, height=L-2*d, 
               forward=-vector(0,1,2))

p = w.panel # Refers to the full region of the window in which to place widgets

tc = wx.TextCtrl(p, pos=(L,25), value="",
            size=(100,20), style=wx.TE_MULTILINE)
tc.SetInsertionPoint(len(tc.GetValue())+1) # position cursor at end of text
tc.SetFocus() #so that keypresses go to the TextCtrl without clicking it
inputMol = "" #initialize input molecule

#create enter button and bind to chemSketch function
enter = wx.Button(p, label="Enter",pos=(L,50))
enter.Bind(wx.EVT_BUTTON, lambda evt, temp=enter: chemSketch(evt, inputMol))

#create pause button and bind to stop rotation function
pause = wx.Button(p, label="Pause",pos=(L+210,50))
pause.Bind(wx.EVT_BUTTON, stop)

#create unpause button and bind to start rotation function
unpause = wx.Button(p, label="Unpause",pos=(L+210,75))
unpause.Bind(wx.EVT_BUTTON, start)

#create show label button and bind to reveal labels function
showLabels = wx.Button(p, label="Show Labels",pos=(L+210,100))
showLabels.Bind(wx.EVT_BUTTON, reveal)

#create hide label button and bind to hide labels function
hideLabels = wx.Button(p, label="Hide Labels",pos=(L+210,125))
hideLabels.Bind(wx.EVT_BUTTON, cover)

#create instructions button and bind to instructions function
instructions = wx.Button(p, label="Instructions",pos=(L,75))
instructions.Bind(wx.EVT_BUTTON, getInstructions)

#create exit button and bind to exit program function
exit_program = wx.Button(p, label="Exit", pos=(L+210,280))
exit_program.Bind(wx.EVT_BUTTON, leave)

while True:
    rate(150) #for smooth rotation
    inputMol = tc.GetValue() #update what is typed in text box
    details = Molecule.details #update molecular properties
    if Draw.isPaused == False: #rotate structure when unpaused
        for obj in Draw.objects:
            obj.rotate(angle=pi/1000,axis=(0,-1,0),origin=(0,0,0))
            obj.rotate(angle=pi/1000,axis=(-1,0,0),origin=(0,0,0))
            obj.rotate(angle=pi/1000,axis=(0,0,-1),origin=(0,0,0))
