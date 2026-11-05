'''
Wir sind endlich im Advanced Ordner angekommen.
Ab hier wird Python richtig mächtig, denn wir lernen dem Computer zu sagen, wie er sich wiederholen soll,
ohne dass wir denselben Code tausend mal hinschreiben müssen.

Schleifen (Loops)

Stell dir vor, du möchtest 100 E-Mails verschicken oder jedes Wort in einem langen Text überprüfen. Ohne Schleifen müsstest du den
Code hunderte male kopieren. Schleifen sind das Werkzeug der Automatisierung. In Python gibt es zwei Hauptarten: die for-Schleife und die
while-Schleife.
'''

### Lektion 1: Die for-Schleife - Der Sammler
'''
Die for-Schleife wird verwendet,um über Sequenz (wie ein String, eine Liste oder eine Zahlenreihe) zu iteriren. Man kann sie sich wie einen 
Lektor vorstellen, der Wort für Wort ein Manuskript durchgeht.
'''

## Beispiel 1: Über einen String iterieren (Wiederholung aus 01)
text = "Python" 
for buchstabe in text:
    print(f'Aktueller Buchstabe: {buchstabe}')


## Beispiel 2: Die range()-Funktion nutzen
## range() erzeugt eine Zahlenfolge. Wir nutzen sie oft, um Code x-mal auszuführen.

print('\n--- Zählen mit range() ---')
for i in range(5):
    print(f'Durchlauf Nummer: {i}')
    # Achtung: Es beginnt bei 0 und endet VOR der 5 (also 0, 1, 2, 3, 4)


'''
Profi-Tipp zu range(start, stop, step)

range() ist extrem flexibel. Du kannst einen Startpunkt, ein Ende und eine Schrittweite definieren:
'''

## Start bei 2, Stop vor 10, Schrittweite 2 (gibt 2, 4, 6, 8 aus)

for zahl in range(2, 10, 2):
    print(zahl)

## Rückwärts zählen (Start 10, Stop vor 0, Schrittweite -1)

print('\nCountdown:')
for i in range(10, 0, -1):
    print(i)
print('Zündung!')


### Lektion 2: Die while-Schleife: Der Ausdauernde 
'''
Während for genau weiß, wie oft es laufen muss, läuft while so lange, wie eine Bedingung wahr ist. Hier verknüpfen wir direkt dein
Wissen aus 05(Bedingungen).
'''

print('\n--- Die while-Schleife ---')
akku = 3

while akku > 0:
    print(f'Akku-Stand: {akku}%')
    akku -= 1   #Das ist das selbe wie: akku = akku -1

print('Handy ist aus. Bitte laden.')

'''
Die größte Gefahr: Die Endlosschleife.

Wenn du die Bedingung nie auf False setzt (oder den Zähler nie verringerst), läuft der Code ewig weiter und du musst das Programm mit
Strg+C(im Terminal) oder dem "Stop"-Button in deiner IDE abwürgen.
'''

### Lektion 3: Schleifenkontrolle: break und continue
'''
Manchmal musst du in den Lauf einer Schleife eingreifen. Dafür gibt es zwei Schlüsselwörter:

 - break:    Der Notausgang. Bricht die Schleife sofort und komplett ab.
 - continue: Der Überspringer: Beendet den aktuellen Durchlauf und springt sofort zum nächsten.
'''

print('\n--- break und continue ---')

## Wir suchen nache einer "verbotenen" Zahl und überspringen gerade Zahlen

for i in range(1, 11):
    if i % 2 == 0:
        continue        # Überspringt den Rest des Codes und geht zur nächsten Zahl (5, 7, 9...)

    if i == 7:
        print(f'Zahl {i} gefunden! Abbruch der Suche.')
        break           # Bricht die gesamte Schleife ab

    print(f'Überprüfe Zahl: {i}')


### Lektion 4: Verschachtelte Schleifen (Nested Loops)
'''
Eine Schleife innerhalb einer Schleife. Die innere Schleife wird für jeden Durchlauf der äußeren Schleife komplett ausgeführt. 
(Wichtig für Tabellen oder Matrizen).
'''

print('\n--- Das kleine Einmaleins (Ausschnitt) ---')
for i in range(1, 11):                              # Äußere Schleife (Zeilen)
    for j in range(1, 11):                          # Innere Schleife (Spalten)
        print(f'{i} * {j} = {i*j}', end=' ')        # end=' ' verhindert den Zeilenumbruch
    print()                                         # Ein einfacher print() am Ender der äußeren Schleife erzeugt die neue Zeile