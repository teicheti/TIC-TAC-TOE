import os   #os importieren (zum Beenden des Programmes)

from tkinter import *

from tkinter import ttk

class SPIELFELD:
    def __init__ (self):
        
        self.beginnen = 0
        
        self.spieler = "x"  #Für Spielerwechsel festlegen

        self.sieger = 0     #Für befehl definieren

        self.beendet = 0
        
        self.gewinner = ["","","","","","","","",""]    #Gewinner Liste erstellen

        self.spielfeld = Canvas (fenster, width = 300, height = 350)
        self.spielfeld.pack ()  #Canvas Größe festlegen (Bezug auf fenster)
        
    def markieren_x (self, x1, y1, x2, y2):
        X = self.spielfeld.create_line (x1, y1, x2, y2, width = 3, fill = "red")  # (Anfang: x,y ; Ende: x,y)
        X = self.spielfeld.create_line (x1, y1+80, x2, y2-80, width = 3, fill = "red")    # (Anfang: x,y ; Ende: x,y)
        #Kreuz zeichnen
        
    def markieren_o (self, x1, y1, x2, y2):
        O = self.spielfeld.create_oval (x1, y1, x2, y2, width = 3, outline = "blue")   # (linker Punkt, oberer P, rechter P, unterer P)
        # Kreis zeichnen
        
    def neustart (self):
        self.spielfeld.delete (ALL)
        senkrechte = self.spielfeld.create_line (100,0,100,300, width = 3)  
        senkrechte = self.spielfeld.create_line (200,0,200,300, width = 3)  
        waagerrechte = self.spielfeld.create_line (0,100,300,100, width = 3)
        waagerrechte = self.spielfeld.create_line (0,200,300,200, width = 3)
        #Spielfeld Linien zeichnen + Zahlen: Anfang_x, Anfang_y, Ende_x, Ende_y
        
