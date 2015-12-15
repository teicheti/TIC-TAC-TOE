import os

from tkinter import *

fenster = Tk ()

class SPIELFELD:
    def __init__ (self, spielfeld):

        self.spieler = "x"

        fenster.title ("Tic-Tac-Toe")
        fenster.geometry ("300x350+250+300")

        self.spielfeld = Canvas (fenster, width = 400, height = 400)
        self.spielfeld.pack ()
        
        senkrechte = self.spielfeld.create_line (100,0,100,300, width = 3)  # (Anfang: x,y ; Ende: x,y)
        senkrechte = self.spielfeld.create_line (200,0,200,300, width = 3)  # (Anfang: x,y ; Ende: x,y)
        waagereechte = self.spielfeld.create_line (0,100,300,100, width = 3)  # (Anfang: x,y ; Ende: x,y)
        waagerrechte = self.spielfeld.create_line (0,200,300,200, width = 3)

    def makieren_x (self, x1, y1, x2, y2):
       
        X = self.spielfeld.create_line (x1, y1, x2, y2, width = 2)# (Anfang: x,y ; Ende: x,y)
        X = self.spielfeld.create_line (x1, y1+80, x2, y2-80, width = 2)# (Anfang: x,y ; Ende: x,y)
               
    def makieren_o (self, x1, y1, x2, y2):

        O = self.spielfeld.create_oval (x1, y1, x2, y2, width = 2) #(105,5,195,95, width = 2)    # (linker Punkt, oberer P, rechter P, unterer P)

class SPIELEN:
    def __init__ (self, Knopf, Breite, Höhe, Position_x, Position_y, X1, Y1, X2, Y2):
        
        self.knopf = Knopf
        self.width = Breite
        self.height = Höhe
        self.position_x = Position_x
        self.position_y = Position_y

        self.x1 = X1
        self.y1 = Y1
        self.x2 = X2
        self.y2 = Y2
        
        self.knopf = Button (fenster, text = self.knopf, command = self.befehl)
        self.knopf.place (x = self.position_x, y = self.position_y, width = self.width, height = self.height)
      

    def befehl(self):
        
        if (self != Beenden and self != Neustart):
            if (SPIELFELD.spieler == "x"):
                SPIELFELD.makieren_x (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "y"
            elif (SPIELFELD.spieler == "y"):
                SPIELFELD.makieren_o (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "x"
                
            self.knopf.destroy ()
            
        elif (self == Neustart):
            print ("NEUES SPIEL")
            
        elif (self == Beenden):
            os._exit(1)        

    

SPIELFELD = SPIELFELD ("Feld")

Feld_1 = SPIELEN ("Feld 1", 96,96,3,2, 10,10,90,90)
Feld_2 = SPIELEN ("Feld 2", 96,96,103,2, 110,10,190,90)
Feld_3 = SPIELEN ("Feld 3",96,96,203,2, 210,10,290,90)
Feld_4 = SPIELEN ("Feld 4",96,96,3,102, 10,110,90,190)
Feld_5 = SPIELEN ("Feld 5", 96,96,103,102, 110,110,190,190)
Feld_6 = SPIELEN ("Feld 6", 96,96,203,102, 210,110,290,190)
Feld_7 = SPIELEN ("Feld 7", 96,96,3,202, 10,210,90,290)
Feld_8 = SPIELEN ("Feld 8", 96,96,103,202, 110,210,190,290)
Feld_9 = SPIELEN ("Feld 9", 96,96,203,202, 210,210,290,290)

Neustart = SPIELEN ("Neustart", 75,25,25,310, 0,0,0,0)
Beenden = SPIELEN ("Beenden", 75,25,200,310, 0,0,0,0)

fenster.mainloop ()
