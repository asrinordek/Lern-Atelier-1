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

for franz in Vocis:
    print('Übersetze dieses Wort: ')
    print(franz)

    antwort = input('Deutsch: ')

    if antwort == Vocis[franz]:
        print('Richtig!')
     
    else: 
        print("Falsch ")
        print("Richtig wäre:", Vocis[franz])

##Count = 'Richitg' +1


print('Du hast', len(Vocis), 'richtig')

