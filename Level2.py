# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Level2
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 22.04.2022
# Zweck: Organisation und Steuerung des zweiten Levels
 
 
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
from screen import screen
from hindernisse import feld
from time import time
from KlassePrinzessin import Prinzessin
from KlasseHarpyie import Harpyie
import DatenSammeln as ds                                                          # Für den Matlab Beleg

zeitStart = True
zeit = 0

hintergrundLevel = pygame.image.load("Bilder/Karte/Level2.png")
tor = pygame.Rect(3*feld,0,48,48)                                      #Ziel in Level 2
LevelManagement.Level = 2
prinzessin = Prinzessin(x = feld*10, y = feld*3, geschw = 1, breite = feld, hoehe = feld, level = LevelManagement.Level, bildFigur = "Prinzessin", zeitMonster= time())
monster1 = Harpyie( feld*9, feld*2,  1,  feld,  feld, LevelManagement.Level, "Harpyie",  time())

# display text
pygame.font.init() # you have to call this at the start, if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)


def Level2(spieler):
    global zeitStart, zeit
    screen.blit(hintergrundLevel, (0, 0))

    # Tor anzeigen
    #pygame.draw.rect(screen, (255,0,0), (3*feld,0,48,48),0) 

    if LevelManagement.numFrames >= LevelManagement.fpsTarget:
        LevelManagement.fpsCurrent = LevelManagement.timeNeeded / LevelManagement.numFrames
        LevelManagement.numFrames = 0
        LevelManagement.timeNeeded = 0
    textsurface = myfont.render("%i fps" % (1000/LevelManagement.fpsCurrent), False, (255, 255, 0))
    screen.blit(textsurface,(10,0))	

    #drawLevel2()

    if zeitStart:                                                                 #Zeit wird ab den ersten aufruf gemäßen (für Matlab)
        zeitStart = False
        LevelManagement.Level = 2
        zeit = time()
    
    
    if prinzessin.mlaufen(spieler, monster1) or monster1.mlaufen(spieler):          #mit mlaufen läuft die Harpyie und es wird überprüft ob der Held getötet wurde
        pygame.display.update()                                                   #mit mlaufen läuft die Prinzessin und es wird überprüft ob die Prinzessin getötet wurde
        pygame.time.wait(1000)
        monster1.reset()                                                           #Es wird Alles für die Harpyie zurück gesetzt
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        LevelManagement.Level = 3
        ds.daten_csv(9, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        ds.daten_csv(11, LevelManagement.Level)
        zeitStart = True
        return LevelManagement.Level
    
    if monster1.leben and spieler.obenKollision.colliderect(tor):                                    #Held muss mit dem Kopf den Eingang berühren
        sounds.soundTor()
        pygame.time.wait(500)
        monster1.reset()                                                           #Es wird Alles für die Harpyie zurück gesetzt
        prinzessin.reset()                                                        #Es wird Alles für die Prinzessin zurück gesetzt
        LevelManagement.Level = 3
        ds.daten_csv(9, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        zeitStart = True
        return LevelManagement.Level
    elif spieler.obenKollision.colliderect(tor) and not monster1.leben:                  
        sounds.soundTor()
        pygame.time.wait(500)
        monster1.reset()                                                           
        prinzessin.reset()                                                       
        LevelManagement.Level = 4
        ds.daten_csv(9, round(time() - zeit))                                     #Zeit für Level3 (für Matlab)
        zeitStart = True
        return LevelManagement.Level
    else:                                                               
        spieler.steuerung()        
        return LevelManagement.Level