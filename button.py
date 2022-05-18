# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Button
# Autor: Viktor Lysow
# Letzte Änderung: 30.03.2022
# Zweck: Knöpfe fürs Startmenü

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
import sys
import sounds
from screen import screen
from screen import font

aktivButton = False

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0, 0, 0))
    return textFlaeche, textFlaeche.get_rect()

def button(bx, by, nachricht, breite, hoehe, farbe_normal, farbe_aktiv, randDicke, maus, klick):
    global aktivButton

    if maus[0] > bx and maus[0] < bx + breite and maus[1] > by and maus[1] < by + hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx, by, breite, hoehe))
        if klick[0] == 1 and aktivButton == False:
            aktivButton = True

            if nachricht == "Neues Spiel":
                sounds.soundTor()
                pygame.time.wait(1000)
                return True

            elif nachricht == "Ende":
                pygame.quit()
                sys.exit()

        if klick[0] == 0:
            aktivButton = False

    else:
        pygame.draw.rect(screen, farbe_normal, (bx, by, breite, hoehe))
    pygame.draw.rect(screen, (0, 0, 0), (bx, by, breite, hoehe), randDicke)
    textGrund, textKasten = textObjekt(nachricht, font)
    textKasten.center = ((bx + (breite / 2)), (by + (hoehe / 2)))
    screen.blit(textGrund, textKasten)
    return False
