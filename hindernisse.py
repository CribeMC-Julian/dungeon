# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Hindernisse
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 30.03.2022
# Zweck: Definition der vorhandenen Hinternisse

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

feld = 48 # pixel
# es gibt 13 x 17 Felder (Höhe x Breite)
                                    # , Farbe ,  (links, oben, breite, höhe), ausgefüllt
grenzeLevel1 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*12),0), # linke Wand
                pygame.draw.rect(screen, (0,0,0), (feld*16,0,feld,feld*13),0), # rechte Wand
                pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0), # obere Wand
                pygame.draw.rect(screen, (0,0,0), (0,feld*12,feld*17,feld),0), # untere Wand
                # die nächsten Zeilen definieren die diversen Hindernisse des Levels
                pygame.draw.rect(screen, (0,0,0), (feld*5, feld, feld*2, feld*4),0),
                pygame.draw.rect(screen, (0,0,0), (feld*3, feld*2,feld*2, feld),0),
                pygame.draw.rect(screen, (0,0,0), (feld*7, feld*6,feld*2, feld*6),0),
                pygame.draw.rect(screen, (0,0,0), (feld*9, feld*6,feld*4, feld),0),
                pygame.draw.rect(screen, (0,0,0), (feld*16,0, feld, 13*feld),0),
                pygame.draw.rect(screen, (0,0,0), (0, feld*12, feld*17, feld),0)]

# Kollisionen in Level2
grenzeLevel2 = [pygame.draw.rect(screen, (0,0,0), (0,0,feld,feld*12),0), # linke Wand
                pygame.draw.rect(screen, (0,0,0), (feld*16,0,feld,feld*13),0), # rechte Wand
                pygame.draw.rect(screen, (0,0,0), (0,0,feld*17,feld),0), # obere Wand
                pygame.draw.rect(screen, (0,0,0), (0,feld*12,feld*17,feld),0), # untere Wand
                # die nächsten Zeilen definieren die diversen Hindernisse des Levels
                pygame.draw.rect(screen, (0,0,0), (feld,feld,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*8,feld*3,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*5,feld*6,feld*2,feld*4),0),
                pygame.draw.rect(screen, (0,0,0), (feld*3,feld*7,feld*2,feld*2),0),
                pygame.draw.rect(screen, (0,0,0), (feld*10,feld*7,feld*2,feld*3),0),
                pygame.draw.rect(screen, (0,0,0), (feld*9,feld*8,feld,feld),0)]

grenzeLevel= []                                                                         #liste mit allen Hindernissen
grenzeLevel.append(grenzeLevel1)
grenzeLevel.append(grenzeLevel2)

tor1 = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                      #Ziel in Level 1
tor2 = pygame.Rect(3*feld + feld/2, feld, 5, 5)                                    #Ziel in Level 2

# Testfunktion um die Ränder/Felder einzufärben, an denen eine Kollision ausgeführt wird.
# Falls gewünscht, testweise aus Level2.py aufrufen.
def drawLevel2():
                        # , Farbe ,  (links, oben, breite, höhe), ausgefüllt
    pygame.draw.rect(screen, (255,0,0), (0,0,feld,feld*12),0) # linke Wand
    pygame.draw.rect(screen, (0,255,0), (feld*16,0,feld,feld*13),0) # rechte Wand
    pygame.draw.rect(screen, (0,0,255), (0,0,feld*17,feld),0) # obere Wand
    pygame.draw.rect(screen, (255,255,0), (0,feld*12,feld*17,feld),0) # untere Wand
    pygame.draw.rect(screen, (0,0,0), (feld,feld,feld*2,feld*2),0)
    pygame.draw.rect(screen, (0,0,0), (feld*8,feld*3,feld*2,feld*2),0)
    pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0)
    pygame.draw.rect(screen, (0,0,0), (feld*6,feld*4,feld*3,feld*2),0)
    pygame.draw.rect(screen, (0,0,0), (feld*5,feld*6,feld*2,feld*4),0)
    pygame.draw.rect(screen, (0,0,0), (feld*3,feld*7,feld*2,feld*2),0)
    pygame.draw.rect(screen, (0,0,0), (feld*10,feld*7,feld*2,feld*3),0)
    pygame.draw.rect(screen, (0,0,0), (feld*9,feld*8,feld,feld),0)