import os   #os importieren (zum Beenden des Programmes)

from tkinter import *

from tkinter import ttk

import random

#---------------------------------------------------------------------

class SPIELFELD:
    def __init__ (self):

        self.spieler = "x"  #Für Spielerwechsel festlegen

        self.gewonnen = 0

        self.beendet = 0
        
        self.gewinner = ["","","","","","","","",""]    #Gewinner Liste erstellen

        self.spielfeld = Canvas (fenster, width = 300, height = 350)
        self.spielfeld.pack ()  #Canvas Größe festlegen (Bezug auf fenster)
        
        self.neustart()
                   
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

#--------------------------------------------------------------------
        
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

        if (modus == 1 and felder_erstellt == 1):   
            SPIELFELD.markieren_x (Feld_1.x1, Feld_1.y1, Feld_1.x2, Feld_1.y2)
            Feld_1.knopf.lower ()
            SPIELFELD.spieler = "o"
            SPIELFELD.gewinner [0] = "x"
            
    
    def gewinncode (self):
        if (SPIELFELD.gewinner [0] == SPIELFELD.gewinner [1] == SPIELFELD.gewinner [2] != "" or
            SPIELFELD.gewinner [3] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [5] != "" or
            SPIELFELD.gewinner [6] == SPIELFELD.gewinner [7] == SPIELFELD.gewinner [8] != "" or
            SPIELFELD.gewinner [0] == SPIELFELD.gewinner [3] == SPIELFELD.gewinner [6] != "" or
            SPIELFELD.gewinner [1] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [7] != "" or
            SPIELFELD.gewinner [2] == SPIELFELD.gewinner [5] == SPIELFELD.gewinner [8] != "" or
            SPIELFELD.gewinner [0] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [8] != "" or
            SPIELFELD.gewinner [6] == SPIELFELD.gewinner [4] == SPIELFELD.gewinner [2] != ""):
            #Gewinnmöglichkeiten

            if (test == 1):
                SPIELFELD.gewonnen = 1
            elif (test == 0):
                SPIELFELD.beendet = 1

        elif (SPIELFELD.gewinner [0] and SPIELFELD.gewinner [1] and SPIELFELD.gewinner [2] and SPIELFELD.gewinner [3]
            and SPIELFELD.gewinner [4] and SPIELFELD.gewinner [5] and SPIELFELD.gewinner [6]
            and SPIELFELD.gewinner [7] and SPIELFELD.gewinner [8] != ""):

            SPIELFELD.beendet = 2
            SPIELEN.ausgang = Label (fenster, text = "UNENTSCHIEDEN", fg = "grey", font = "Times 15")
            SPIELEN.ausgang.place (x = 60, y = 340)
            #Unentschieden festlegen

