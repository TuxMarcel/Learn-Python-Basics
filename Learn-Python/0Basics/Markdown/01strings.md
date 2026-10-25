'''
In dieser Datei gehen wir spezifisch auf Strings ein. 
Strings werden ja mit str abgekürtzt.

Hier nochmal eine kleine Wiederholung.

Schon wie in der 00Basic.py ist Ausführbarercode Auskommentiert mit genau einem "#" vor dem code. Entferne das Zeichen um den Code auszuführen. 
Vergiss nicht neue zu setzen wenn du weiter liest.
'''
## - Escape-Zeichen (\):Wenn du Anführungszeichen im Text verwenden willst oder eine neue Zeile brauchst, nutzt den Backslash \ :
   
###    - \n: Neue Zeile (New Line)
###    - \t: Tabulator Abstand
###    - \" oder \': Anführungszeichen im Text darstellen
###    - \\: Gibt einen echten Backslash aus. 

########################################################################################################################################################

'''
### Lektion 1 - Erstellung von Strings und Mehrzeiler ###

Ein String ist eine Kette von Zeichen, die in einfache ('...') oder doppelte ("...") Anführungszeichen eingeschlossen wird. Python behandelt beide Varianten,
gleich solange Start- und Endzeichen übereinstimmen. Mehrzeilige Strings: Mit drei Anführungszeichen """...""" kannst du langen Text 
über mehrere Zeilen schreiben.
'''
#print('--- Lektion 1 ----)
#print("Hallo Welt mit doppelten Anführungszeichen")
#print('Hallo Welt mit einfachen Anführungszeichen')

#mehrzeilig = """Erste zeile
#Zweite Zeile
#Dritte Zeile"""

#print(mehrzeilig)


'''
### Lektion 2 - Escape-Sequenzen (Steuerzeichen im Terminal) ###
'''
##  Der Backslash \ unterbricht die normale Textverarbeitung und signalisiert Python ein Steuerzeichen.
##  Oben ist eine Tabelle für die einzelnen Backslash eingaben.

#print('\n--- Lektion 2 ----')
#print("Zeile 1\nZeile 2 (durch \\n getrennt)")
#print("Einkaufsliste:\n\t- Aepfel (durch \\t eingerückt)\n\t- Bohnen")
#print("Er sagte: \"Python ist genial!\"")
#print("Dateipfad: /home/user/Coden/Python")


'''
### Lektion 3 - Strings verbinden & Formatieren (f-strings vs. +) ###

Strings können mit + verknüpft werden. Wenn du eine zahl mit einem String verinden willst, schlägt + fehl (TypeError), weshalb die Zahl zuerst mit str()
umgewandelt werden muss. Die moderne und einfache Lösung sind f-strings: Ein f vor den Anführungszeichen erlaubt es, Variablen und Rechnungen direkt
in geschweiften klammern {...} winzusetzen.
'''

#print('\n--- Lektion 3 ---')
#vorname = "Michael"
#alter = 30

## Alte Methode mit str() Umwandlung:

#print("Name: " + vorname + " , Alter: " + str(alter))


## Moderne Methode mit f-String:

#print(f'name: {vorname}, Alter: {alter} (in 5 Jahren: {alter + 5})')


## String-Wiederholung mit *:

#print("=" * 25)


'''
### Lektion 4 - String-Analyse (Länge len(), Indexing & Slicing)

- len(): Gibt die Gesamtzahl aller Zeichen inklusive Leerzeichen zurück.

- Indexing (string[i] ): Der erste Buchstabe liegt auf Index 0, der letzte auf Index -1

- Slicing (string[start:stop] ): Schneidet einen Teilbereich heraus. Der start -Index ist inklusive, der stop -Index ist exklusive (wird nicht mehr mitgenommen).

'''


## len(), Indexing & Slicing

#print("\n--- Lektion 4 ---")
#wort = "Python"

#print('Länge von \"Python\":', len(wort))
#print('Erster Buchstabe (Index 0):', wort[0])
#print("Letzter Buchstabe (Index -1):", wort[-1])

## Slicing: Index 0 bis 2 (Index 2 wird NICHT mitgenommen)

#print('Slicing [0:2]:', wort[0:2])
#print('Slicing [:4] (vom Anfang bis Index 3):', wort[:4])
#print('Slicing [2:] (ab Index 2 bis zum Ende):', wort[2:])


'''
### Lektion 5 - Wichtige String-Methoden (Transformation) ###

Methoden sind spezielle Funktionen, die mit einem Punkt direkt an den String angehängt werden (string.methode()):

    - .upper() / .lower(): Wandelt Groß-/Kleinschreibung um
    - .strip(): Entfernt störende Leezeichen am Anfang und Ende.
    - .replace(alt, neu): Ersetzt Zeichen oder Wörter.
    - .split(trennzeichen): Zerschneidet den String an einem Trennzeichen in eine Liste 

Was eine Liste ist kommt später. Ist erstmal Nice to know!

'''

#print('\n--- Lektion 5 ---')

#raw_text = "   Hallo Python Welt   "

#print("Original mit Leerzeichen: '" + raw_text + "'")
#print("Bereinigt mit .strip():   '" + raw_text.strip() + "'")
#print("Großbuchstaben . upper(): ", raw_text.strip().upper())
#print("Großbuchstaben . lower(): ", raw_text.strip().lower())
#print("Text ersetzen .replace(): ", raw_text.strip().replace("Welt","Profi"))

#daten_string = "Max-24-Deutschland"
#print("String zerlegen mit .split('-'):", daten_string.split("-"))


'''
### Lektion 6 - Suchen & Prüfen (Validierung) ###

    - .find("..."): Liefert die Start-Indexposition eines Suchbegriffs zurück.
    - in: Prüft als Operator, ob ein Wort im Text vorkommt (True/False).
    - .isnumeric() / .isalpha(): Prüfen, ob ein String rein aus Zahlen oder rein aus Buchstaben besteht. 
'''

#print('\n--- Lektion 6 ----')

#satz = "Das ist ein Python-Kurs"

#print(satz)
#print("Start-Index von 'Python' (.find()):", satz.find("Python"))
#print("Ist 'Python' im Satz enthalten? (in):", "Python" in satz)

#eingabe_zahl = "12345"
#eingabe_text = "Python"

#print(eingabe_zahl)
#print(eingabe_text)
#print("Ist '12345' numerisch? (.istnumeric()):", eingabe_zahl.isnumeric())
#print("Besteht 'Python' nur aus Buchstaben? (.isalpha()):", eingabe_text.isalpha())
