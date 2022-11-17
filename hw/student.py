from datetime import datetime


class Student:
    name = ''
    group = 'C29153'
    old = 2010
    damage = 3
    defense = 0
    health = 100

    def __init__(self, name='', health=100, damage=3, defense=0, group='C29153'):
        self.name = name
        self.group = group
        self.damage = damage
        self.defense = defense
        self.health = health

    def get_age(self, old=datetime.date.today().year-2008):
        self.old = old

    def __str__(self):
        return f' == {self.name} ==\n' \
               f'Health: {self.health}\n'\
               f'Damage: {self.damage}\n' \
               f'Defense: {self.defense}\n' \
               f'Old: {self.old}\n' \
               f'Group: {self.group}\n' \

    def take_damage(self, damage=0):
        self.health -= max(damage, 0)

    def attack(self, target):
        target.take_damage(self.damage)


