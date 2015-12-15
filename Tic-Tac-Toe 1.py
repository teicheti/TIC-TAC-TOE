from tkinter import *

import os

class Spiel:
    def __init__ (self, master, Knopf, Ausgabe, Breite, Höhe, Position_x, Position_y, X1, Y1, X2, Y2):

        frame = Frame(master)
        frame.pack()     
        
        self.knopf = Knopf
        self.ausgabe = Ausgabe
        self.width = Breite
        self.height = Höhe
        self.position_x = Position_x
        self.position_y = Position_y

        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2
        
        self.knopf = Button(fenster, text = self.knopf, command = self.makieren_x)
        self.knopf.place(x = self.position_x, y = self.position_y, width = self.width, height = self.height)
    def exit_():
        os._exit()
    def befehl(self):
        print (self.ausgabe)
        
    def makieren_x(self):
        X = spielfeld.create_line (self.x1, self.y1, self.x2, self.y2, width = 2)# (Anfang: x,y ; Ende: x,y)
        X = spielfeld.create_line (self.x1, self.y1+80, self.x2, self.y2-80, width = 2)# (Anfang: x,y ; Ende: x,y)
        self.knopf.destroy()
        
    def makieren_o(self):
        O = spielfeld.create_oval (self.x1, self.y1, self.x2, self.y2, width = 2) #(105,5,195,95, width = 2)    # (linker Punkt, oberer P, rechter P, unterer P)
        self.knopf.destroy()

            
fenster = Tk ()
fenster.title ("Tic-Tac-Toe")
fenster.geometry ("300x350+250+300")

spielfeld =  Canvas (fenster, width = 400, height = 400)
spielfeld.pack ()

senkrechte = spielfeld.create_line (100,0,100,300, width = 3)  # (Anfang: x,y ; Ende: x,y)
senkrechte = spielfeld.create_line (200,0,200,300, width = 3)  # (Anfang: x,y ; Ende: x,y)
waagereechte = spielfeld.create_line (0,100,300,100, width = 3)  # (Anfang: x,y ; Ende: x,y)
waagerrechte = spielfeld.create_line (0,200,300,200, width = 3)


Feld_1 = Spiel (fenster, "Feld 1", "Feld 1 angeklickt",96,96,3,2, 10,10,90,90)
Feld_2 = Spiel (fenster, "Feld 2", "Feld 2 angeklickt",96,96,103,2, 110,10,190,90)
Feld_3 = Spiel (fenster, "Feld 3", "Feld 3 angeklickt",96,96,203,2, 210,10,290,90)
Feld_4 = Spiel (fenster, "Feld 4", "Feld 4 angeklickt",96,96,3,102, 10,110,90,190)
Feld_5 = Spiel (fenster, "Feld 5", "Feld 5 angeklickt",96,96,103,102, 110,110,190,190)
Feld_6 = Spiel (fenster, "Feld 6", "Feld 6 angeklickt",96,96,203,102, 210,110,290,190)
Feld_7 = Spiel (fenster, "Feld 7", "Feld 7 angeklickt",96,96,3,202, 10,210,90,290)
Feld_8 = Spiel (fenster, "Feld 8", "Feld 8 angeklickt",96,96,103,202, 110,210,190,290)
Feld_9 = Spiel (fenster, "Feld 9", "Feld 9 angeklickt",96,96,203,202, 210,210,290,290)

Neustart = Spiel (fenster, "Neustart", "Neustart",75,25,25,310, 0,0,0,0)
Beenden = Spiel (fenster, "Beenden", "Beenden",75,25,200,310, 0,0,0,0)

fenster.mainloop()
