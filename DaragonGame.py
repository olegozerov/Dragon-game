import random


class Hiroes:

    """Тут мы плодим наших героев"""

    def __init__(self, hp=0, defence=0, strong=0, weapon=0, shield=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
        self._shield = shield        #  shield - щит


    def modify_health(self, parametr):
        if self._hp > 0:
            if parametr > 0:
                self._hp += parametr
                return self._hp
            else:
                self._hp += parametr
                return self._hp

    def hit(self):
        return self._strong + self._weapon


class Dragon(Hiroes):

    """Дракон обладает следующими характреистиками: hp, defence, strong, weapon"""

    def __init__(self, hp=2000, defence=120, strong=150, weapon=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие

    def __str__(self):
        return f"Характеристики дрокона: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n"

                
class Knight(Hiroes):

    """Рыцарь обладает следующими характреистиками: hp, defence, strong, weapon, shield"""

    def __init__(self, hp=1000, defence=100, strong=120, weapon=250, shield=150):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
        self._shield = shield        #  shield - щит
    
    def __str__(self):
        return f"Характеристики дрокона: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n \
                       shield = {self._shield}\n"


class Damage():

    """Описаны методы насенного урона в зависомости от персонажа игры"""

    dragon = Dragon()
    knight = Knight()

    def knight_damage(self):
        if random.random() < 0.75:
            self.damage = self.knight.hit() - self.dragon._defence
            self.dragon._hp -= self.damage
            print(f"\nДракон получил {self.damage} едениц урона \n")
            print(self.dragon)
        else:
            print(f"\nРыцарь не смог нанести урон дракону \n")
            print(self.dragon)

    def dragon_damage(self):
        if random.random() < 0.50:
            self.damage = self.dragon.hit() - self.knight._defence
            self.knight._hp -= self.damage
            print(f"\nРыцарь получил {self.damage} едениц урона \n") 
            print(self.knight)
        else:
            print(f"\nДракон не смог нанести урон рыцарю \n")
            print(self.knight)



class DragonGame:

    """Здесь происходит сражение"""

    while True:
        break    




d = Damage()

d.knight_damage()
d.dragon_damage()
print(d.dragon)
print(d.knight)