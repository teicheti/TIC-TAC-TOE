import os   #os importieren (zum Beenden des Programmes)

from tkinter import *

from tkinter import ttk

import random

#---------------------------------------------------------------------

class SPIELFELD:
    def __init__ (self):

        self.spieler = "x"  #Für Spielerwechsel festlegen

        self.modus = 2
        
        self.test = 0

        self.gewonnen = 0

        self.beendet = 0
        
        self.gewinner = ["","","","","","","","",""]    #Gewinner Liste erstellen

        self.spielfeld = Canvas (fenster, width = 300, height = 400)
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
    
    def gewinncode (self, gewinner):
        if (gewinner [0] == gewinner [1] == gewinner [2] != "" or   #waagerecht oben
            gewinner [3] == gewinner [4] == gewinner [5] != "" or   #waagerecht mitte
            gewinner [6] == gewinner [7] == gewinner [8] != "" or   #waagerecht unten
            gewinner [0] == gewinner [3] == gewinner [6] != "" or   #senkrecht links
            gewinner [1] == gewinner [4] == gewinner [7] != "" or   #senkrecht mitte
            gewinner [2] == gewinner [5] == gewinner [8] != "" or   #senkrecht rechts
            gewinner [0] == gewinner [4] == gewinner [8] != "" or   #diagonal oben unten
            gewinner [6] == gewinner [4] == gewinner [2] != ""):    #diagonal unten oben
            #Gewinnmöglichkeiten

            if (SPIELFELD.test == 1):
                SPIELFELD.gewonnen = 1
            elif (SPIELFELD.test == 0):
                SPIELFELD.beendet = 1

        elif (gewinner [0] and gewinner [1] and gewinner [2]
              and gewinner [3] and gewinner [4] and gewinner [5]
              and gewinner [6] and gewinner [7] and gewinner [8] != ""):

            SPIELFELD.beendet = 2
            
#---------------------------------------------------------------------

    def kopieren (self, fortschritt):
        #Liste zum vergleich kopieren

        kopie = []

        for i in fortschritt:
            kopie.append(i)
        return kopie
    

    def platz_frei (self, status, nummer):
        return status [nummer] == ""

    def überprüfen (self, spieler):
        Felder = [Feld_1, Feld_2, Feld_3, Feld_4, Feld_5, Feld_6, Feld_7, Feld_8, Feld_9]

        for i in range(0, 9):
            kopie = self.kopieren (SPIELFELD.gewinner)
            if self.platz_frei (kopie, i):
                kopie [i] = spieler
                self.gewinncode (kopie)
                if (SPIELFELD.gewonnen == 1):
                    Feld = Felder [i]
                    SPIELFELD.markieren_x (Feld.x1, Feld.y1, Feld.x2, Feld.y2)
                    Feld.knopf.lower ()
                    SPIELFELD.gewinner [i] = "x"
                    SPIELFELD.gewonnen = 0
                    SPIELFELD.test = 0
                    SPIELFELD.überprüft = 1
                    kopie = SPIELFELD.gewinner
                    return self.gewinncode (kopie)
                else:
                    kopie = SPIELFELD.gewinner

#-------------------------------------------------        

    def computer (self):
        SPIELFELD.test = 1
        SPIELFELD.überprüft = 0
        
        #Überprüfen ob ein Gewinn möglich ist
        self.überprüfen ("x")
        

        #Überprüfen ob Spieler gewinnen kann
        self.überprüfen ("o")

        #Versuchen in eine Ecke zu setzen
        if ((SPIELFELD.gewinner [0] == "" or SPIELFELD.gewinner [2] == "" or SPIELFELD.gewinner [6] == "" or SPIELFELD.gewinner [8] == "") and SPIELFELD.überprüft == 0):
            ecke = []
            a = []
            if (SPIELFELD.gewinner [0] == ""):
                ecke.append (Feld_1)
                a.append (0)
            elif (SPIELFELD.gewinner [8] == ""):
                ecke.append (Feld_9)
                a.append (8)
            elif (SPIELFELD.gewinner [2] == ""):
                ecke.append (Feld_3)
                a.append (2)
            elif (SPIELFELD.gewinner [6] == ""):
                ecke.append (Feld_7)
                a.append (6)
            
            Feld = ecke [0]
            nummer = a [0]
            
            SPIELFELD.markieren_x (Feld.x1, Feld.y1, Feld.x2, Feld.y2)
            Feld.knopf.lower ()
            SPIELFELD.gewinner [nummer] = "x"

        #Versuchen in die Mitte zu setzen
        elif (SPIELFELD.gewinner [4] == "" and SPIELFELD.überprüft == 0):
            SPIELFELD.markieren_x (Feld_5.x1, Feld_5.y1, Feld_5.x2, Feld_5.y2)
            Feld_5.knopf.lower ()
            SPIELFELD.gewinner [4] = "x"

        #Versuchen auf eine Seite (2, 4, 6, 8) zu setzen
        elif ((SPIELFELD.gewinner [1] == "" or SPIELFELD.gewinner [3] == "" or SPIELFELD.gewinner [5] == "" or SPIELFELD.gewinner [7] == "") and SPIELFELD.überprüft == 0):
            seite = []
            a = []
            if (SPIELFELD.gewinner [1] == ""):
                seite.append (Feld_2)
                a.append (1)
            elif (SPIELFELD.gewinner [3] == ""):
                seite.append (Feld_4)
                a.append (3)
            elif (SPIELFELD.gewinner [5] == ""):
                seite.append (Feld_6)
                a.append (5)
            elif (SPIELFELD.gewinner [7] == ""):
                seite.append (Feld_8)
                a.append (7)
            
            Feld = seite [0]
            nummer = a [0]
            
            SPIELFELD.markieren_x (Feld.x1, Feld.y1, Feld.x2, Feld.y2)
            Feld.knopf.lower ()
            SPIELFELD.gewinner [nummer] = "x"

