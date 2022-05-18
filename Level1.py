# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Level1
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 22.04.2022
# Zweck: Organisation und Steuerung des ersten Levels

# Der Nachfolgende Codeblock "BLOCK1" sorgt dafür, dass man aus jeder Datei heraus das Hauptprogramm starten kann.
# Dadurch kann man in jeder Datei auf "play" drücken und es wird automatisch main.py gestartet.
if __name__=="__main__":
    import subprocess
    # Auf Linux oder Mac aktivieren Sie die folgende Zeile und deaktivieren Sie die Zeile danach:
    #subprocess.call("python3 main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    subprocess.call("main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    exit(0) # nun das Programm hier beenden .. wir wollen ja nur das Hauptprogramm starten und nicht *diese* Datei.
# Ende "BLOCK1"

from KlasseLevelmanagement import LevelManagement
import pygame
import sounds
import DatenSammeln as ds                           # Für den Matlab Beleg
from screen import screen
from hindernisse import feld
from time import time
from KlasseGeist import Geist

zeitStart = True
zeit = 0

LevelManagement.Level = 1
hintergrundLevel1 = pygame.image.load("Bilder/Karte/Level1.png")
tor = pygame.Rect(3*feld,0,48,48)                                      #Ziel in Level 1

monster = Geist(x = 100, y = 200, geschw= 3, breite = feld, hoehe = feld, level = LevelManagement.Level,bildFigur= "Geist",zeitMonster= time())
# display text
pygame.font.init() # you have to call this at the start, if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def Level1(spieler):
    global zeitStart, zeit
    screen.blit(hintergrundLevel1, (0, 0))

    # Tor anzeigen
    #pygame.draw.rect(screen, (255,0,0), (3*feld,0,48,48),0) 

    if LevelManagement.numFrames >= LevelManagement.fpsTarget:
        LevelManagement.fpsCurrent = (LevelManagement.timeNeeded / LevelManagement.numFrames)
        LevelManagement.numFrames = 0
        LevelManagement.timeNeeded = 0
    textsurface = myfont.render("%i fps" % (1000/LevelManagement.fpsCurrent), False, (255, 255, 0))
    screen.blit(textsurface,(10,0))	


    if zeitStart:                                                     #Zeit wird ab den ersten aufruf gemäßen (für Matlab)
        zeitStart = False
        LevelManagement.Level = 1
        zeit = time()

    if monster.mlaufen(spieler):           #mit mlaufen läuft der Geist und es wird überprüft, ob der Held getötet wurde
        pygame.display.update()
        pygame.time.wait(1000)
        gameOver = 3
        monster.reset()                                               #Es wird Alles für den Geist zurück gesetzt
        ds.daten_csv(8,round(time() - zeit))                          #Zeit für Level1 (für Matlab)
        ds.daten_csv(11,LevelManagement.Level)
        zeitStart = True
        return gameOver

    if spieler.obenKollision.colliderect(tor):                        #Held muss mit dem Kopf den Eingang berühren
        LevelManagement.Level += 1
        spieler.neu_Position(582, 476, LevelManagement.Level)                         #Neue Position für das nächste Level
        sounds.soundTor()
        pygame.time.wait(500)
        monster.reset()                                                #Es wird Alles für den Geist zurück gesetzt
        ds.daten_csv(8, round(time() - zeit))                          #Zeit für Level1 (für Matlab)
        zeitStart = True
        return LevelManagement.Level 
    else:                                                              #Das Level läuft weiter
        spieler.steuerung()
        return LevelManagement.Level



