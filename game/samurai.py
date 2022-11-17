from cw.character import Character

class Samurai(Character):
    combo = 0
    max_combo = 5

    def __int__(self, name='', health=100, damage=1, defense=0, max_combo=5):
        Character.__init__(self, name, health, damage, defense)
        self.max_combo = (self.combo +1) % self.max_combo