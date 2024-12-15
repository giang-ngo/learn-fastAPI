from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *


def battle(e: Enemy, e2: Enemy):
    e.talk()
    e2.talk()

    while e.health_points > 0 and e2.health_points > 0:
        print('-----------------------------------')
        e.special_attack()
        e2.special_attack()

        print(f'{e.get_type_of_enemy()}: {e.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')

        e2.attack()
        e.health_points -= e2.attack_damage
        e.attack()
        e2.health_points -= e.attack_damage
    print('-----------------------------------')

    if e.health_points > 0:
        print(f'{e.get_type_of_enemy()} wins!')
    else:
        print(f'{e2.get_type_of_enemy()} wins!')


def hero_battle(hero: Hero, enemy: Enemy):
    while hero.health_points > 0 and enemy.health_points > 0:
        print('-----------------------------------')

        print(f'Hero: {hero.health_points} HP left')
        print(f'{enemy.get_type_of_enemy()}: {enemy.health_points} HP left')

        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage
    print('-----------------------------------')

    if hero.health_points > 0:
        print(f'Hero wins!')
    else:
        print(f'{enemy.get_type_of_enemy()} wins!')


zombie = Zombie(10, 1)
ogre = Ogre(20, 3)
hero = Hero(10, 10)
weapon = Weapon('Sword', 5)
hero.weapon = weapon
hero.equip_weapon()

# battle(zombie, ogre)
hero_battle(hero, zombie)
hero_battle(hero, ogre)
