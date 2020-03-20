import sys
import tkinter as tk
from tkinter import *
from client import *
from random import randint

clt=None

window=tk.Tk()
window.title("Client Console")

Frame1=tk.Frame(window,highlightbackground="black",highlightthickness=1)
Frame1.grid(row=0,column=0,rowspan=4, sticky=tk.W+tk.E)
l1=tk.Label(Frame1,text="Enter Port Number")
l1.grid(row=3,column=0,sticky = W,pady = 2)

e1 = tk.Text(Frame1, width=20, height=2)
e1.insert(tk.END,"1115")
e1.delete(1.0, tk.END)
e1.grid(row = 3, column = 1, pady = 2)

def start_clt():
    port=e1.get(1.0,tk.END)
    global clt
    if clt == None:
        clt=Client(int(port))
        clt.startListening()
    clt.startclient()

b1=tk.Button(Frame1,text="Start Client",command=start_clt)
b1.grid(row=5,column=0,pady = 2,sticky=tk.W+tk.E)

def stop_clt():
    clt.stopclient()

b3=tk.Button(Frame1,text="Stop Client",command=stop_clt)
b3.grid(row=5,column=1,sticky=tk.W+tk.E,pady = 2)



Frame2=tk.Frame(window,highlightbackground="black",highlightthickness=1)
Frame2.grid(row=5,column=0,rowspan=8,  sticky=tk.W+tk.E)

l5=tk.Label(Frame2,text="Transaction console")
l2=tk.Label(Frame2,text="Enter Your Account Name")
l3=tk.Label(Frame2,text="Enter Beneficiary Name")
l4=tk.Label(Frame2,text="Enter Amount")


l5.grid(row=0,columnspan=2,sticky=tk.W+tk.E)
l2.grid(row=1,column=0,sticky=W)
l3.grid(row=2,column=0,sticky=W)
l4.grid(row=3,column=0,sticky=W)

e2 = tk.Text(Frame2, width=20, height=2)
e2.delete(1.0, tk.END)
e3 = tk.Text(Frame2, width=20, height=2)
e3.delete(1.0, tk.END)
e4 = tk.Text(Frame2, width=20, height=2)
e4.delete(1.0, tk.END)

e2.grid(row = 1, column = 1,sticky = W, pady = 2)
e3.grid(row = 2, column = 1,sticky = W, pady = 2)
e4.grid(row = 3, column = 1,sticky = W, pady = 2)

def transaction():
    trans=str(str(e2.get(1.0,'end-1c'))+" "+str(e3.get(1.0,'end-1c'))+" "+str(e4.get(1.0,tk.END)))
    print(trans)
    chese=clt.cheeseChain.createCheese(str(trans+'\n'))
    if chese !=-1:
        clt.bradcastchain(chese.id)

b2=tk.Button(Frame2,text="Make Transaction",command=transaction)
b2.grid(row=4,columnspan=2,sticky=tk.W+tk.E,pady = 2)



Frame3=tk.Frame(window,highlightbackground="black",highlightthickness=1)
Frame3.grid(row=0,column=1,rowspan=8,  sticky=tk.W+tk.E)

def print_cheese():
    print(clt.cheeseChain)


txt_output = tk.Text(Frame3);
printcheese=tk.Button(Frame3,text="Print Cheese Chain",command=print_cheese)
printcheese.grid(row=0)
txt_output.grid(row=1,sticky = W,rowspan=7)

class stdoutRedirector:
    def __init__(self, tkwidget):
        self.tkwidget = tkwidget

    def write(self, string):
        self.tkwidget.insert('end', string)
        self.tkwidget.see('end')

sys.stdout = stdoutRedirector(txt_output)

window.geometry('900x400')
window.mainloop()

