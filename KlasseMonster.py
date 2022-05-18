# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Monster-Klasse
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 30.03.2022
# Zweck: Definition der Monster
#
# Monster erbt Alles von Figur
# Monster können selbst laufen
# Sterben, wenn sie mit der Magie des Helden in Berührung kommen
# können den Helden bei Berührung töten

# Der Nachfolgende Codeblock "BLOCK1" sorgt dafür, dass man aus jeder Datei heraus das Hauptprogramm starten kann.
# Dadurch kann man in jeder Datei auf "play" drücken und es wird automatisch main.py gestartet.
if __name__=="__main__":
    import subprocess
    # Auf Linux oder Mac aktivieren Sie die folgende Zeile und deaktivieren Sie die Zeile danach:
    #subprocess.call("python3 main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    subprocess.call("main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    exit(0) # nun das Programm hier beenden .. wir wollen ja nur das Hauptprogramm starten und nicht *diese* Datei.
# Ende "BLOCK1"

import pygame
from random import randint
from time import time
from KlasseFigur import Figur
from screen import screen
import sounds


class Monster(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur)
        self.xReset = x
        self.yReset = y
        self.richtung = 1
        self.zeitMonster = zeitMonster
        self.leben = True
        self.heldTot = False
        self.feuerWechsel = 0
        self.heldDaten = None
        self.monsterDaten = None

        self.bildTot = [pygame.image.load(f"Bilder/Feuer/F1.png"),
                         pygame.image.load(f"Bilder/Feuer/F2.png"),
                         pygame.image.load(f"Bilder/Feuer/F3.png")]

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.leben = True
        self.heldTot = False

    def mlaufen(self, spieler , monster = None):                                   #Monster können selber laufen
        if self.leben:
            self.heldDaten = spieler                                               #Alle Daten vom Held werden hier gespeichert
            self.monsterDaten = monster                                            #Alle Daten von einem Monster werden hier gespeichert
            if time() - self.zeitMonster >= 1:                                     #abhängig von der Zeit
                self.richtung = randint(0, 3)                                      #Zufallsrichtung
                self.zeitMonster = time()
            self.laufen(self.richtung)                                             #Laufen in eine Richtung
            self.sterben()
            self.faehigkeit()
            return self.heldTot                                                     #Rückgabe ob der Held tot ist

        else:
            screen.blit(self.bildTot[self.feuerWechsel], (self.x, self.y))          #Monster brennen, wenn sie tot sind
            if time() - self.zeitMonster >= 0.15:
                if self.feuerWechsel < 2:
                    self.feuerWechsel += 1
                else:
                    self.feuerWechsel = 0
                self.zeitMonster = time()

    def toeten(self):                                                               #Held wird getötet bei Kollision
        if self.rechteck.colliderect(self.heldDaten.rechteck):
            sounds.soundTot()
            screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
            self.heldTot = True

    def sterben(self):                                                             # Monster ist tot nach der Berührung von der Magie des Helden
        for slide in self.heldDaten.kugeln:
            if self.rechteck.colliderect(slide.kugelRec):
                self.heldDaten.kugeln.remove(slide)
                self.leben = False
                sounds.soundFeuer()

    def faehigkeit(self):                                                            #Alle Fähigkeiten von Monster kommen hier rein
        self.toeten()