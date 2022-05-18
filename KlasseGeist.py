# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Geist-Klasse
# Autor: Viktor Lysow
# Letzte Änderung: 30.03.2022
# Zweck: Geist-Entität definieren
#
# Geist erbt alles von Monster
# können den Held bei Berührung töten
# Geist kann neue Monster erschaffen, die wie Geister aussehen

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
from KlasseMonster import Monster
from time import time
from random import randint

class Geist (Monster):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)
        self.MonsterDupl = Monster                                                            #Welche Klasse erschaffen wird
        self.dupliList = []                                                                     #Liste der erschaffenen Monster
        self.zeitDupl = zeitMonster
        self.anzahlDouble = 1

        self.zeitUnsicht = zeitMonster
        self.bildUnsicht = [pygame.image.load("Bilder/Geist/tot.png"),
                         pygame.image.load("Bilder/Geist/tot.png")]
        self.saveBildOben = self.bildOben
        self.saveBildUnten = self.bildUnten
        self.saveBildRechts = self.bildRechts
        self.saveBildLinks = self.bildLinks

        self.zeitSpring = zeitMonster

    def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.leben = True
        self.heldTot = False
        self.anzahlDouble = 1
        self.dupliList = []


    def faehigkeit(self):                        #Fähigkeiten von Monstern werden mit den Fähigkeiten der Klasse überschrieben!!!
        self.toeten()
        self.duplizieren()


    #Alle Fähigkeiten der Klasse Geist

    def duplizieren(self):
        for dupli in self.dupliList:                                                            #Alle erschaffenen Monster in Bewegung bringen
           if dupli.mlaufen(self.heldDaten):                                                    #Prüfen ob ein erschaffenes Monster den Held getötet hat
                self.heldTot = True

        if time() - self.zeitDupl >= 0.5 * self.anzahlDouble:                                   #Zeit zur Duplezierung wird jedes mal erhöht
            self.dupliList.append(self.MonsterDupl(x = self.x, y = self.y, geschw = self.geschw, breite = self.breite, hoehe = self.hoehe, level = self.level, bildFigur = self.bildFigur, zeitMonster = time())) #Monster wird erschaffen und in die Liste eingefügt
            self.zeitDupl = time()                                                                                                            #Zeit wird wieder auf Null gesetzt
            self.anzahlDouble += 1

