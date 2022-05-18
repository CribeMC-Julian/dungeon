# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Figur-Klasse
# Autor: Johannes Tümler
# Letzte Änderung: 12.04.2022
# Zweck: Figur-Entität definieren
#
# Harpyie erbt Alles von Monster
# können den Held bei Berührung töten
# Harpyie kann in alle 4 Himmelrichtungen schießen, nacheinander pro Richtung (nicht zugleich)
# Harpyie kann seitwärts schießen
# Harpyie kann in alle Richtungen bewegen

# Der Nachfolgende Codeblock "BLOCK1" sorgt dafür, dass man aus jeder Datei heraus das Hauptprogramm starten kann.
# Dadurch kann man in jeder Datei auf "play" drücken und es wird automatisch main.py gestartet.
if __name__=="__main__":
    import subprocess
    # Auf Linux oder Mac aktivieren Sie die folgende Zeile und deaktivieren Sie die Zeile danach:
    #subprocess.call("python3 main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    subprocess.call("main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    exit(0) # nun das Programm hier beenden .. wir wollen ja nur das Hauptprogramm starten und nicht *diese* Datei.
# Ende "BLOCK1"


import sounds
from screen import screen
from KlasseFigur import Figur 
from time import time
from KlasseMonster import Monster
import pygame
from KlasseMagie import Magie
from KlasseGeist import Geist


class Harpyie (Geist):
   def __init__(self, x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster):            
        super().__init__(x, y, geschw, breite, hoehe, level, bildFigur, zeitMonster)            
       
        self.MonsterDupl = Geist                                                                                                                               #liste der erschaffennen Monster
        self.zeitDupl = zeitMonster                                                              
        self.zeitKugel = time()                                                                 
        self.b = 0
        self.zeitSpring = zeitMonster
        self.kugeln =[]
        self.dupliList = []     
        self.anzahlDouble = 1
        self.leben = True   
        self.stehRicht = 0                                                                
        self.zeitUnsicht = zeitMonster
        self.bildUnsicht = [pygame.image.load("Bilder/Geist/tot.png"),
                         pygame.image.load("Bilder/Geist/tot.png")]
        self.saveBildOben = self.bildOben                                                           
        self.saveBildUnten = self.bildUnten
        self.saveBildRechts = self.bildRechts
        self.saveBildLinks = self.bildLinks

   def reset(self):
        self.x = self.xReset
        self.y = self.yReset
        self.leben = True
        self.heldTot = False
        self.anzahlDouble = 1
        self.dupliList = []

   def faehigkeit(self):                      
        self.duplizieren()
        self.schuss()


        print(len(self.kugeln))                   
        
       

   def duplizieren(self):
        for dupli in self.dupliList:                                                            
           if dupli.mlaufen(self.heldDaten):                                                  
                self.heldTot = True                                                            

        if time() - self.zeitDupl >= 0.5 * self.anzahlDouble:                                 
            self.dupliList.append(self.MonsterDupl(self.x, self.y, self.geschw, self.breite, self.hoehe, self.level, self.bildFigur, time())) 
            self.zeitDupl = time()                                                                                                           
            self.anzahlDouble += 1
    
   def schuss(self) :                                       
          if len(self.kugeln) <= 0:
               
               if time() - self.zeitKugel >= 2:                            
                    if self.b == 0:
                         self.kugeln.append(Magie(self.x, self.y, 0, "R", 5))
                         self.b=1
                    elif self.b==1:
                         self.kugeln.append(Magie(self.x, self.y, 1, "R", 5))
                         self.b=2
                    elif self.b==2:
                         self.kugeln.append(Magie(self.x, self.y, 2, "R", 5))
                         self.b=3
                    elif self.b==3:
                         self.kugeln.append(Magie(self.x, self.y, 3, "R", 5))
                         self.b=0
                         self.zeitKugel = time() 
          
         
          for magie in self.kugeln:                                                                  
               if not self.hindernis(magie.kugelRec):
                    self.kugeln.remove(magie)
               magie.bewegung()
         
          for magie in self.kugeln:  
               for neutral in self.heldDaten.kugeln:
                    if magie.kugelRec.colliderect(neutral.kugelRec):                                       
                         self.heldDaten.kugeln.remove(neutral)
                         self.kugeln.remove(magie)
          
          for slide in self.kugeln:                                                   
               if slide.kugelRec.colliderect(self.heldDaten.rechteck):                                
                    sounds.soundTot()
                    screen.blit(self.heldDaten.bildtot, (self.heldDaten.x, self.heldDaten.y))
                    self.heldTot = True
       
          