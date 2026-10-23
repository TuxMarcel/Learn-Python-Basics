'''
Das hier ist der anfang des Python Tutorials in dieser Datei werden die ersten Basics von Python bearbeitet.

https://www.python-kurs.eu/python_kurs.php 
https://www.youtube.com/watch?v=e6vPt_e9sRw <<--- Tutorial Video auf Deutsch

Dieses Tutorial soll nicht nur die Syntax zeigen, sondern auch Grundlegende Programmierkonzepte verstaendlich machen.

Damit nicht jedes mal der ganze Code in dieser Datei ausgeführt wird Werden die " # " hinter den Funktionen gesetzt.
Kommentare in dieser Datei haben immer mindestens " ## " vorne dran stehen.

Beim Lesen kann also immer der Code direkt ausgeführt werden.
Vergiss aber nicht nach dem ausführen wieder den Code als # Kommentar zu setzen.

Viel Spaß beim lernen.

-------------------------------------------------------------------------

#### Lektion 1: Hallo Welt
###  Das ist die erste Funktion "print()" sie ist eine der elementarsten Funktionen in Python
##   ---> Ausgabe der Inhalte im Terminal
-------------------------------------------------------------------------
'''

#print('Hallo Welt!')                                                            
#print("Ich habe Hallo Welt programmiert und bin bald ein Python Profi!")        
 
## man kann '' als anführungs für Strings (Zeichenketten) nehmen
## aber auch "" doppelte Anführungszeichen ändern nichts daran, dass es ein String 

'''
Python führt Code immer nacheinander aus!
In der Konsole hat man hier also eine Ausgabe:

Hallo Welt!
Ich habe Hallo Welt programmiert und bin bald ein Python Profi!

Python ist eine Interpretersprache, dazu später mehr.


----------------------------------------------------------------------
### Lektion 2: Datentypen
##  In Python unterscheidet man verschiedene Arten von Daten.
#   ---> Verschiedene datentypen liefern verschiedene Ergebnisse.
----------------------------------------------------------------------
Die Vier GrundTypen:

1. Text (str/ String / Zeichenkette):
    - Alles, was ist Anführungszeichen steht (z.B "Hallo" oder '123')
    - Auch Zahlen werden als Text behandelt, wenn Anfühungszeichen drumherumstehen.

2. Ganzzahlen (int/Integer)
    - Alle Zahlen ohne Komme - egal ob positiv, negativ oder Null (z.B 42, -5, 0)
    - Mit ihnen kann Python direkt rechnen.

3. Fließkommazahlen (float/ Float):
    - Zahlen mit Nachkommastellen.
    - Wichtig: In Python wird immer ein Punkt "." statt eines Kommas verwendet (z.B 50.5 oder 3.14). Selbst eine Zahl wie 50.0 gilt als Float.

4. Wahrheitswärte (bool/ Boolean):
    - Kennt nur zwei Zustände: True (wahr) oder False (falsch) oder 1 oder 0 mann kann auch ja oder nein sagen.
    - Der erste Buchstabe muss immer großgeschrieben werden.

Zwei wichtige Zusatzfunktionen für Anfänger:
    - type(): Teigt dir, welchen Datentyp ein Wert gerade hat.
    - Typunmwandlung: mit str(10) machst du aus einer Zahl einen Text , mit int("10") aus einem Text eine Zahl. 


----------------------------------------------------------------------
### Lektion 3: Aretmetische Operatoren
##  Python kann wie ein Taschenrechner verwendet werden. 
#   Dafür gibt es verschiedene mathematischen Operatoren:
----------------------------------------------------------------------
'''
## 1. Standard-Rechenarten:

#print(10 + 3)   ## + Addition 10+3 ergibt 13 im Terminal
#print(10 - 3)   ## - Subtraktion 10-3 ergibt 7
#print(10 * 3)   ## * Multiplikation 10 * 3 ergibt 30
#print(10 / 3)   ## / Division 10 / 3 ergibt 3.3333333333333335 als Ausgabe im Terminal

# Es gibt jetzt aber noch eine Sache zu beachten und zwar kann man das + zum Beispiel auch dazu verschenden Zeicheketten miteinander zu verbinden.

#print('1' + '1')  ## Ausgabe im Terminal ist 11 

'''
Am besten du Testest einw enig was man jetzt schon alles mit den Datentypen machen kann zum Beispiel was passieren würde wenn du print('10' - '2') 
oder print("Hallo" + int(Welt)) passiert.
'''

## 2. Besondere Operatoren:

#print(10 // 3)     ## // Ganzzahldivision / Floor Division teilt und rundet das ergebnis ab. Ergebnis hier also 3.
#print(10 % 3)      ## % Modulo / Restwert Teilt zwei Zahlen und gibt nur den Rest zurück. Ergebnis hier also 1. (Tip: Nützlich zur Prüfung ob eine Zahl gerade 
                    ## oder ungerade ist)
#print(10 ** 3)     ## ** Potenzierung ist gleich 10³ = 1000


## 3. Die Vergleichsoperatoren < und > (Kleiner / Größer als)

'''
Die Spitzen Klammern < und > sind die sogenannten Vergleichsoperatoren:

- < (Kleiner als): Prüft, ob der linke Wert kleiner ist als der rechte (z.B. 5 < 10 ergibt True)
- > (Größer als): Prüft, ob der linke Wert größer ist als der rechte (z.B. 5 > 10 ergibt False)
- <= / =>: Kleiner-gleich / Größer-gleich
- ==: Prüft auf Gleichheit.

Das Ergebnis eines solchen Vergleichs ist immer ein Wahrheitswert (bool: True oder False)
'''

