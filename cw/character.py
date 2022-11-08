class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name='', health=100, damage=1, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return f' == {self.name} ==\n' \
               f' Здоровье: {self.health}\n' \
               f' Урон: {self.damage}\n' \
               f' Защита: {self.defence}'

    def take_damage(self, damage=0):
        self.health -= max(damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)

    def is_alive(self):
        return self.health > 0