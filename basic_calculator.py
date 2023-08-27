'''
 Calcolatrice
'''
from math import sqrt

hello_message = '''
Benvenuti al programma calcolatrice: funzioni disponibili
1 - addizione
2 - sottrazione
3 - moltiplicazione
4 - divisione
5 - esponenziale
6 - radice quadrata
7 - chiudi calcolatrice
'''

while True:
    print(hello_message)

    action = input('Inserisci numero dell\'operazione: ')

    if action == '1':
        print('\nHai scelto addizione\n')
        a = float(input('primo numero: '))
        b = float(input('secondo numero: '))
        result = a+b
        print('risultato:' + str(result))

    elif action == '2':
        print('\nHai scelto sottrazione\n')
        a = float(input('primo numero: '))
        b = float(input('secondo numero: '))
        result = a-b
        print('risultato:' + str(result))

    elif action == '3':
        print('\nHai scelto moltiplicazione\n')
        a = float(input('primo numero: '))
        b = float(input('secondo numero: '))
        result = a*b
        print('risultato:' + str(result))

    elif action == '4':
        print('\nHai scelto divisione\n')
        a = float(input('primo numero: '))
        b = float(input('secondo numero: '))
        result = a/b
        print('risultato:' + str(result))

    elif action == '5':
        print('\nHai scelto esponenziale\n')
        a = float(input('primo numero: '))
        b = float(input('secondo numero: '))
        result = a**b
        print('risultato:' + str(result))

    elif action == '6':
        print('\nHai scelto radice quadrata\n')
        a = float(input('radicando: '))
        result = sqrt(a)
        print('risultato:' + str(result))

    elif action == '7':
        print('Chiudo la calcolatrice')
        break

    new_action = input('Continuare? S-N: ')
    if new_action == 'S' or new_action =='s':
        print('Torno al menù')
        continue
    else:
        print('Esco')
        break
