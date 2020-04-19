import tkinter as tk
import os


gui = tk.Tk(className="CSnote")
gui.geometry("600x600")




#with open("C:/Users/charles.sharpe/OneDrive - Global Graphics PLC/Documents/CS/Random/other/csnotetest.txt", "r") as f:
#    tk.Label(gui, text=f.read()).pack()






#####################################################
##          Functions from Buttons                 ##
#####################################################
def save():
    path = "C:/Users/charles.sharpe/OneDrive - Global Graphics PLC/Documents/CS/Random"
    path = os.path.realpath(path)
    os.startfile(path)
#    file1 = open(path,"a")#append mode 

    

def open():
    path = "C:/Users/charles.sharpe/OneDrive - Global Graphics PLC/Documents/CS/Random"
    path = os.path.realpath(path)
    os.startfile(path)
#    with open("C:/Users/charles.sharpe/OneDrive - Global Graphics PLC/Documents/CS/Random/other/csnotetest.txt", "r") as f:
#        tk.Label(gui, text=f.read()).pack()


def line_Num():
    print("Line Number")



######################################################
##          Button controls                         ##
######################################################
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













gui.mainloop() 
