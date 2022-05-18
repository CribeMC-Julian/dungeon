# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Levelmanagement-Klasse
# Autor: Johannes Tümler
# Letzte Änderung: 30.03.2022
# Zweck: Speichern des aktuellen Levels als static Klassenvariable

# Der Nachfolgende Codeblock "BLOCK1" sorgt dafür, dass man aus jeder Datei heraus das Hauptprogramm starten kann.
# Dadurch kann man in jeder Datei auf "play" drücken und es wird automatisch main.py gestartet.
if __name__=="__main__":
    import subprocess
    # Auf Linux oder Mac aktivieren Sie die folgende Zeile und deaktivieren Sie die Zeile danach:
    #subprocess.call("python3 main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    subprocess.call("main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    exit(0) # nun das Programm hier beenden .. wir wollen ja nur das Hauptprogramm starten und nicht *diese* Datei.
# Ende "BLOCK1"

class LevelManagement:
    Level = 0                       # static!!

    # Die folgenden sind wichtig für die fps-Berechnung und damit die Schrittweite der Figuren 
    deltaTime = 0                   # static!!
    fpsTarget = 30                  # static!!
    numFrames = 0                   # static!!
    timeNeeded = 0                  # static!!
    fpsCurrent = 1                  # static!!

    def __init__(self):
        LevelManagement.Level = 0