'''
----------------------------------------------------------------------
#### Lektion 4: Variablen
###  Variablen sind Platzhalter dem Werte zugewiesen werden können
##   ---> zur Wiederverwendung an späterer Stelle im Programm
----------------------------------------------------------------------
'''


#x = 5
#print(x)

## Der Wert 5 wird in der Variable x gespeichert und mit der print() funktion ausgegeben

#print("x")

## Wegen der Anführungsstriche "" in der Funktion wird nun x und nicht 5 ausgegeben.

#print(x)
#x = 5

## Python führt Code von oben nach unten aus. Schreibt man es so gibt das Terminal eine Fehlermeldung.

'''
Praxisbeispiel: Man kann mit Variablen und der print()-Funktion schon richtig gut automatisieren. Du möchtest zum Beispiel 10
E-Mails ab verschiedene Firmen schreiben...und musst nicht in jeder E-Mail den Firmennamen manuell anpassen. Du änderst einfach
den Wert einer einzigen Variable, und Python setzt den neuen Namen im Ausgabetext automatisch überall ein.

(Die Variable ist hier das Eigentliche Automatisierungskonzept. Die Kernbotschaft: Eine Variable dient als zenraler 
Stellvertreter/ Platzhalter. Ändert man den Inhalt der Variable einmal, passt sich das gesamte Programm an.)

zurück zur E-Mail Geschichte....

Beispiel E-Mail:

Hallo liebes Team von {firmenname},

ich möchte gerne bei euch in der Firma {firmenname} arbeiten.
Ich würde mich über eine Antwort freuen!
'''

#firmenname = "SuperFirma"
#print("Hallo liebes Team von " + firmenname + ", ich möchte gerne bei euch in der Firma " + firmenname + " arbeiten."
#"ich würde mich über eine Antwort freuen!")

'''
Jetzt haben wir uns Theoretisch erstmal nur 1x "Superfirma" schreiben "Gespart".
Aber wir wollten ja auch an 10 Firmen schreiben.
Nicht Optimal aber schon effektiver als immer den ganzen Text neu zu schreiben können wir jetzt  immer die Variable anpassen wie es uns gefällt.
Zum Beispiel könnte man jetzt SuperFirma ersetzen durch SpiederFirma. :D
Aber denk mal so nach: Stell dir vor du hättest einen Text wo die Variable 1000 mal vorkommt. Dann ist sie nicht mehr so useless!


Man kann auch mehrere Variablen in einen Text einfügen. Und die Variante die Variablen "+ +" zu schreiben könnte bei längeren Texten umständlich und 
unübersichtlich werden. Desegen kann man f-Strings verwenden.
'''
#firmenname = "SpiederFirma"
#berufsbild = "Kammerjäger"

#print(f"Hallo liebes Team von {firmenname}, ich möchte gerne bei euch in der Firma {firmenname} arbeiten."
#f" Ich habe eine Weiterbildung zum {berufsbild} gemacht.")

'''
2 Dinge zu dem Code. Schreibst du f vor den String kannst du die Variablen in geschweiften Klammern setzen.
Die andere Sache ist meine Schreibweise nach dem Zeilenumbruch. Sowohl die Anführungszeichen als auch das f muss nein weiteres mal hingeschrieben.


Wie dir bestimmt aufgefallen ist  gibt das Terminal das aber nicht mit dem Zeilenumbruch an. Wenn du Zeilenumbrüche in der Terminalausgabe willst kannst du \n
nutzen. Das sieht dann so aus:
'''
#firmenname = "SpiederFirma"
#berufsbild = "Kammerjäger"

#print(f"Hallo liebes Team von {firmenname},\nich möchte gerne bei euch in der Firma {firmenname} arbeiten. \n"
#f"Ich habe eine Weiterbildung zum {berufsbild} gemacht.")

'''
Mit Variablen kann man aber noch mehr machen. Angenommen wir wollen jetzt noch angeben wie Lange die weiterbildung gedauert hat.

'''
#firmenname = "SpiederFirma"
#berufsbild = "Kammerjäger"
#weiterbildungsdauer = 6

#print(f"Hallo liebes Team von {firmenname},\nich möchte gerne bei euch in der Firma {firmenname} arbeiten. \n
#f"Ich habe eine Weiterbildung zum {berufsbild} gemacht.\n
#f"{weiterbildungsdauer} habe ich für Weiterbildung benötigt")

'''
Was wir aber auch noch zusätzlich machen können ist in der Variable zu Rechnen. Jetzt waren wir gut und haben die Weiterbildung 2 Monate früher abgeschlossen.
'''
#firmenname = "SpiederFirma"
#berufsbild = "Kammerjäger"
#weiterbildungsdauer = 6 - 2

#print(f"Hallo liebes Team von {firmenname},\nich möchte gerne bei euch in der Firma {firmenname} arbeiten. \n
#f"Ich habe eine Weiterbildung zum {berufsbild} gemacht.\n
#f"{weiterbildungsdauer} habe ich für Weiterbildung benötigt")

'''
Und das gute daran ist. Python rechnet für uns die 6 - 2 aus direkt aus. Und weil wir keine "" verwendet haben erkennt Python automatisch das es ein integer ist
und kein String.
'''
