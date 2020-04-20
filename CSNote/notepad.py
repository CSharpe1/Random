###########################################
import tkinter as tk
from tkinter import *
import os
###########################################
###########################################
#       Make Gui container                #
###########################################
gui = tk.Tk(className="CSnote")
gui.geometry("600x600")
###########################################
#       Functions from Buttons            #
###########################################
def save():
    path = "C:/Users/"
    path = os.path.realpath(path)
    os.startfile(path)
def open():
    path = "C:/Users/"
    path = os.path.realpath(path)
    os.startfile(path)
def donothing():
   filewin = Toplevel(gui)
   button = Button(filewin, text="Do nothing button")
   button.pack()
def about():
   filewin = Toplevel(gui)
   button = Button(filewin, text="This is a project a little bit too complicated for me but just testing and trying\n\n\nCreated by Me;\nCharles")
   button.pack()
#########################################
#       Button controls                 #
#########################################
open = tk.Button(gui, text = "open", command = open)
open.pack()
open.place( height = 20, width = 50, x = 0, y = 0)

save = tk.Button(gui, text = "save", command = save)
save.pack()
save.place( height = 20, width = 50, x = 51, y = 0)

save = tk.Button(gui, text = "save", command = save)
save.pack()
save.place( height = 20, width = 50, x = 51, y = 0)

v = tk.IntVar()
linenumber = tk.Radiobutton(gui, text="line numbers",  padx = 10,  variable=v, value=1)
linenumber.pack()
linenumber.place( height = 20, width = 100, x = 101, y = 0)

#########################################
#       Make Menu bar                   #
#########################################
menubar = Menu(gui)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=gui.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
#####
langmenu = Menu(menubar, tearoff=0)
langmenu.add_command(label=".txt", command=donothing)
langmenu.add_command(label=".MD", command=donothing)
langmenu.add_command(label=".html", command=donothing)
langmenu.add_command(label=".css", command=donothing)
langmenu.add_command(label=".py", command=donothing)
menubar.add_cascade(label="Lang", menu=langmenu)

gui.config(menu=menubar)
###########################################
#       TEXT BOX NOTE PAD SECTION         #
###########################################
T = tk.Text(gui)
T.place(height = 500, width = 200  ,x = 11, y = 20,  )
T.insert(tk.END, "Just a text Widget\nin two lines\n")
###########################################
#                                         #
###########################################
gui.mainloop() 