#---------------------------------------------------------------------

    def neustart (self):
        Felder = [Feld_1, Feld_2, Feld_3, Feld_4, Feld_5, Feld_6, Feld_7, Feld_8, Feld_9]
        for i in Felder:
            i.knopf.lift () #Knöpfe sichtbar machen
        SPIELFELD.neustart ()
        SPIELFELD.spieler = "x" #Wieder mit x beginnen

        if (SPIELFELD.beendet == 1 or SPIELFELD.beendet == 2):
            SPIELEN.ausgang.destroy ()  #Label hat gewonnen, etc. verschwindet
        SPIELFELD.beendet = 0
            
        SPIELFELD.gewinner = ["","","","","","","","",""]   #Gewinncode zurücksetzten

        beginner = random.randint (1, 2)
        if (SPIELFELD.modus == 1 and beginner == 1):
            SPIELFELD.markieren_x (Feld_1.x1, Feld_1.y1, Feld_1.x2, Feld_1.y2)
            Feld_1.knopf.lower ()
            SPIELFELD.gewinner [0] = "x"
            SPIELFELD.spieler = "o"
        else:
            SPIELFELD.spieler = "o"
            
#-------------------------------------------------
        
    def befehl (self):   #Befehle

        if (self == Neustart):    #Spiel neustaten
            self.neustart ()               
            
        elif (self == Beenden): #Spiel beenden
            os._exit(1)

        elif (self == Einzelspieler):
            if (SPIELFELD.modus == 2):
                SPIELFELD.modus = 1
                self.neustart ()
            
        elif (self == Mehrspieler):
            if (SPIELFELD.modus == 1):
                SPIELFELD.modus = 2
                self.neustart ()
            
#---------------------------------------------------------------------

        elif (SPIELFELD.beendet == 0):

            if (SPIELFELD.spieler == "x" and SPIELFELD.modus == 2):
                SPIELFELD.markieren_x (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "o"
                SPIELFELD.gewinner [self.nummer] = "x"
                #Auf Kreuz verweisen + Spielerwechsel + Nummer für Gewinncode
                
                self.gewinncode (SPIELFELD.gewinner)
                                    
                if (SPIELFELD.beendet == 1):
                    SPIELEN.ausgang = Label (fenster, text = "X HAT GEWONNEN", fg = "red", font = "Times 15")
                    SPIELEN.ausgang.place (x = 50, y = 375)
                    #Label für Gewinner

#---------------------------------------------------------------------
                    
            elif (SPIELFELD.spieler == "o"):
                SPIELFELD.markieren_o (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.spieler = "x"
                SPIELFELD.gewinner [self.nummer] = "o"
                wahl = self.nummer
                #Auf Kreis verweisen + Spielerwechsel + Nummer für Gewinncode

                self.gewinncode (SPIELFELD.gewinner)

           
                if (SPIELFELD.modus == 1):
                    self.computer ()      
                    SPIELFELD.spieler = "o" #Anderer Spieler
                    SPIELFELD.test = 0  
                    self.gewinncode (SPIELFELD.gewinner)    #Überprüfen ob gewonnen
                    
                    
                if (SPIELFELD.beendet == 1):
                    if (SPIELFELD.modus == 1):
                        SPIELEN.ausgang = Label (fenster, text = "X HAT GEWONNEN", fg = "red", font = "Times 15")
                    else:
                        SPIELEN.ausgang = Label (fenster, text = "O HAT GEWONNEN", fg = "blue", font = "Times 15")
                    SPIELEN.ausgang.place (x = 50, y = 375)
                    #Label für Gewinner
                    
            self.knopf.lower () #Knöpfe nach anklicken verstecken

            if (SPIELFELD.beendet == 2):
                SPIELEN.ausgang = Label (fenster, text = "UNENTSCHIEDEN", fg = "grey", font = "Times 15")
                SPIELEN.ausgang.place (x = 60, y = 375)
                #Unentschieden festlegen

#---------------------------------------------------------------------

def anleitung ():
    anfang = Tk ()
    anfang.title ("Anleitung TIC-TAC-TOE")
    anfang.geometry ("400x200+217+275")

    beschreibung = Label (anfang, text = "Dies ist ein normeles TIC-TAC-TOE Spiel.\n Dabei geht es darum, als erster Drei Symbole in einer\n Reihe zu haben. Es gibt dabei drei Möglichkeiten:\n\n 1: waagerrecht\n\n 2: senkrecht\n\n 3: diagolal")
    beschreibung.pack ()

    starten = Button (anfang, text = "Schließen", command = anfang.destroy)
    starten.pack (side = TOP, pady = 10)

    anfang.mainloop ()

#---------------------------------------------------------------------

fenster = Tk () #Fenster erzeugen
fenster.title ("Tic-Tac-Toe")   #Name Fenster
fenster.geometry ("335x420+250+250")

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
Beenden = SPIELEN ("Beenden", 10, 75,25,210,310, 0,0,0,0)   #Beenden Button

Anleitung = Button (fenster, text = "Anleitung", command = anleitung)
Anleitung.place (x = 112, y = 310, width = 75, height = 25)

Einzelspieler = SPIELEN ("Einzelspieler", 11, 75,25,55,345, 0,0,0,0)
Mehrspieler = SPIELEN ("Mehrspieler", 12, 75,25,160,345, 0,0,0,0)

fenster.mainloop () #Hauptschleife

#---------------------------------------------------------------------

os._exit (1)
