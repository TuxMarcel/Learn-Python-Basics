'''
In dieser Datei wird das Thema bedigungen und verzweigungen Beigebracht.

Wozu braucht man Bedingungen?

Bisher laufen die Skripte von oben nach unten, Zeile für Zeile. Ein Programm trifft damit keine Entscheidungen. Mit Verzweigungen kann Code 
abhängig von einer Bedingung unterschiedliche Wege nehmen: Passwort richtig oder falsch, Wert größer oder kleiner, Datei vorhanden oder nicht.
Das ist die Grundlage für jedes Programm, das Sie später schreiben, von Admin-Skripten bis zu Security-Tools. 
'''

### Die if Anweisung

alter = 20

if alter >= 18:
    print("Volljährig")

'''
Drei Dinge sind hier wichtig:
    
    1. Nach der Bedingung steht ein Doppelpunkt. Den vergessen Anfänger ständig.

    2. Der eingerückte Block darunter gehört zum if. Python erkennt zusammengehörigen Code allein über Einrückungen, nicht über Klammern wie 
       andere Sprachen. 
    
    3. Die Bedingung alter >= 18 ergibt True oder False. Genau die Booleans aus Kapitel 04 entscheiden hier, ob der Block läuft oder übersprungen wird.
       if heißt wörtlich: führe den Block aus, wenn die Bedingung True ist.
'''


### else: der Else-Fall
##  Läuft der if-Block nicht, passiert sonst nichts. Mit else definierst du den Gegnzweig:

alter = 15

if alter >= 18:
    print('Volljährig')
else:
    print('Minderjährig')

'''
Genau einer der beiden Blöcke läuft immer. Beachten Sie: elde kommt keine Bedingung, nur den Doppelpunkt.
'''

### elif: mehrere Fälle
'''
Für mehr als zwei Fälle gibt es elif (Kurzform von else if). Python prüft von oben nach unten und läuft beim ersten zutreffenden Zweig hinein,
alle weiteren werden übersprungen.
'''

punkte = 84

if punkte >= 91:
    print('Note 1')
elif punkte >= 81:
    print('Note 2')
elif punkte >= 66:
    print('Note 3')
elif punkte >= 50:
    print('Note 4')
else:
    print('Nicht bestanden')

'''
Bei 84 Punkten ist punkte >= 90 False, also weiter zur näcshten Prüfung. punkte >=80 ist True, es kommt 'Note 2' heraus. Der Rest wird ignoriert,
obwohl 84 auch größer als 70 ist. Deshalb ist die Reihenfolge bei elif wichtig: von der strengsten Bedingung nach unten,
'''

### Vergleichsoperatoren
'''
Operator | Bedeutung        | Beispiel | Ergebnis
--------------------------------------------------
==       | gleich           | 5 == 5   | True
-------------------------------------------------- 
!=       | ungleich         | 5!= 3    | True
--------------------------------------------------
>        | größer           | 3 > 5    | False
--------------------------------------------------
<        | kleiner          | 3 < 5    | True
--------------------------------------------------
>=       | größer geleich   | 5 >= 5   | True
--------------------------------------------------
<=       | kleiner gleich   | 3 <= 5   | True
--------------------------------------------------
''' 
'''
Der klassische Anfängerfehler: ein einzelnes '=' ist eine Zuweisung (alter = 18), zwei '==' sind ein Vergleich (alter = 18). In einer if-Bedingung
gehört immer '=='.

Achtung bei Strings: 'Admin' == 'admin' ist False, Python unterscheidet Groß und Kleinschreibung.
Typisch für spätere Login-Skripte.
'''

### Bedingungen kombinieren: and, or, not 

##  Hier kommt das Wissen aus 04booleans_und_logik direkt zum Einsatz. Bedingungen lassen sich verknüpfen:

benutzer = 'admin'
passwort = 'sicher123#'

if benutzer == 'admin' and passwort == 'sicher123#':
    print('Login erfolgreich')
else:
    print('Computer sagt Neeein')

'''
° and: beide Bedingungen müssen True sein.

° or:  mindestens eine muss True sein.

° not: dreht das Ergebnis um, True wird False.
'''

## Beispiele mit or und not:

uhrzeit = 22

if uhrzeit < 6 or uhrzeit >= 22:
    print('Nachts')

if not uhrzeit < 6:
    print('Keine Nachtanfangsstunde')

'''
Für Übersicht in komplexen Bedingungen dürfen Sie Klammern setzen: 'if (alter >= 18) and (alter <= 67):'. Python kann auch ohne,
klammern machen es lesbarer.
'''

### Eingaben Prüfen
'''
Jetzt kombinieren wir Verzweigungen mit 03input&typumwandlung. input liefert immer einen String, deshalb die Typumwandlung mit int.
'''

eingabe = input('Temperatur in Grad: ')
temperatur = int(eingabe)

if temperatur >= 30:
    print('Heiß')
elif temperatur >= 15:
    print('Angenehm')
elif temperatur >= 0:
    print('Kühl')
else:
    print('Gefriert')

## Teste ruhig mehrer Werte durch.

## Noch ein Beispiel mit Strings, wie er Ihnen in der Praxis begegnen wird.

status = input('Dienststatus (aktiv/inaktiv): ')

if status == 'aktiv':
    print('System läuft')
elif status == 'inaktiv':
    print('System gestoppt')
else:
    print('Invalide Eingabe (Computer sagt Nein)')


### Verschachtelte Bedingungen
'''
Ein if kann innerhalb eines anderen if stehen. Nutzen Sie sparsam, weil es schnell unlesbar wird.
'''

benutzer = 'admin'
eingeloggt = True

if benutzer == 'admin':
    if eingeloggt:
        print('Vollzugriff')
    else:
        print('Bitte Einlogen. (Computer sagt Nein!)')

'''
Oft ist die flache Variante mir and sauber: 'if benuter == 'admin' and eingeloggt:.

Merkpunkte für die Wissensdatenbank

- If, elif, else steuern, Welcher Codeblock läuft.
- Python erkennt Blöcke über Einrückung, nicht über Klammern.
- Doppelpunkte nicht vergessen.
- = weist zu, == vergleicht.
- elif wird von oben nach unten geprüft, der erste Treffer gewinnt.
- and, or, not verknüpfen Bedingungen.
- input liefert Strings, bei Zahlvergleich mit int oder float umwandel. 
'''