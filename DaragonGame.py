import random


class Hiro:

    """Тут мы плодим наших героев"""

    def __init__(self, hp=0, defence=0, strong=0, weapon=0, shield=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
        self._shield = shield        #  shield - щит

    def health_tracking(self):
        if self._hp < 0:
            self._hp = 0
            return self._hp
        else:
            return self._hp

    def hiroe_lose(self):
        if self._hp <= 0:
            print(f"\n{self.__repr__()} умер \n")

    def hit(self):
        return self._strong + self._weapon


class Dragon(Hiro):

    """Дракон обладает следующими характреистиками: hp, defence, strong, weapon"""

    def __init__(self, hp=400, defence=120, strong=150, weapon=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие

    

    def __str__(self):
        return f"Характеристики дрокона: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n"

    def __repr__(self):
        return f"{'Дракон'}"
                
class Knight(Hiro):

    """Рыцарь обладает следующими характреистиками: hp, defence, strong, weapon, shield"""

    def __init__(self, hp=70, defence=100, strong=120, weapon=250, shield=150):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
        self._shield = shield        #  shield - щит

    def equip_shield(self):
        if self._defence <= 100:
            self._defence += self._shield
            print("\nРыцарь надел свой щит \n")
        else:
            pass


    def remove_shield(self):
        if self._defence > 100:
            self._defence -= self._shield
            print("\nРыцарь снял свой щит \n")
        else: 
            pass

    def pass_move(self):
        pass
    
    def __str__(self):
        return f"Характеристики дрокона: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n \
                       shield = {self._shield}\n"

    def __repr__(self):
        return f"{'Рыцарь'}"

class Damage():

    """Описаны методы насенного урона в зависомости от персонажа игры"""

    dragon = Dragon()
    knight = Knight()

    def knight_damage(self):
        if self.knight._hp > 0:
            if random.random() < 0.75:
                self.damage = self.knight.hit() - self.dragon._defence
                self.dragon._hp -= self.damage
                print(f"\nРыцарь нанес удар и дракон получил {abs(self.damage)} единиц урона")
                print(f"И теперь у дракона осталось {self.dragon.health_tracking()} единиц здоровья \n")
                self.dragon.hiroe_lose()
            else:
                print(f"\nРыцарь не смог попасть и нанести урон дракону")
                print(f"У дракона все еще {self.dragon.health_tracking()} единиц здоровья \n")


    def dragon_damage(self):
        if self.dragon._hp > 0:
            if random.random() < 0.50:
                self.damage = self.dragon.hit() - self.knight._defence
                self.knight._hp -= self.damage
                print(f"\nДракон нанес удар и рыцарь получил {abs(self.damage)} единиц урона") 
                print(f"И теперь у рыцаря осталось {self.knight.health_tracking()} единиц здоровья \n")
                self.knight.hiroe_lose()
            else:
                print(f"\nДракон проспал свой ход")
                print(f"У рыцаря все еще {self.knight.health_tracking()} единиц здоровья \n")


class DragonGame:

    """Здесь происходит сражение"""

    damage = Damage()
  
    while True:
        
        action = input("Пожалуйста введите действие героя: attack, pass, defence \n")

        if action == "attack":
            damage.knight.remove_shield
            if damage.dragon._hp > 0:
                damage.knight_damage()
            else:
                break
        elif action == "pass":
            damage.knight.pass_move()
        elif action == "defence":
            damage.knight.equip_shield()
        if damage.knight._hp > 0:
            damage.dragon_damage() 
        else:
            break
        


d = Damage()


"""d.dragon_damage()
d.knight
d.dragon_damage()
d.knight
print(d.knight)"""

"""d.knight_damage()
d.dragon
d.knight_damage()
d.dragon
print(d.dragon)"""