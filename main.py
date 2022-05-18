# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Hauptprogramm
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 12.03.2021
# Zweck: Steuerung des gesamten Spielablaufs - dieses Programm muss gestartet werden, um das Spiel zu spielen.
#
# Das Hauptprgramm
# hier wird der Held erstellt
# Hauptschleife greift auf alle Level zu

from KlassePrinzessin import Prinzessin
from KlasseLevelmanagement import LevelManagement
import pygame
import GameWin
import sys
import sounds
from screen import screen
from time import time
from hindernisse import feld
from startBild import start
from KlasseHeld import Held
from Level1 import Level1
from Level2 import Level2
from GameOver import gameOver
import DatenSammeln as ds                               # Für den Matlab Beleg

zeitmax = 0                                                             #performance test
zeit_start_ges = 0

spieler1 = Held(x = 582, y = 476, geschw = 15, breite = feld, hoehe = feld, level = 1, bildFigur="Held")                    #Figuren erstellen
sounds.soundLevel()
LevelManagement.Level = 0

go = True
clock = pygame.time.Clock()

while go:      
    LevelManagement.deltaTime = clock.tick(LevelManagement.fpsTarget)
                                               # das Spiel soll mit 30-50 fps (Bilder pro Sekunde) laufen
                                               # Falls irgendwas komisch läuft (Monster in Wänden, nichts bewegt sich, oder ähnlich)
                                               # dann mal das fpsTarget mit kleineren/größeren Werten testen (siehe Klasse LevelManagement)
    LevelManagement.numFrames += 1
    LevelManagement.timeNeeded += LevelManagement.deltaTime
    zeit = time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:	# Wenn Escape gedrueckt wird, posten wir ein QUIT-Event in Pygames Event-Warteschlange.
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    screen.fill((0, 0, 0))

    if LevelManagement.Level == 0:                                                          #Startbildschrim
        LevelManagement.Level = start()
        zeit_start_ges =time()                                              #Zeit des Startes vom Spiel (für Matlab)

    elif LevelManagement.Level == 1:                                                         #Geist
        LevelManagement.Level = Level1(spieler1)

    elif LevelManagement.Level == 2:                                                         #Boss
        LevelManagement.Level = Level2(spieler1)
    
    elif LevelManagement.Level == 3:                                                         #Game Over
        ds.daten_csv(10, round(time() - zeit_start_ges))                      #Gesamt Spielzeit (für Matlab)
        LevelManagement.Level = gameOver(spieler1)
        spieler1.neu_Position(582, 476, 1)                                            

    pygame.display.update()

    if zeitmax < time() - zeit:                                                         #performance Test
        zeitmax = time() - zeit
        #print(zeitmax)

    