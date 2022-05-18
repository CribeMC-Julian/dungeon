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

from screen import screen
import pygame
import DatenSammeln as ds                                                   # Für den Matlab Beleg
from screen import screen

#Hier kommt der Game Over Hintegrund und dann wird alles für den Startbildschirm eingestellt bzw zurück gestellt

def gameOver(spieler):
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/Gameover2.wav")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)
    screen.blit(pygame.image.load("Bilder/GameOver.png"), (0, 0))    
    pygame.display.update()
    pygame.time.wait(4000)                                       
    pygame.mixer.music.stop()                                        

    level = 0
    ds.daten_csv(6, spieler.schritteZaehler)                              # Anzahl der Schritte wird gespeichert (für Matlab)
    ds.daten_csv(7, spieler.schussZaehler)                                # Schusszahl wird gespeichert (für Matlab)
    ds.write_csv()                                                        # csv Datei wird erstellt oder überschrieben (für Matlab)
    spieler.schritteZaehler = 0
    spieler.schussZaehler = 0
    return level