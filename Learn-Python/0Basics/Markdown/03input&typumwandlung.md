'''
### input() & Typenumwandlung ###

Willkommen zur nächsten Etappe deiner Python-Journey! In dieser Datei behandeln wir die input()-Funktion und das Konzept der Typenumwandlung(TypeCasting).

Schon wie in der 00Basic.py ist Ausführbarercode Auskommentiert mit genau einem "#" vor dem code. Entferne das Zeichen um den Code auszuführen. 
Vergiss nicht neue zu setzen wenn du weiter liest.
'''

### Lektion 1: Die input().Funktion (Interaktivität & Programmpause)
'''
Bisher waren alle Werte in unseren Skripten fest im Code niedergeschrieben (hartcodiert).
Mit der eingebauten Funktion input() machen wir programme dynamisch:

    - Ablauf: Python gibt den Text in den Klammern im Terminal aus und pausiert die Programmausführung
    - Das Programm wartet so lange, bis der Nutzer etwas eintippt und die Enter-Taste drückt
    - Der eingegebene Wert wird zurückgegeben und kann direkt in einer Variable gespeichert werden
'''

#print('--- Lektion 1 ---')

## Das Programm pausiert hier und wartet auf eine Eingabe
#benutzername = input('Wie heißt du? ')

## Ausgabe der dynamischen Eingabe
#print(f'Hallo {benutzername}! Willkommen im Python-Kurs.')


### Lektion 2: Der "String-Fallstrick" bei Eingaben
'''
Ein zentraler Detail in Python: Die Funktion input() gibt immer einen String(str) zurück. Selbst wenn du Terminal eine Zahl (wei 25) eingibst,
speichert Python sie als Text.

Versuchst du zwei solche Eingaben mit einem + zu addieren, werden die Texte nur aneinander gehängt (Verkettung), anstatt mathematisch gerechnet!
'''

print('\n---Lektion 2 ---')

eingabe_a = input('Gib Zahl A ein: ')  # z.B. 5
eingabe_b = input('Gib Zahl B ein: ')  # z.B. 3

print('Datentyp von eingabe a:', type(eingabe_a))

## Der + Operator verbindet hier Texte ('5' + '3' --> '53')
falsches_ergebnis = eingabe_a + eingabe_b
print(f"Falsches Ergebnis ('{eingabe_a}' + '{eingabe_b}'): {falsches_ergebnis}")


### Lektion 3: Typumwandlung (type Casting mit int() und float())
'''
Damit du mit nutzereingaben rechnen kannst, musst du den Text explizit in eine Zahl umwandlen (Casting):

    - int():   Wandelt einen String mit einer Ganzzahl in den Typ int um.
    - float(): Wandelt einen String mit einer Kommazahl Typ float um (Wichtig: Punkt als Dezimaltrenner)
''' 

print('\n--- Lektion 3 ---')

## Schritt 1: Text-Eingaben holen
text_eingabe = input('Gib deine Liegĺingszahl ein: ')

## Schritt 2: Manuelle Umwandlung in einen Integer
echte_zahl = int(text_eingabe)

print('Datentyp nach int():', type(echte_zahl))
print(f'Rechnen funktioniert jetzt: {echte_zahl} + 10 = {echte_zahl +10}')


### Lektion 4: Best Practice - Verschachtelte Eingaben direkt umwandeln ### 
'''
In der Praxis trennt man die Eingabe und die Typumwandlung selten in zwei Zeilen. man umschließt die input()-Funktion direkt mit int() oder float().
'''

print('\n--- Lektion 4 ---')

## Direktes Casting bei der Eingabe:
alter = int(input('Wie alt bist du?: '))
groesse_m = float(input("Wie groß bist du in  Metern? (z.B. 1.80): "))

## Rechnen & Ausgabe mit f-Strings
print(f'In 5 Jahren bist du {alter + 5} Jahre alt.')
print(f'Deine Größe in cm: {groesse_m * 100} cm')