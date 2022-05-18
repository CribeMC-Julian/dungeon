# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Sounds
# Autor: Viktor Lysow
# Letzte Änderung: 30.03.2022
# Zweck: Verwaltung der Soundfiles

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

#Hier werden alle Geräusche aufgelistet

def soundTor():
    soundtor = pygame.mixer.Sound("Sound/tor.wav")
    soundtor.set_volume(0.5)
    pygame.mixer.Sound.play(soundtor)

def soundFeuer():
    soundFeuer = pygame.mixer.Sound("Sound/Fire.wav")
    soundFeuer.set_volume(0.5)
    pygame.mixer.Sound.play(soundFeuer)

def soundMagie():
    soundMagie = pygame.mixer.Sound("Sound/Attack2.wav")
    soundMagie.set_volume(0.5)
    pygame.mixer.Sound.play(soundMagie)

def soundKolMag():
    soundKolMag = pygame.mixer.Sound("Sound/mag.wav")
    soundKolMag.set_volume(0.5)
    pygame.mixer.Sound.play(soundKolMag)

def soundTot():
    soundTot = pygame.mixer.Sound("Sound/tot.wav")
    soundTot.set_volume(0.5)
    pygame.mixer.Sound.play(soundTot)

def soundGewonnen():
    soundTot = pygame.mixer.Sound("Sound/Victory1.wav")
    soundTot.set_volume(0.5)
    pygame.mixer.Sound.play(soundTot)

def soundLevel():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/level.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(1)

def soundBoss():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("Sound/levelBoss.mp3")
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.6)