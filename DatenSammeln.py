# (c) Hochschule Anhalt, veröffentlicht unter MIT-Lizenz
# Datensammler
# Autor: Viktor Lysow, Johannes Tümler
# Letzte Änderung: 22.04.2022
# Zweck: Daten für den Matlab Beleg sammeln

# Der Nachfolgende Codeblock "BLOCK1" sorgt dafür, dass man aus jeder Datei heraus das Hauptprogramm starten kann.
# Dadurch kann man in jeder Datei auf "play" drücken und es wird automatisch main.py gestartet.
if __name__=="__main__":
    import subprocess
    # Auf Linux oder Mac aktivieren Sie die folgende Zeile und deaktivieren Sie die Zeile danach:
    #subprocess.call("python3 main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    subprocess.call("main.py", shell=True)  # die richtige Main-Datei aufrufen (unser eigentliches Hauptprogramm)
    exit(0) # nun das Programm hier beenden .. wir wollen ja nur das Hauptprogramm starten und nicht *diese* Datei.
# Ende "BLOCK1"

import datetime

dateiName = 'Spiel_Daten.csv'

"""
Erläuterung zum Daten Sammeln:
    [0] = Jahr
    [1] = Monat
    [2] = Tag

    [3] = Stunde
    [4] = Minute
    [5] = Sekunde

    [6] = Schritte Held
    [7] = Schüsse Held
    [8] = Zeit Level 1
    [9] = Zeit Level 2 
    ###ALT[10] = Zeit Level 3
    [10] = Gesamt Zeit
    [11] = Besiegt in Level
"""
# ['0','Datum','Uhrzeit','Schritte Held', 'Schüsse Held´', 'Zeit Level 1', 'Zeit Level2', 'Zeit Level3', 'Gesamt Zeit', 'Besiegt in Level']

neue_zeile = [0,0,0,0,0,0,0,0,0,0,0,0]  # Zeile, die eingefügt wird


def open_csv():
    try:  # Test, ob die csv existiert
        op_text = open(dateiName)
    except:  # Wenn nicht, neu erstellen
        neu_text = open(dateiName, 'w')
        #neu_text.write(f'{zeile0[0]},{zeile0[1]},{zeile0[2]},{zeile0[3]},{zeile0[4]},{zeile0[5]},{zeile0[6]},{zeile0[7]},{zeile0[8]},{zeile0[9]},{zeile0[10]},{zeile0[11]}')
        neu_text.close()
        op_text = open(dateiName)

    text = op_text.read()
    op_text.close()

    zeilen = text.split('\n')
    tabelle = []
    if not zeilen == ['']:
        for i in range(len(zeilen)):
            spalten = zeilen[i].split(',')
            tabelle.append(spalten)

    return tabelle


def daten_csv(spalte,
              info):  # (welche Spalte, die Information in der Spalte)  Zeit, Schritte und Schüsse werden hier übergeben

    info = str(info)

    neue_zeile[spalte] = info


def write_csv():  # Die csv wird hier überschrieben (Speichern)
    neue_zeile[0] = datetime.datetime.today().year  # Datum in Spalte 1 - 3
    neue_zeile[1] = datetime.datetime.today().month
    neue_zeile[2] = datetime.datetime.today().day

    neue_zeile[3] = datetime.datetime.today().hour  # Uhrzeit in Spalte 3 - 6
    neue_zeile[4] = datetime.datetime.today().minute
    neue_zeile[5] = datetime.datetime.today().second

    tabelle = open_csv()  # Gesamte Tabelle
    tabelle.append(neue_zeile)  # Gesmate Tabelle + der neuen Zeile

    neu_text = open(dateiName, 'w')

    for i in range(len(tabelle)):
        neu_text.write(
            f'{tabelle[i][0]},{tabelle[i][1]},{tabelle[i][2]},{tabelle[i][3]},{tabelle[i][4]},{tabelle[i][5]},{tabelle[i][6]},{tabelle[i][7]},{tabelle[i][8]},{tabelle[i][9]},{tabelle[i][10]},{tabelle[i][11]}')
        if not len(tabelle) - 1 == i:
            neu_text.write('\n')

    neu_text.close()
    reset()


def reset():  # neue Zeile wird wieder auf 0 gesetzt für das eventuelle nächste Spiel
    global neue_zeile
    neue_zeile = [0,0,0,0,0,0,0,0,0,0,0,0]
