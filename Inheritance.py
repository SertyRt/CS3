class Paladin:
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp

    def attack(self):
        return f"{self.name} attacks with his melee weapon!"


class OathOfGlory(Paladin):
    def __init__(self, name, level, hp):
        super().__init__(name, level, hp)
        self.spell = "Cure Wounds"

    def use_spell(self):
        return f"{self.name} casts {self.spell}!"