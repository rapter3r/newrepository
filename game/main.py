from berserk import Berserk
from cw.character import Samurai

player1 = Berserk(name='Кратос', damage=10)
player2 = Samurai(name='Тор', damage=10)

print(f'{player1}\n')
print(f'{player2}\n')

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    player2.attack(player1)

    print(f'{player1}\n')
    print(f'{player2}\n')