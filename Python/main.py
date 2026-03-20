#print('Hallo Asrin!') 
#print('Mein erstes Python Programm läuft!')

#name = input('Wie heisst du?')

#print('Hallo', name)
#print('Willkommen bei Python!')

Vocis = {
    'le mal du pays': 'Heimweh',
    'patient': 'geduldig',
    'une annonce': 'eine Anzeige',
    'aimer': 'mögen'
}
count = 0
fehler = [] #Liste für Falsche Antworten

for franz in Vocis:
    print('Übersetze dieses Wort: ')
    print(franz)

    antwort = input('Deutsch: ')

    if antwort == Vocis[franz]:
        print('Richtig!')
        count += 1
     
    else: 
        print("Falsch ")
        print("Richtig wäre:", Vocis[franz])
        fehler.append(franz) #Falsche Wörter werden gespeichert

#fehler wiederholen
print ('\---Fehler wiederholen---')

for franz in fehler:
    print('Übersetze dieses Wort:')
    print(franz)

    antwort = input('Deutsch')

    if antwort == Vocis[franz]
    print ('jetzt Richtig!')
    count +=  1

else   



print('Du hast', count, 'von', len(Vocis), 'richtig')



