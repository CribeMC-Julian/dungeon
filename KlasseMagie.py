# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Magie-Klasse
# Autor: Viktor Lysow
# Letzte Änderung: 18.04.2022
# Zweck: Magie ist das, mit dem der Held schießt (blau) oder der Boss schießt (rosa). Magie fliegt herum.


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
from time import time
from KlasseLevelmanagement import LevelManagement
import sounds

class Magie:
    def __init__(self, x, y, richtung, farbe, geschw):
        sounds.soundMagie()                                                             #Sound beim Erschaffen von Magie
        self.x = x
        self.y = y
        self.farbe = farbe
        self.richtung = richtung
        self.zeit = time()
        self.geschw = geschw
        # falls das Spiel bei Ihnen zu langsam / zu schnell läuft, ändern Sie die nachfolgende Zeile:
        self.geschw_FPS_trick = self.geschw * (30 / LevelManagement.fpsTarget) # hier mit der "30" experimentieren, falls nötig
        self.kugelRec = pygame.Rect(self.x + 12 , self.y +12, 24, 24)
        self.bildbewegung = 2
        self.bildMagie = [pygame.image.load(f"Bilder/Magie/{farbe}1.png"),
                          pygame.image.load(f"Bilder/Magie/{farbe}2.png"),
                          pygame.image.load(f"Bilder/Magie/{farbe}3.png"),
                          pygame.image.load(f"Bilder/Magie/{farbe}2.png")]

        if self.richtung == 0:              #oben
            self.y -= self.geschw_FPS_trick

        elif self.richtung == 1:            #unten
            self.y += self.geschw_FPS_trick

        elif self.richtung == 2:            #rechts
             self.x += self.geschw_FPS_trick

        elif self.richtung == 3:            #links
            self.x -= self.geschw_FPS_trick


        elif self.richtung == 4:            #oben links   Bonus!!!!
            self.y -= self.geschw_FPS_trick
            self.x -= self.geschw_FPS_trick

        elif self.richtung == 5:            #oben rechts   Bonus!!!!
            self.y -= self.geschw_FPS_trick
            self.x += self.geschw_FPS_trick

        elif self.richtung == 6:            # unten links   Bonus!!!!
            self.y += self.geschw_FPS_trick
            self.x -= self.geschw_FPS_trick

        elif self.richtung == 7:            #unten rechts   Bonus!!!!
            self.y += self.geschw_FPS_trick
            self.x += self.geschw_FPS_trick

    def bewegung(self):
        if self.richtung == 0:          #oben
            self.y -= self.geschw_FPS_trick

        elif self.richtung == 1:        #unten
            self.y += self.geschw_FPS_trick

        elif self.richtung == 2:        #rechts
            self.x += self.geschw_FPS_trick

        elif self.richtung == 3:        #links
            self.x -= self.geschw_FPS_trick



        elif self.richtung == 4:        #oben links   Bonus!!!!
            self.y -= self.geschw_FPS_trick
            self.x -= self.geschw_FPS_trick

        elif self.richtung == 5:        #oben rechts   Bonus!!!!
            self.y -= self.geschw_FPS_trick
            self.x += self.geschw_FPS_trick

        elif self.richtung == 6:        #unten links   Bonus!!!!
            self.y += self.geschw_FPS_trick
            self.x -= self.geschw_FPS_trick

        elif self.richtung == 7:        #unten rechts   Bonus!!!!
            self.y += self.geschw_FPS_trick
            self.x += self.geschw_FPS_trick

        self.zeichnen()

    def zeichnen(self):                         # Bilder werden alle 0.1 Sekunden ausgetauscht
        if time() - self.zeit >= 0.1:
            self.zeit = time()
            self.bildbewegung += 1
            if self.bildbewegung >= 3:
                self.bildbewegung = 0

        screen.blit(self.bildMagie[self.bildbewegung], (self.x, self.y))
        self.kugelRec = pygame.Rect(self.x + 12, self.y + 12, 24, 24)          #Kugel ist halb so groß wie das Bild