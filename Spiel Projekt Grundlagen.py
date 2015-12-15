from tkinter import*

def knopf_com1 ():
    print ("Knopf 1")
def knopf_com2():
    print ("Knopf 2")
def knopf_com3():
    print ("Knopf 3")

fenster = Tk()
fenster.title ("Testfenster")
fenster.geometry ("250x250+300+300")

knopf1 = Button (text = "Testknopf 1", command = knopf_com1, bg = "blue", fg = "black")
knopf1.pack (fill = X)

knopf2 = Button (text = "Testknopf 2", command = knopf_com2, bg = "yellow", fg = "red")
knopf2.pack (fill = X)

knopf3 = Button (text = "Testknopf 3", command = knopf_com3, bg = "orange", fg = "white")
knopf3.pack (fill = X)

#mainloop()

from tkinter import*

root = Tk ()
root.title ("Passworteingabe")

label_1 = Label (root, text = "Name")
label_2 = Label (root, text = "Passwort")
entry_1 = Entry (root)
entry_2 = Entry (root)

label_1.grid (row = 0)
label_2.grid (row = 1)

entry_1.grid (row = 0, column = 1)
entry_2.grid (row = 1, column = 1)

c = Checkbutton (root, text = "Lass mich eingelogt")
c.grid (columnspan = 2)

#root.mainloop ()

from tkinter import*

root = Tk ()

canvas = Canvas (root, width = 200, height = 100)
canvas.pack ()

blackline = canvas.create_line (0,0,200,50)
redline = canvas.create_line (0,100,200,50, fill = "red")
greenBox = canvas.create_rectangle (25,25,130,60, fill = "green")

root.mainloop ()
