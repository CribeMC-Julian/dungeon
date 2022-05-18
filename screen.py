# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Pygame-Fenster
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 30.03.2022
# Zweck: Aktivierung von Pygame mit entsprechenden Parametern

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

pygame.init()

screen = pygame.display.set_mode([816, 624])
clock = pygame.time.Clock()
pygame.display.set_caption("Test") # Sie dürfen sich hier hinzufügen
font = pygame.font.SysFont('Impact', 20)

feld = 48   # pixel