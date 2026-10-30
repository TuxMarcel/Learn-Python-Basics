'''
### Zahlen und Arithmetik ###

Willkommen zur nächsten Etappe deiner Python-Journey! In dieser Datei behandeln wir numerischen Datentypen Intergers und Floats sowie alle wichtigen
arithmetischen Operatoren.

Schon wie in der 00Basic.py ist Ausführbarercode Auskommentiert mit genau einem "#" vor dem code. Entferne das Zeichen um den Code auszuführen. 
Vergiss nicht neue zu setzen wenn du weiter liest.
'''

#######################################################################################################################################################

### Lektion 1: Datentypen - Ganzzahlen (Integer) & Kommazahlen (Float) ###
'''
Python unterscheidet bei Zahlen zwei wesentlichen Typen:

    - Integer(int): Ganzzahlen ohne Nachkommastelle (positiv, negativ oder 0)
    - Float(float): Gleitkommazahl mit Nachkommastelle. Wichtig: In Python wird Dezimaltrenner immer ein Punkt (.) statt eines Kommas verwendet.
                    Sobald eine Zahl einen Punkt hat (selbst .0), gilt als Float.
    
    - type() :      Mit der eingebauten Funktion type() kannst du prüfen, welchen Datentyp eine Zahl hat. 
'''

print('--- Lektion 1 ---')
ganzzahl = 50
kommazahl = 50.5
float_ganzzahl = 50.0

print("Ganzzahl:", ganzzahl, "| Typ:", type(ganzzahl))
print("Kommazahl:", kommazahl, "| Typ:", type(kommazahl))
print("Float mit .0:", float_ganzzahl, "| Typ:", type(float_ganzzahl))


### Lektion 2: Grundrechenarten (+,-,*,/) ###
'''
Python unterstützt alle Standard-Rechenarten: Addition(+), Subtraktion(-), Multiplikation(*) und Division(/)

    - Besonderheit der Division (/): Eine normale Division ergibt in Python immer einen float - selbst wenn das Ergebnis eine glatte Zahl ist. 
'''
print('\n--- Lektion 2 ---')
print('Addition (10 + 2)=', 10+2)
print('Subtraktion (10 - 2)=', 10-2)
print('Multiplikation (10 * 2)=', 10*2)

## Division liefert immer einen Float zurück:
print('Division (10 / 2)=', 10 / 2, '| Type:', type(10 / 2)) 


### Lektion 3: Spezielle Operatoren - Modulo (%) & Potenzierung (**) ###
'''
- Modulo-Operatoren (%): Berechnet den Rest einer mathematischen Division.
    - Einsatzbereich: Sehr nützlich, um zu prüfen, ob eine Zahl gerade oder ungerade ist. Bei geraden Zahlen ist x % 2 immer = 0 bei ungeraden 1

- Potenz-Operator(**): Rechnet eine Zahl hoch eine andere (Basis ** Exponent)
    - Trick: Mit ** 0.5 kannst du dir Quadratwurzel einer Zahl ziehen.
'''

print('\n--- lektion 3 ---')

## Modulo: Rest der Division
print('10 % 3 (10 geteilt durch 3 ist 3, Rest 1):', 10 % 3)
print('10 % 2 (Gerade Zahl --> rest 0):', 10 % 2)
print('11 % 2 (Ungerade Zahl --> Rest 2):', 11 % 2)

## Potenzierung
print('10 ** 2 (10²):', 10 ** 2)
print('2 ** 3 (2³):', 2 ** 3)
print('16 ** 0.5 (Quadratwurzel aus 16):', 16 ** 0.5, '| Type:', type(16 ** 0.5))


### Lektion 4: Rechenregeln & Automatischer Typwechsel
'''
- Mathematische Rangfolge: Auch in Python gilt Punkt- vor Strichrechnung (* und / binden stärker als + und -)
  Mit Klammern () kannst du die Reihenfolge gezielt steuern.

- Mischen vin Integers und Floats: Verknüpfst du in einer Rechnung einen int mit einem float, ist das Endergebnis automatisch immer ein float.
'''

print('\n--- Lektion 4 ---')

# Punkt- vor Strichrechnung vs. Klammern

print('Ohne KLammern (2 + 1 * 3)=', 2 + 1 * 3)
print('Mit KLammern ((2 + 1) * 3)=', (2 + 1) * 3)

# Mischen von int und float

ergebnis_gemischt = 5.2 * 3
print("int * float (5.2 * 3)=", ergebnis_gemischt, '| Type:', type(ergebnis_gemischt))