'''
### ibooleans & logik ###

Willkommen zur nächsten Etappe deiner Python-Journey! In dieser Datei behandeln wir booleans und logik in Python.

Schon wie in der 00Basic.py ist Ausführbarercode Auskommentiert mit genau einem "#" vor dem code. Entferne das Zeichen um den Code auszuführen. 
Vergiss nicht neue zu setzen wenn du weiter liest.
'''

### Lektion 1: Der Datentyp Boolean (True & False) ###
'''
Ein Boolean (bool) kann in Python genau zwei Werte annehmen: True (Wahr) oder False (Falsch).

    - Wichtig: Die ersten Buchstaben müssen immer großgeschrieben werden. Schreibst du true oder false klein, erkennt Python das nicht als Boolean, sondern 
      sucht nach einer Variable und wirft einen Fehler.
'''

print('--- Lektion 1 ---')
ist_online = True
ist_admin = False

print("Wert von ist_online:", ist_online, "| Typ:", type(ist_online))
print("Wert von ist_admin:", ist_admin, "| Typ:", type(ist_admin))


### Lektion 2: Vergleichsoperatoren ( == ; != ; > ; < ; >= ; <= ) ###
'''
Vergleichoperatoren vergleichen zwei Werte miteinander und liefern als Ergebnis einen Boolean (True oder False) zurück.

    - ==:    Prüft aug Gleichheit. Achtung: Ein einzelnes = weist einer Variable einen Wert zu, zwei == vergleichen zwei Werte.
    - !=:    Prüft auf Ungleichheit.
    - >/<:   Größer als / Kleiner als 
    - >=/<=: Größer-gleich / Kleiner-gleich
'''

print("\n--- Lektion 2 ---")
a = 10
b = 5

print('Ist a gleich b? (10 == 5):', a == b)
print('Ist a ungleich b? 10 != 5', a != b)
print('Ist a goeßer als b? (10 > 5):', a > b)
print('Ist a kleiner als b? (10 < 5):', a < b)
print('Ist b kleiner gleich 5? (5 <= 5):', b <= 5)


### Lektion 3: Logische Operatoren (and, or, not)
'''
Mit logischen Operatoren verknüpfst du mehrere Wahrheitsprüfungen.

 - and: Gibt nur dann True zurück, wenn alle verknüpften Bedingungen erfüllt sind.
 - or:  Gibt bereits True zurück, sobald mindestens eine Bedingung erfüllt ist.
 - not: Kehrt den Wahrheitswert um (True wird zu False, False wird zu True).
'''

print('\n--- Lektion 3 ---')
alter = 20
hat_führerschein = True 

## and: Beide Bedingungen müssen True sein
kann_auto_fahren = (alter >= 18) and hat_führerschein
print("Darf Auro fahren? (alter >= 18 and hat_führerschein):", kann_auto_fahren)

## or: Mindestens eine Bdedingung muss True sein
hat_ticket = False
ist_ehrengast = True
darf_rein = hat_ticket or ist_ehrengast
print('Darf hinein? (hat_ticket or ist_ehrengast):', darf_rein)

## not: Dreht True/False um
ist_eingeloggt = False
print('Ist nicht eingeloggt? (not ist_eingeloggt):', not ist_eingeloggt)


### Lektion 4: Verkettete Vergleiche ###
'''
In Python kannst du Bereichsprüfungen direkt hintereinanderstellen, zum Beispiel um zu prüfen, ob ein Wert zwischen zwei Grenzen liegt.
'''

print('\n--- Lektion 4 ---')
alter = 25

## Prüft direkt, ob alter zwischen 18 und 65 liegt
im_arbeitsalter = 18 <= alter <= 65
print('Liegt Alter (25) zwichen 18 und 65?:', im_arbeitsalter)
