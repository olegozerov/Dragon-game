import random
 
class Hiro:
 
    """Тут мы плодим наших героев"""
 
    def __init__(self, hp=0, defence=0, strong=0, weapon=0, shield=0, potion=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
        self._shield = shield        #  shield - щит
        self._potion = potion        #  potion - зелье
 
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
 
    """Дракон обладает следующими характеристиками: hp, defence, strong, weapon"""
 
    def __init__(self, hp=900, defence=120, strong=150, weapon=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
 
    def __str__(self):
        return f"Характеристики дракона: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n"
 
    def fire_ball(self):
        return self._strong * 2
 
    def __repr__(self):
        return f"{'Дракон'}"
                
class Knight(Hiro):
 
    """Рыцарь обладает следующими характеристиками: hp, defence, strong, weapon, shield"""
 
    HAS_SHIELD = False
 
    def __init__(self, hp=400, defence=100, strong=120, weapon=250, shield=150, potion=(2, 500)):
        self._hp = hp                                           #  hp - жизненная энергия, запас здоровья
        self._defence = defence                                 #  defence - защита
        self._strong = strong                                   #  srong - сила
        self._weapon = weapon                                   #  weapon - оружие
        self._shield = shield                                   #  shield - щит
        self._potion_butle, self._potion_portion = potion       #  potion_butle - количество бутылочек с зельем
                                                                #  potion_portion - порция зелья
 
    def equip_shield(self):
        if Knight.HAS_SHIELD == False:
            self._defence += self._shield
            Knight.HAS_SHIELD = True
            print(f"\nРыцарь надел свой щит, его защита теперь {self._defence} единиц \n")
            return Knight.HAS_SHIELD
        else:
            pass
 
    def remove_shield(self):
        if self._hp > 0:
            if Knight.HAS_SHIELD == True:
                self._defence -= self._shield
                Knight.HAS_SHIELD = False
                print(f"\nРыцарь снял свой щит, его защита теперь {self._defence} единиц \n")
                return Knight.HAS_SHIELD
            else:
                pass
 
    def get_potion(self):
        if self._potion_butle > 0:
            self._potion_butle -= 1
            print(f'Осталось бутылочек с зельем {self._potion_butle}')
            self._hp += self._potion_portion
            return self._hp
        else:
            print('Бутылочки с зельем закончились')
  
    def __str__(self):
        return f"Характеристики дракона: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n \
                       shield = {self._shield}\n \
                       potion = {self._potion}\n"
 
    def __repr__(self):
        return f"{'Рыцарь'}"
 
class Damage():
 
    """Описаны методы настенного урона в зависимости от персонажа игры"""
    LOOP_ = True

    dragon = Dragon()
    knight = Knight()
    
 
    def dragon_damage_whith_fire_ball(self):
        if self.knight.HAS_SHIELD == False:
            self.knight._hp -= self.dragon.fire_ball()
            print(f"\nДракон нанес удар огненным шаром и рыцарь получил {self.dragon.fire_ball()} единиц урона") 
            print(f"И теперь у рыцаря осталось {self.knight.health_tracking()} единиц здоровья \n")
            self.knight.hiroe_lose()
        else:
            print(f"\nДракон изверг огонь, но не смог нанести урон. Рыцарь был под щитом")
 
    def dragon_damage_whithout_fire_ball(self):
        if self.dragon.hit() > self.knight._defence:
            self.knight._hp -= self.dragon.hit() - self.knight._defence
            print(f"\nДракон нанес удар и рыцарь получил {self.dragon.hit() - self.knight._defence} единиц урона") 
            print(f"И теперь у рыцаря осталось {self.knight.health_tracking()} единиц здоровья \n")
            self.knight.hiroe_lose()
        else:
            print(f"\nДракон нанес удар рыцарю, но не смог нанести урон. Рыцарь был под щитом")
    
    def dragon_damage(self):
        if self.dragon._hp > 0:
            if random.random() <= 0.50:
                if random.random() <= 0.50:
                    self.dragon_damage_whith_fire_ball()
                else:
                    self.dragon_damage_whithout_fire_ball()    
            else:
                print(f"\nДракон проспал свой ход")
                print(f"У рыцаря все еще {self.knight.health_tracking()} единиц здоровья \n")
 
    def dragon_attack(self):
        if self.knight._hp > 0:
            self.dragon_damage()
            self.knight.remove_shield()
            if self.knight._hp == 0:
                Damage.LOOP_ = False
        else:
            Damage.LOOP_ = False

    def knight_damage(self):
        if self.knight._hp > 0:
            if random.random() <= 0.75:
                self.dragon._hp -= self.knight.hit() - self.dragon._defence
                print(f"\nРыцарь нанес удар и дракон получил {self.knight.hit() - self.dragon._defence} единиц урона")
                print(f"И теперь у дракона осталось {self.dragon.health_tracking()} единиц здоровья \n")
                self.dragon.hiroe_lose()
            else:
                print(f"\nРыцарь не смог попасть и нанести урон дракону")
                print(f"У дракона все еще {self.dragon.health_tracking()} единиц здоровья \n")

    def knight_attack(self):
        if self.dragon._hp > 0: 
            self.knight_damage()
            if self.dragon._hp == 0:
                Damage.LOOP_ = False
        else:
            Damage.LOOP_ = False
 
class DragonGame:
 
    """Здесь происходит сражение"""
 
    damage = Damage()
 
    while damage.LOOP_:
        action = input("Пожалуйста введите действие рыцаря: attack, pass, defence, potion\n")
        
        if action == "attack":
            damage.knight_attack()
            damage.dragon_attack()
        elif action == "pass":
            pass
            damage.dragon_attack()
        elif action == "defence":
            damage.knight.equip_shield()
            damage.dragon_attack()
        elif action == "potion":
            damage.knight.get_potion()
            damage.dragon_attack()
        else:
            print("\nТаклй комманды нет попробуйте снова \n")  
 
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