# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Held-Klasse
# Autor: Viktor Lysow
# Letzte Änderung: 30.03.2022
# Zweck: Held-Entität definieren
# 
# Held erbt Alles von Figur
# Held kann stehen und nicht laufen
# Held wird mit Steuerkreuz/Pfeiltasten gesteuert
# Held kann mit Leerzeichen in seine Guckrichtung schießen


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
from screen import screen
from KlasseFigur import Figur
from KlasseMagie import Magie



class Held(Figur):
    def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur):
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur)
        self.bildOben.append(pygame.image.load(f"Bilder/{bildFigur}/HintenS.png"))
        self.bildUnten.append(pygame.image.load(f"Bilder/{bildFigur}/VornS.png"))
        self.bildRechts.append(pygame.image.load(f"Bilder/{bildFigur}/RechtsS.png"))
        self.bildLinks.append(pygame.image.load(f"Bilder/{bildFigur}/LinksS.png"))
        self.bildtot = pygame.image.load(f"Bilder/{bildFigur}/tot.png")
        self.stehRicht = 0
        self.spaceHalten = False

    def stehen(self):                                                                           #Nur der Held kann stehen
        if self.stehRicht == 0:
            screen.blit(self.bildOben[2], (self.x, self.y))
        if self.stehRicht == 1:
            screen.blit(self.bildUnten[2], (self.x, self.y))
        if self.stehRicht == 2:
            screen.blit(self.bildRechts[2], (self.x, self.y))
        if self.stehRicht == 3:
            screen.blit(self.bildLinks[2], (self.x, self.y))

    def steuerung(self):
        self.gedrueckt = pygame.key.get_pressed()

        if self.gedrueckt[pygame.K_UP]:
            self.laufen(0)
            self.stehRicht = 0
        elif self.gedrueckt[pygame.K_DOWN]:
            self.laufen(1)
            self.stehRicht = 1
        elif self.gedrueckt[pygame.K_RIGHT]:
            self.laufen(2)
            self.stehRicht = 2
        elif self.gedrueckt[pygame.K_LEFT]:
            self.laufen(3)
            self.stehRicht = 3
        else:
            self.stehen()

        self.schuss()

    def schuss(self):
        if self.gedrueckt[pygame.K_SPACE] and self.spaceHalten and len(self.kugeln) <= 3:       # Leerzeichen wird nur pro Tastenschlag gezählt und es dürfen nicht mehr als 4 Magiekugeln existieren

            self.kugeln.append(Magie(self.x, self.y, self.stehRicht, "B", 5))                   #Magie wird erschaffen

            self.schussZaehler += 1

            self.spaceHalten = False

        if not self.gedrueckt[pygame.K_SPACE]:                                                  #Leerzeichen wird losgelassen
            self.spaceHalten = True

        for k in self.kugeln:                                                                   #Alle Magiekugeln werden in Bewegung gebracht und Kollision von Hindernissen vernichtet
            if not self.hindernis(k.kugelRec):
                self.kugeln.remove(k)
            k.bewegung()


    def neu_Position(self,x_neu, y_neu, level_neu):
        self.x = x_neu
        self.y = y_neu

        self.rechteck = pygame.Rect(self.x, self.y, self.breite, self.hoehe)                # Aktualisierung der Rechtecke
        self.obenKollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y, 4, 4)
        self.untenKollision = pygame.Rect(self.x + self.breite / 2 - 2, self.y + self.hoehe - 4, 4, 4)
        self.rechtsKollision = pygame.Rect(self.x + self.breite - 2, self.y + self.hoehe / 2 - 2, 4, 4)
        self.linksKollision = pygame.Rect(self.x, self.y + self.hoehe / 2 - 2, 4, 4)

        self.kugeln = []
        self.level = level_neu