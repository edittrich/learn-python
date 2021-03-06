name = input('Bitte gib Deinen Namen ein: ')
print('Hello, ' + name + '!\n')

zahl = eval(input('Bitte gib eine Zahl größer als 100 zum Verdoppeln ein: '))

while zahl != 0:
    if zahl > 100:
        print(zahl*2)
    else:
        print('Die Zahl ist nicht größer als 100!')
    zahl = eval(input('Bitte gib eine Zahl größer als 100 zum Verdoppeln ein: '))

print('\nAuf Wiedersehen, ' + name + '!')