class SPIELEN:
    def __init__ (self, Knopf, Nummer, Breite, Höhe, Position_x, Position_y, X1, Y1, X2, Y2):
        
        self.nummer = Nummer
        self.width = Breite
        self.height = Höhe
        self.position_x = Position_x    #Position Button x
        self.position_y = Position_y    #Position Button y
    
        self.x1 = X1    #Anfang x
        self.y1 = Y1    #Anfang y
        self.x2 = X2    #Ende x
        self.y2 = Y2    #Ende y
        
        self.knopf = Button (fenster, text = Knopf, command = self.befehl)
        self.knopf.place (x = self.position_x, y = self.position_y, width = self.width, height = self.height)
        #Button erzeugen (Verweis auf befehl) und Platzieren   

    def befehl(self):   #Befehle
        if (self != Beenden and self != Neustart and SPIELFELD.sieger == 0):
            if (SPIELFELD.spieler == "x"):
                SPIELFELD.markieren_x (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "o"
                SPIELFELD.gewinner [self.nummer] = "x"
                #Auf Kreuz verweisen + Spielerwechsel + Nummer für Gewinncode
                                
            elif (SPIELFELD.spieler == "o"):
                SPIELFELD.markieren_o (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "x"
                SPIELFELD.gewinner [self.nummer] = "o"
                #Auf Kreis verweisen + Spielerwechsel + Nummer für Gewinncode

            self.knopf.lower () #Knöpfe nach anklicken verstecken
            
            if (SPIELFELD.gewinner [0] == SPIELFELD.gewinner [1] == SPIELFELD.gewinner [2] == "x" or
                SPIELFELD.gewinner [3] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [5] == "x" or
                SPIELFELD.gewinner [6] == SPIELFELD.gewinner [7] == SPIELFELD.gewinner [8] == "x" or
                SPIELFELD.gewinner [0] == SPIELFELD.gewinner [3] == SPIELFELD.gewinner [6] == "x" or
                SPIELFELD.gewinner [1] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [7] == "x" or
                SPIELFELD.gewinner [2] == SPIELFELD.gewinner [5] == SPIELFELD.gewinner [8] == "x" or
                SPIELFELD.gewinner [0] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [8] == "x" or
                SPIELFELD.gewinner [6] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [2] == "x"):

                SPIELFELD.sieger = 1
                SPIELFELD.beendet = 1
                SPIELEN.ausgang = Label (fenster, text = "X HAT GEWONNEN", fg = "red", font = "Times 15")
                SPIELEN.ausgang.place (x = 50, y = 340)
                #Gewinnmöglichkeiten + Sieger zum beenden der Runde + Label
                
            elif (SPIELFELD.gewinner [0] == SPIELFELD.gewinner [1] == SPIELFELD.gewinner [2] == "o" or
                SPIELFELD.gewinner [3] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [5] == "o" or
                SPIELFELD.gewinner [6] == SPIELFELD.gewinner [7] == SPIELFELD.gewinner [8] == "o" or
                SPIELFELD.gewinner [0] == SPIELFELD.gewinner [3] == SPIELFELD.gewinner [6] == "o" or
                SPIELFELD.gewinner [1] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [7] == "o" or
                SPIELFELD.gewinner [2] == SPIELFELD.gewinner [5] == SPIELFELD.gewinner [8] == "o" or
                SPIELFELD.gewinner [0] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [8] == "o" or
                SPIELFELD.gewinner [6] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [2] == "o"):

                SPIELFELD.sieger = 1
                SPIELFELD.beendet = 1
                SPIELEN.ausgang = Label (fenster, text = "O HAT GEWONNEN", fg = "blue", font = "Times 15")
                SPIELEN.ausgang.place (x = 50, y = 340)
                #Gewinnmöglichkeiten + Sieger zum beenden der Runde + Label

            elif (SPIELFELD.gewinner [0] and SPIELFELD.gewinner [1] and SPIELFELD.gewinner [2] and SPIELFELD.gewinner [3]
                  and SPIELFELD.gewinner [4] and SPIELFELD.gewinner [5] and SPIELFELD.gewinner [6]
                  and SPIELFELD.gewinner [7] and SPIELFELD.gewinner [8] != ""):

                SPIELFELD.beendet = 1
                SPIELEN.ausgang = Label (fenster, text = "UNENTSCHIEDEN", fg = "grey", font = "Times 15")
                SPIELEN.ausgang.place (x = 60, y = 340)
                #Unentschieden festlegen

        elif (self == Neustart):    #Spiel neustaten
            Felder = [Feld_1, Feld_2, Feld_3, Feld_4, Feld_5, Feld_6, Feld_7, Feld_8, Feld_9]
            for i in Felder:
                i.knopf.lift () #Knöpfe sichtbar machen
            SPIELFELD.neustart ()
            if (SPIELFELD.beendet == 1):
                SPIELEN.ausgang.destroy ()  #Label hat gewonnen, etc. verschwindet
            SPIELFELD.beendet = 0   #noch keiner gewonnen = Kein Label
            SPIELFELD.sieger = 0    #Sieger zurücksetzten = gibt kein Sieger
            SPIELFELD.spieler = "x" #Wieder mit x beginne
            SPIELFELD.gewinner = ["","","","","","","","",""]   #Gewinncode zurücksetzten
           
                        
        elif (self == Beenden): #Spiel beenden
            os._exit(1)

   
fenster = Tk () #Fenster erzeugen
fenster.title ("Tic-Tac-Toe")   #Name Fenster
fenster.geometry ("335x385+250+250")
          
fenster = ttk.Frame(fenster, borderwidth = 10, padding = "5")
fenster.grid () #Größe des Fensters festlegen

SPIELFELD = SPIELFELD ()    #Spielfeld aufrufen    #Fenster definieren

Anfang = Label (fenster, text = "Dies ist ein normales TIC-TAC-TOE Spiel.\n Dabei geht es darum als erster 3 Kästchen in einer Reihe zu\n haben. Es gibt drei Möglichkeiten:\n\n 1. waagerrecht\n\n 2. senkrecht\n\n 3. diagonal")
Anfang.place (x = -10, y = 100)

def fortfahren (): 
    Anfang.destroy ()
    Beginnen.destroy ()
    SPIELFELD.neustart()

    #print (SPIELFELD.beginnen)
    SPIELFELD.beginnen = 1
    #print (SPIELFELD.beginnen)
    
#print (SPIELFELD.beginnen+20)

if (SPIELFELD.beginnen == 0):
    Beginnen = Button (fenster, text = "Fortfahren", command = fortfahren)
    Beginnen.place (x = 117, y = 300, width = 75, height = 25)
    
elif (SPIELFELD.beginnen == 1):
    
    Feld_1 = SPIELEN ("Feld 1", 0, 96,96,3,2, 10,10,90,90)
    Feld_2 = SPIELEN ("Feld 2", 1, 96,96,103,2, 110,10,190,90)
    Feld_3 = SPIELEN ("Feld 3", 2, 96,96,203,2, 210,10,290,90)
    Feld_4 = SPIELEN ("Feld 4", 3, 96,96,3,102, 10,110,90,190)
    Feld_5 = SPIELEN ("Feld 5", 4, 96,96,103,102, 110,110,190,190)
    Feld_6 = SPIELEN ("Feld 6", 5, 96,96,203,102, 210,110,290,190)
    Feld_7 = SPIELEN ("Feld 7", 6, 96,96,3,202, 10,210,90,290)
    Feld_8 = SPIELEN ("Feld 8", 7, 96,96,103,202, 110,210,190,290)  
    Feld_9 = SPIELEN ("Feld 9", 8, 96,96,203,202, 210,210,290,290)

#Zahlen: Feld, Nummer, Breite, Höhe, Pos_x, Pos_y, X_Anfang, Y_Anfang, X_Ende, Y_Ende 

    Neustart = SPIELEN ("Neustart", 9, 75,25,15,310, 0,0,0,0)   #Neustart Button
    Beenden = SPIELEN ("Beenden", 10, 75,25,210,310, 0,0,0,0)   #Beenden Button

fenster.mainloop () #Hauptschleife

os._exit (1)
