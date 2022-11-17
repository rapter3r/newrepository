from cw.character import Character


class Berserk(Character):
    max_health = 100

    def __init__(self, name='', health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)
        self.max_health = self.health

    def count_additional_damage(self):
        return self.damage * (1 - self.health / self.max_health)

    def attack(self, target):
        target.take_damage(self.damage + self.count_additional_damage())