# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Game Over
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 22.04.2022
# Zweck: Festlegung was passieren soll, wenn das Spiel verloren wurde

# Der Nachfolgende Codeblock "BLOCK1" sorgt dafür, dass man aus jeder Datei heraus das Hauptprogramm starten kann.
# Dadurch kann man in jeder Datei auf "play" drücken und es wird automatisch main.py gestartet.
if __name__=="__main__":
    import subprocess
    # Auf Linux oder Mac aktivieren Sie die folgende Zeile und deaktivieren Sie die Zeile danach:
    #subprocess.call("python3 main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    subprocess.call("main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    exit(0) # nun das Programm hier beenden .. wir wollen ja nur das Hauptprogramm starten und nicht *diese* Datei.
# Ende "BLOCK1"

import GameOver
from screen import screen
import pygame
import DatenSammeln as ds                                                  
from screen import screen


def gameWin(spieler):

    screen.blit(pygame.image.load("Bilder/GameWin.png"), (0, 0)) 
    pygame.display.update()
    pygame.mixer.Sound("Sound/Victory1.wav")
    pygame.mixer.Sound.play(pygame.mixer.Sound("Sound/Victory1.wav"))
    pygame.time.wait(4750)  
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.stop()                                               
    pygame.mixer.music.load("Sound/level.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    level = 0                                                                 
    ds.daten_csv(6, spieler.schritteZaehler)                              
    ds.daten_csv(7, spieler.schussZaehler)                                
    ds.write_csv()                                                       
    spieler.schritteZaehler = 0
    spieler.schussZaehler = 0
    return level
    
