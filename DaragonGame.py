import random
from imageACS import *
 
class Hero:
    """Here we breed our heroes"""

    def __init__(self, hp=0, defence=0, strong=0, weapon=0, shield=0, potion=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
        self._shield = shield        #  shield - щит
        self._potion = potion        #  potion - зелье
 
    def health_tracking(self):
        """We make sure that the hp level is not lower than 0"""
        if self._hp < 0:
            self._hp = 0
            return self._hp
        return self._hp
 
    def hiroe_lose(self):
        """We display a message about the death of one of the heroes"""
        if self._hp <= 0:
            print("\n\n+" + "-" * 150 + "+")
            print(f"{self.__repr__()} DIED ")
            print("+" + "-" * 150 + "+")
            print(death)
 
    def hit(self):
        """Hit one of the heroes"""
        return self._strong + self._weapon
 
class Dragon(Hero):
    """The dragon has the following characteristics: hp, defense, strong, weapon"""
 
    def __init__(self, hp=900, defence=120, strong=150, weapon=0):
        self._hp = hp                #  hp - жизненная энергия, запас здоровья
        self._defence = defence      #  defence - защита
        self._strong = strong        #  srong - сила
        self._weapon = weapon        #  weapon - оружие
 
    def __str__(self):
        return f"Dragon characteristics: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n"
 
    def fire_ball(self):
        """Fire strike"""
        return self._strong * 2
 
    def __repr__(self):
        return f"{'DRAGON'}"
                
class Knight(Hero):
    """The knight has the following characteristics: hp, defense, strong, weapon, shield"""
    HAS_SHIELD = False
 
    def __init__(self, hp=400, defence=100, strong=120, weapon=250, shield=150, potion=(1, 500)):
        self._hp = hp                                           #  hp - жизненная энергия, запас здоровья
        self._defence = defence                                 #  defence - защита
        self._strong = strong                                   #  srong - сила
        self._weapon = weapon                                   #  weapon - оружие
        self._shield = shield                                   #  shield - щит
        self._potion_butle, self._potion_portion = potion       #  potion_butle - количество бутылочек с зельем
                                                                #  potion_portion - порция зелья
 
    def equip_shield(self):
        """The use of a shield, the hero's defense increases by the number of shield units"""
        if Knight.HAS_SHIELD is False:
            self._defence += self._shield
            Knight.HAS_SHIELD = True
            print(knight_shield)
            print("+" + "-" * 150 + "+")
            print(f"The knight has put on his shield, his defense is now {self._defence} units")
            print("+" + "-" * 150 + "+")
            return Knight.HAS_SHIELD
        pass
 
    def remove_shield(self):
        """Removing the shield, the hero's defense is reduced by the number of shield units"""
        if self._hp > 0:
            if Knight.HAS_SHIELD is True:
                self._defence -= self._shield
                Knight.HAS_SHIELD = False
                return Knight.HAS_SHIELD
            pass
 
    def get_potion(self):
        """Applying a knight's hp increasing potion"""
        if self._potion_butle > 0:
            self._potion_butle -= 1
            self._hp += self._potion_portion
            print(bottle)
            print("+" + "-" * 150 + "+")
            print(f"The knight drank the potion and his health increased by {self._potion_portion} units")
            print(f"Potion bottles left {self._potion_butle}")
            print("+" + "-" * 150 + "+")
            return self._hp
        print("+" + "-" * 150 + "+")
        print("\nIt was a mistake! Potion bottles are out \n")
        print("+" + "-" * 150 + "+")

  
    def __str__(self):
        return f"Dragon characteristics: hp = {self._hp}\n \
                       defence = {self._defence}\n \
                       strong = {self._strong}\n \
                       weapon = {self._weapon}\n \
                       shield = {self._shield}\n \
                       potion_butle = {self._potion_butle}\n \
                       potion_portion = {self._potion_portion}\n"
 
    def __repr__(self):
        return f"{'KNIGHT'}"
 
class Damage():
    """Described damage methods depending on the character of the game"""  
    LOOP = True
    dragon = Dragon()
    knight = Knight()   
 
    def dragon_damage_whith_fire_ball(self):
        if self.knight.HAS_SHIELD is False:
            self.knight._hp -= self.dragon.fire_ball()
            print(dragon_att_fire)
            print("+" + "-" * 150 + "+")
            print(f"The dragon struck with fire and the knight took {self.dragon.fire_ball()} damage") 
            print(f"And now the knight has {self.knight.health_tracking()} health units left")
            print("+" + "-" * 150 + "+")
            self.knight.hiroe_lose()
        else:
            print(fack)
            print("+" + "-" * 150 + "+")
            print(f"The dragon spewed fire, but was unable to deal damage. The knight was under the shield")
            print("+" + "-" * 150 + "+")

 
    def dragon_damage_whithout_fire_ball(self):
        if self.dragon.hit() > self.knight._defence:
            self.knight._hp -= self.dragon.hit() - self.knight._defence
            print(dragon_att)
            print("+" + "-" * 150 + "+")
            print(f"The dragon struck and the knight took {self.dragon.hit() - self.knight._defence} damage") 
            print(f"And now the knight has {self.knight.health_tracking()} health units left ")
            print("+" + "-" * 150 + "+")
            self.knight.hiroe_lose()
        else:
            print(fack)
            print("+" + "-" * 150 + "+")
            print(f"The dragon stabbed the knight, but was unable to inflict damage. The knight was under the shield")
            print("+" + "-" * 150 + "+")

    
    def dragon_damage(self):
        if self.dragon._hp > 0:
            if random.random() <= 0.50:
                if random.random() <= 0.50:
                    self.dragon_damage_whith_fire_ball()
                else:
                    self.dragon_damage_whithout_fire_ball()    
            else:
                print(dragon_sleep)
                print("+" + "-" * 150 + "+")
                print(f"The dragon slept through its turn")
                print(f"The knight still has {self.knight.health_tracking()} health points ")
                print("+" + "-" * 150 + "+")
 
    def dragon_attack(self):
        if self.knight._hp > 0:
            self.dragon_damage()
            self.knight.remove_shield()
            if self.knight._hp == 0:
                Damage.LOOP = False
        else:
            Damage.LOOP = False

    def knight_damage(self):
        if self.knight._hp > 0:
            if random.random() <= 0.75:
                self.dragon._hp -= self.knight.hit() - self.dragon._defence
                print(knight_att)
                print("+" + "-" * 150 + "+")
                print(f"The knight struck and the dragon took {self.knight.hit() - self.dragon._defence} damage")
                print(f"And now the dragon has {self.dragon.health_tracking()} health units ")
                print("+" + "-" * 150 + "+")
                self.dragon.hiroe_lose()
            else:
                print(fack)
                print("+" + "-" * 150 + "+")
                print(f"The knight was unable to hit and damage the dragon")
                print(f"The dragon still has {self.dragon.health_tracking()} health ")
                print("+" + "-" * 150 + "+")


    def knight_attack(self):
        if self.dragon._hp > 0: 
            self.knight_damage()
            if self.dragon._hp == 0:
                Damage.LOOP = False
        else:
            Damage.LOOP = False
 
class DragonGame:
    """There's a battle going on here"""
    damage = Damage()
    print("\n+" + "-" * 64 + "DRAGONGAME" + "-" * 64 + "+")
    print(start_game)
    print(damage.knight)
    print(damage.dragon)
    counter = 1
 
    while damage.LOOP:
        print("\n\n+" + "-" * 72 + "ROUND"+f"{counter}" + "-" * 72 + "+\n\n")
        counter += 1
        print("+" + "-" * 150 + "+")
        print("\n+" + "DRAGON hp - " + f"{damage.dragon._hp}" + "-" * 120 + f"{damage.knight._hp}" + " - hp KNIGHT" + "+\n")
        action = input("Please enter a knight action: stop, attack, pass, defence, potion, info ==> ").lower()
        print("+" + "-" * 150 + "+")
        if action == "attack":
            damage.knight_attack()
            damage.dragon_attack()
        elif action == "pass":
            print(pass_round)
            print("+" + "-" * 150 + "+")
            print("Knight misses a turn ")
            print("+" + "-" * 150 + "+")
            damage.dragon_attack()
        elif action == "defence":
            damage.knight.equip_shield()
            damage.dragon_attack()
        elif action == "potion":
            damage.knight.get_potion()
            damage.dragon_attack()
        elif action == "info":
            print(damage.knight)
            print(damage.dragon)
        elif action == "stop":
            break
        else:
            print("+" + "-" * 150 + "+")
            print("There is no such command, try again ")
            print("+" + "-" * 150 + "+")  
 
d = Damage()


