class Paladin:
    def __init__(self, name, level, oath):
        self.name = name
        self.level = level
        self.oath = oath

paladins = [
    Paladin('René', 5, 'Ancients'),
    Paladin('Radko', 7, 'Glory'),
    Paladin('Kat', 4, 'Vengeance')
]

sorted_paladins = sorted(paladins, key=lambda x: x.level)


for paladin in sorted_paladins:
    print(paladin.name, paladin.level, paladin.oath)