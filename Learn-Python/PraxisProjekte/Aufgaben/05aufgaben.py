'''
Übungsaufgaben nach dem durcharbeiten der 05bedingungen&verweigungen.py
-------------------------------------------------------------------------


Aufgabe 1. Schreibe ein Skript, das eine Zahl über input einliest und ausgibt, ob sie positiv, negativ oder null ist.
'''

### Lösung Aufgabe 1

zahl = input('Gib eine Zahl ein: ')
eingabe = float(zahl)

if eingabe > 0:
    print('Positiver Wert')
elif eingabe < 0:
    print('Negativer Wert')
elif eingabe == 0:
    print('0 ist Positiv und Negativ')


'''
Aufgabe 2: Baue einen Mini-Login: frage Benutzername und Passwort ab, gebe 'Zugriff gewährt'nur bei korrekten Kombinationen aus,
           sonst 'Zugriff Verweigert'.
'''

benutzername = 'marcel'
passwort = 'Superpw123'

eingabe_benutzername = input('Gebe deinen Benutzernamen ein: ')
eingabe_passwort = input('Gebe dein Passwort ein: ')

if eingabe_benutzername == benutzername and eingabe_passwort == passwort:
    print('Zugriff gewährt')
else:
    print('Zugriff verweigert')


'''
Aufgabe 3: Erweiter die Temperaturausgabe: bei unter 0 soll zusätzlich 'Wasser gefriert' erscheinen,
           bei 100 oder darüber 'Wasser kocht'
'''

eingabe = input("Temperatur in Grad: ")
temperatur = int(eingabe)


if temperatur >= 100:
    print('Wasser kocht')
elif temperatur >= 35:
    print("Heiß")
elif temperatur >= 20:
    print("Angenehm")
elif temperatur >= 5:
    print("Kühl")
elif temperatur >= 0:
    print('Wasser gefriert')
