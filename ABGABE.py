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
        senkrechte = self.spielfeld.create_line (100,0,100,300, width = 4)  
        senkrechte = self.spielfeld.create_line (200,0,200,300, width = 4)  
        waagerrechte = self.spielfeld.create_line (0,100,300,100, width = 4)
        waagerrechte = self.spielfeld.create_line (0,200,300,200, width = 4)
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
                kopie [i] = spieler     #Überprüft, ob auf einem der Felder ein Sieg möglich ist
                self.gewinncode (kopie)
                if (SPIELFELD.gewonnen == 1):   #Wenn Sieg mölich ist führt er aus
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

    def computer (self):    #Block ist für das setzen vom Computer zuständig
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
        SPIELFELD.neustart ()   #Neues Spielfeld erzeugen
        #SPIELFELD.spieler = "x" #Wieder mit x beginnen

        if (SPIELFELD.beendet == 1 or SPIELFELD.beendet == 2):
            SPIELEN.ausgang.destroy ()  #Label hat gewonnen, etc. verschwindet
        SPIELFELD.beendet = 0
            
        SPIELFELD.gewinner = ["","","","","","","","",""]   #Gewinncode zurücksetzten

        global beginner
        #Per Zufall beginner auswählen
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

        elif (self == Einzelspieler):   #Zu Einzelspieler wechseln
            SPIELFELD.modus = 1
            Einzelspieler.knopf.lower ()
            Mehrspieler.knopf.lift ()
            Einzelspieler_modus.lift ()
            Mehrspieler_modus.lower ()
            self.neustart ()
            
        elif (self == Mehrspieler):     #Zu Mehrspieler wechseln
            SPIELFELD.modus = 2
            Mehrspieler.knopf.lower ()
            Einzelspieler.knopf.lift ()
            Mehrspieler_modus.lift ()
            Einzelspieler_modus.lower ()
            SPIELFELD.spieler = "x"
            self.neustart ()
                
            
