#Imports and Declarations
import Tkinter
import tkMessageBox
import SimpleHTTPServer
import SocketServer
import os
import sys
from Tkinter import *
root = Tk()
root.wm_title("OpenServe")

#Global Values
global p
global v
global f

#Method Declarations
def buttonClicked():
  callback()
  port()
  portdef()   
def callback():
  global v
  v=str( e.get() )
def port():
	global f
	global p
	p =int( f.get() )
def portdef():
	global f
	global p
	p = 80

def ServerCall():
	global v
	global f
	global p	
	os.system("cd "+repr(v)+" ; python -m SimpleHTTPServer "+repr(p)+" ")
	root.after(10*1000, root.quit)
def quit():
	global root
	root.quit()


#Two Entry Boxes 
L1 = Label(root, text="Folder path:")
L1.pack()
e = Entry(root, width=30)
e.pack()
e.focus_set()
L2 = Label(root, text="Port:")
L2.pack()
f= Entry(root, width=8)
f.pack()


#Buttons
R = Radiobutton(root, text="Auto Port 80", value=1, command = portdef)
R.pack()
C = Button(root, text="Setup", width=10, command= buttonClicked)
C.pack()
B = Button(root, text ="Start Serving", command = ServerCall)
B.pack()
root.mainloop()
