### Aufgaben zur Festigung von Schleifen

'''
Kleiner Tip für die Aufgaben: Nutze wenn nötig, input() und Typumwandlung (int()), um dein Vorwissen zu verknüpfen,

Aufgabe 1: Der FizzBuzz-Klassiker (for, if/elif, continue)
Iteriere mit einer for-Schleife von 1 bis 30.

 - Ist die Zahl durch 3 teilbar, print "Fizz".
 - Ist die Zahl durch 5 teilbar, printe "Buzz".
 - ist die Zahl durch beide teilbar, printe "FizzBuzz".
 - Ist die Zahl durch keines teilbar, printe einfach die Zahl.
    (Tipp: Prüfe die Bedingung für "beide teilbar" als allererstes!)
'''


## Lösung Aufgabe 1

#print('Lösung Aufgabe 1')
#for i in range(1, 31):
#    if i % 3 == 0:
#        print('Fizz')
#    elif i % 5 == 0:
#        print('Buzz')
#    elif i % 3 == 0 and i % 5 == 0:
#        print('FizzBuzz')
#    else:
#        print(i)


'''
Aufgabe 2: Das Passwort-Portal (while, break, Bedingungen)
Schreibe ein Skript, das den Nutzer nach einem Passwort fragt.

    - Das korrekte Passwort ist "sicherheit123".
    - Der nutzer hat maximal 3 Versuche.
    - Nutze eine while-Schleife und ein Zähler.
    - Bei richtiger Eingabe: Printe 'Zugang gewährt' und brich die Schleife mit break ab.
    - Bei flascher Eingabe: Printe 'Falsche, noch X Versuche"
    - Wenn die Verscuhe aufgebracuht sind, printe 'Konto gesperrt'.
'''


## Lösung Aufgabe 2

#print('\n--- Lösung Aufgabe 2 ---')
#passwort = 'sicherheit123'
#versuche = 3

#while versuche > 0:
#    passworteingabe = input('Geben Sie das Passwort ein: ')
#    if passwort == passworteingabe:
#        print('Zugang gewährt')
#    elif passwort != passworteingabe:
#        versuche -= 1
#        print(f'Falsch noch {versuche} Versuche')
#    if versuche == 0:
#        print('Konto gesperrt')


'''
Aufgabe 3: Der Vokal-Filter (for, String-Methoden, continue)
Nimm den String: satz = 'Programmieren lernt man am besten durch tun'
Iteriere durch jedes Zeichen des Strings.

    - Wenn das Zeichen ein Vokal (a, e, i, o, u) ist, überspringe es (continue).
    - Wenn das Zeichen ein Leerzeichen ist, ersetzt es durch einen "_" (Tipp: Nutze print(..., end=' ')) oder samme es in einem neuen String).
    - Alle anderen Zeichen sollen normal ausgegeben werden.
'''
## Lösung Aufgabe 3

print('\n--- Lösung Aufgabe 3 ---')

satz = 'Programmieren lernt man am besten durch tun'

for zeichen in satz:
    if zeichen in "aeiou":
        continue
    if zeichen == ' ':
        zeichen = '_'

    print(zeichen, end='')

print()

## Alternativlösung zu Aufgabe 3

satz = 'Programmieren lernt man am besten durch tun'
neuer_satz = ''     # Ein leerer String, den wir nach und nach füllen

for zeichen in satz:
    if zeichen in 'aeiou':
        continue

    if zeichen == ' ':
        zeichen = '_'

    neuer_satz = neuer_satz + zeichen

print(neuer_satz,' (Alternativlösung)')