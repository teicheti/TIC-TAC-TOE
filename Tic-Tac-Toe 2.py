import os

from tkinter import *

class Spiel:
    
    def __init__ (self, master, Knopf, Breite, Höhe, Position_x, Position_y,
                  x_Anfang, y_Anfang, x_Ende, y_Ende):

        self.knopf = Knopf
        self.width = Breite
        self.height = Höhe
        self.position_x = Position_x
        self.position_y = Position_y
        self.x_anfang = x_Anfang
        self.y_anfang = y_Anfang
        self.x_ende = x_Ende
        self.y_ende = y_Ende
        self.knopf = Button(fenster, text = self.knopf, command = self.befehl)
        self.knopf.place(x = self.position_x, y = self.position_y, width = self.width, height = self.height)
      
    def befehl(self):
        if (self != Beenden and self != Neustart):
            self.makieren_x()
            self.makieren_o()

            self.knopf.destroy()
            
        elif (self == Neustart):
            print ("Neues Spiel")
        elif (self == Beenden):
            os._exit(1)
                
        
    def makieren_x(self):
        X = spielfeld.create_line (self.x_anfang, self.y_anfang, self.x_ende, self.y_ende, width = 2)# (Anfang: x,y ; Ende: x,y)
        X = spielfeld.create_line (self.x_anfang, self.y_anfang+80, self.x_ende, self.y_ende-80, width = 2)# (Anfang: x,y ; Ende: x,y)
                     
    def makieren_o(self):
        O = spielfeld.create_oval (self.x_anfang, self.y_anfang, self.x_ende, self.y_ende, width = 2) #(105,5,195,95, width = 2)    # (linker Punkt, oberer P, rechter P, unterer P)
        
fenster = Tk ()
fenster.title ("Tic-Tac-Toe")
fenster.geometry ("300x350+250+300")

spielfeld = Canvas (fenster, width = 400, height = 400)
spielfeld.pack ()

senkrechte = spielfeld.create_line (100,0,100,300, width = 3)  # (Anfang: x,y ; Ende: x,y)
senkrechte = spielfeld.create_line (200,0,200,300, width = 3)  # (Anfang: x,y ; Ende: x,y)
waagereechte = spielfeld.create_line (0,100,300,100, width = 3)  # (Anfang: x,y ; Ende: x,y)
waagerrechte = spielfeld.create_line (0,200,300,200, width = 3)



        # Zahlen: Breite, HÃ¶he, Position_x, Position_y,    x_Anfang, y_Anfang, x_Ende, y_Ende 

Feld_1 = Spiel (fenster, "Feld_1",96,96,3,2, 10,10,90,90)
Feld_2 = Spiel (fenster, "Feld 2",96,96,103,2, 110,10,190,90)
Feld_3 = Spiel (fenster, "Feld 3",96,96,203,2, 210,10,290,90)
Feld_4 = Spiel (fenster, "Feld 4",96,96,3,102, 10,110,90,190)
Feld_5 = Spiel (fenster, "Feld 5",96,96,103,102, 110,110,190,190)
Feld_6 = Spiel (fenster, "Feld 6",96,96,203,102, 210,110,290,190)
Feld_7 = Spiel (fenster, "Feld 7",96,96,3,202, 10,210,90,290)
Feld_8 = Spiel (fenster, "Feld 8",96,96,103,202, 110,210,190,290)
Feld_9 = Spiel (fenster, "Feld 9",96,96,203,202, 210,210,290,290)

Neustart = Spiel (fenster, "Neustart",75,25,25,310, 0,0,0,0)
Beenden = Spiel (fenster, "Beenden",75,25,200,310, 0,0,0,0)

fenster.mainloop()