#---------------------------------------------------------------------

        elif (SPIELFELD.beendet == 0):

            if (SPIELFELD.spieler == "x" and SPIELFELD.modus == 2):
                SPIELFELD.markieren_x (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.gewinner [self.nummer] = "x"
                self.gewinncode (SPIELFELD.gewinner)
                SPIELFELD.spieler = "o"
                if (SPIELFELD.beendet == 1):
                    SPIELFELD.spieler = "x"
                #Auf Kreuz verweisen + Spielerwechsel + Nummer für Gewinncode
                
                
                                    
#---------------------------------------------------------------------
                    
            elif (SPIELFELD.spieler == "o"):
                SPIELFELD.markieren_o (self.x1, self.y1, self.x2, self.y2)
                SPIELFELD.gewinner [self.nummer] = "o"
                self.gewinncode (SPIELFELD.gewinner)
                SPIELFELD.spieler = "x"
                if (SPIELFELD.beendet == 1):
                    SPIELFELD.spieler = "o"
                #Auf Kreis verweisen + Spielerwechsel + Nummer für Gewinncode    
           
                if (SPIELFELD.modus == 1 and SPIELFELD.beendet == 0):
                    self.computer ()      
                    SPIELFELD.test = 0  
                    self.gewinncode (SPIELFELD.gewinner)    #Überprüfen ob gewonnen
                    if (SPIELFELD.beendet != 1 and SPIELFELD.beendet != 2):
                        SPIELFELD.spieler = "o" #Anderer Spieler     
                    
            self.knopf.lower () #Knöpfe nach anklicken verstecken

            if (SPIELFELD.beendet == 1):
                if (SPIELFELD.spieler == "x"):
                    SPIELEN.ausgang = Label (fenster, text = "X HAT GEWONNEN", fg = "red", font = "Times 15")
                    SPIELEN.ausgang.place (x = 50, y = 375)
                elif (SPIELFELD.spieler == "o"):
                    SPIELEN.ausgang = Label (fenster, text = "O HAT GEWONNEN", fg = "blue", font = "Times 15")
                    SPIELEN.ausgang.place (x = 50, y = 375)
                #Label für Gewinner

            elif (SPIELFELD.beendet == 2):
                SPIELEN.ausgang = Label (fenster, text = "UNENTSCHIEDEN", fg = "grey", font = "Times 15")
                SPIELEN.ausgang.place (x = 60, y = 375)
                #Unentschieden festlegen

#---------------------------------------------------------------------

def anleitung ():
    anfang = Tk ()
    anfang.title ("Anleitung TIC-TAC-TOE")
    anfang.geometry ("400x240+217+275")

    beschreibung = Label (anfang, text = "Dies ist ein normeles TIC-TAC-TOE Spiel.\nDabei geht es darum, als erster Drei Symbole in einer\n Reihe zu haben.\n Dabei stehen folgende drei Möglichkeiten zur Wahl:\n\n 1: waagerrecht\n\n 2: senkrecht\n\n 3: diagolal\n\n (Im Einzelspielermodus wird per zufall bestimmt wer beginnen darf.)")
    beschreibung.pack ()

    starten = Button (anfang, text = "ZURÜCK", command = anfang.destroy)
    starten.pack (side = TOP, pady = 10)

    anfang.mainloop ()

#---------------------------------------------------------------------

fenster = Tk () #Fenster erzeugen
fenster.title ("TIC-TAC-TOE")   #Name Fenster
fenster.geometry ("335x420+250+250")

fenster = ttk.Frame (fenster, borderwidth = 10, padding = "5")
fenster.grid () #Größe des Fensters festlegen

SPIELFELD = SPIELFELD ()    #Spielfeld aufrufen    #Fenster definieren   

Feld_1 = SPIELEN ("", 0, 96,96,3,2, 10,10,90,90)
Feld_2 = SPIELEN ("", 1, 96,96,103,2, 110,10,190,90)
Feld_3 = SPIELEN ("", 2, 96,96,203,2, 210,10,290,90)
Feld_4 = SPIELEN ("", 3, 96,96,3,102, 10,110,90,190)
Feld_5 = SPIELEN ("", 4, 96,96,103,102, 110,110,190,190)
Feld_6 = SPIELEN ("", 5, 96,96,203,102, 210,110,290,190)
Feld_7 = SPIELEN ("", 6, 96,96,3,202, 10,210,90,290)
Feld_8 = SPIELEN ("", 7, 96,96,103,202, 110,210,190,290)
Feld_9 = SPIELEN ("", 8, 96,96,203,202, 210,210,290,290)

#Zahlen: Feld, Nummer, Breite, Höhe, Pos_x, Pos_y, X_Anfang, Y_Anfang, X_Ende, Y_Ende 

Neustart = SPIELEN ("NEUSTART", 9, 75,25,15,310, 0,0,0,0)   #Neustart Button
Beenden = SPIELEN ("BEENDEN", 10, 75,25,210,310, 0,0,0,0)   #Beenden Button

Anleitung = Button (fenster, text = "ANLEITUNG", command = anleitung)
Anleitung.place (x = 112, y = 310, width = 75, height = 25)

Einzelspieler = SPIELEN ("EINZELSPIELER", 11, 100,25,197,345, 0,0,0,0)
Mehrspieler = SPIELEN ("MEHRSPIELER", 12, 100,25,197,345, 0,0,0,0)

Einzelspieler_modus = Label (fenster, text = "MODUS: EINZELSPIELER", font = "Times 12")
Einzelspieler_modus.place (x = 15, y = 347)
Mehrspieler_modus = Label (fenster, text = "MODUS: MEHRSPIELER", font = "Times 12")
Mehrspieler_modus.place (x = 15, y = 347)
#Label für Modus
Mehrspieler.knopf.lower ()
Einzelspieler_modus.lower ()

fenster.mainloop () #Hauptschleife

#---------------------------------------------------------------------

os._exit (1)    #Wenn Fenster geschlossen wird komplett beenden
