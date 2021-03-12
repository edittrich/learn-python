from summen import gesamtsumme

name = input('Bitte gib Deinen Namen ein: ')
print('Hello, ' + name + '!\n')

fahrzeug1 = {"marke": "vw", "modell": "golf", "baujahr": 2012, "preis": 5000}
fahrzeug2 = {"marke": "renault", "modell": "clio", "baujahr": 2011, "preis": 6000}
fahrzeuge = [fahrzeug1, fahrzeug2]

gesamtpreis = 0
for fahrzeug in fahrzeuge:
    print(fahrzeug["preis"])
    gesamtpreis = gesamtpreis + (fahrzeug["preis"])
print('Der Gesamtpreis aller Fahrzeuge ist', gesamtpreis, '€')

print(gesamtsumme())
print(gesamtsumme(10))
print(gesamtsumme(100))

zahl = eval(input('Bitte gib eine Zahl größer als 100 zum Verdoppeln ein: '))

while zahl != 0:
    if zahl > 100:
        print(zahl*2)
    else:
        print('Die Zahl ist nicht größer als 100!')
    zahl = eval(input('Bitte gib eine Zahl größer als 100 zum Verdoppeln ein: '))

print('\nAuf Wiedersehen, ' + name + '!')