#---------------------------------------------------------------------

    def befehl (self):   #Befehle
        if (self != Beenden and self != Neustart and SPIELFELD.beendet == 0):

            if (SPIELFELD.spieler == "x" and modus == 2):
                SPIELFELD.markieren_x (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "o"
                SPIELFELD.gewinner [self.nummer] = "x"
                #Auf Kreuz verweisen + Spielerwechsel + Nummer für Gewinncode
                
                self.gewinncode ()
                                    
                if (SPIELFELD.beendet == 1):
                    SPIELEN.ausgang = Label (fenster, text = "X HAT GEWONNEN", fg = "red", font = "Times 15")
                    SPIELEN.ausgang.place (x = 50, y = 340)
                    #Label für Gewinner

#---------------------------------------------------------------------
                    
            elif (SPIELFELD.spieler == "o"):
                SPIELFELD.markieren_o (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "x"
                SPIELFELD.gewinner [self.nummer] = "o"
                wahl = self.nummer
                #Auf Kreis verweisen + Spielerwechsel + Nummer für Gewinncode

                self.gewinncode ()

#---------------------------------------------------------------------
                
                if (modus == 1):
                    SPIELFELD.gesetzt = 0
                    self.computer ()
                        
#---------------------------------------------------------------------
                            
                    self.gewinncode ()
                    
                if (SPIELFELD.beendet == 1):
                    if (modus == 1):
                        SPIELEN.ausgang = Label (fenster, text = "X HAT GEWONNEN", fg = "red", font = "Times 15")
                    else:
                        SPIELEN.ausgang = Label (fenster, text = "O HAT GEWONNEN", fg = "blue", font = "Times 15")
                    SPIELEN.ausgang.place (x = 50, y = 340)
                    #Label für Gewinner
                    
            self.knopf.lower () #Knöpfe nach anklicken verstecken

#---------------------------------------------------------------------
            
        elif (self == Neustart):    #Spiel neustaten
            Felder = [Feld_1, Feld_2, Feld_3, Feld_4, Feld_5, Feld_6, Feld_7, Feld_8, Feld_9]
            for i in Felder:
                i.knopf.lift () #Knöpfe sichtbar machen
            SPIELFELD.neustart ()
            if (SPIELFELD.beendet == 1 or SPIELFELD.beendet == 2):
                SPIELEN.ausgang.destroy ()  #Label hat gewonnen, etc. verschwindet
            SPIELFELD.beendet = 0
            SPIELFELD.spieler = "x" #Wieder mit x beginne
            SPIELFELD.gewinner = ["","","","","","","","",""]   #Gewinncode zurücksetzten

            if (modus == 1 and felder_erstellt == 1):
                SPIELFELD.markieren_x (Feld_1.x1, Feld_1.y1, Feld_1.x2, Feld_1.y2)
                Feld_1.knopf.lower ()
                SPIELFELD.spieler = "o"
                SPIELFELD.gewinner [0] = "x"
                SPIELFELD.schritt = 1
            
        elif (self == Beenden): #Spiel beenden
            os._exit(1)

#---------------------------------------------------------------------

fehler = 1

anfang = Tk ()
anfang.title ("Anleitung TIC-TAC-TOE")
anfang.geometry ("400x200+217+275")

beschreibung = Label (anfang, text = "Dies ist ein normeles TIC-TAC-TOE Spiel.\n Dabei geht es darum, als erster Drei Symbole in einer\n Reihe zu haben. Es gibt dabei drei Möglichkeiten:\n\n 1: waagerrecht\n\n 2: senkrecht\n\n 3: diagolal")
beschreibung.pack ()

def Einzelspieler ():
    global modus
    modus = 1
    global fehler
    fehler = 0
    anfang.destroy ()
    
def Mehrspieler ():
    global modus
    modus = 2
    global fehler
    fehler = 0
    anfang.destroy ()
    
einzelspieler = Button (anfang, text = "1 Spieler", command = Einzelspieler)
einzelspieler.place (x = 120, y = 160, width = 75, height = 25)

mehrspieler = Button (anfang, text = "2 Spieler", command = Mehrspieler)
mehrspieler.place (x = 210, y = 160, width = 75, height = 25)

anfang.mainloop ()

if (fehler == 1):
    os._exit (1)

#---------------------------------------------------------------------
global felder_erstellt
felder_erstellt = 0

global test
test = 0

fenster = Tk () #Fenster erzeugen
fenster.title ("Tic-Tac-Toe")   #Name Fenster
fenster.geometry ("335x385+250+250")

fenster = ttk.Frame (fenster, borderwidth = 10, padding = "5")
fenster.grid () #Größe des Fensters festlegen

SPIELFELD = SPIELFELD ()    #Spielfeld aufrufen    #Fenster definieren   

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

felder_erstellt = 1

Beenden = SPIELEN ("Beenden", 10, 75,25,210,310, 0,0,0,0)   #Beenden Button

fenster.mainloop () #Hauptschleife

#---------------------------------------------------------------------

#os._exit (1)
