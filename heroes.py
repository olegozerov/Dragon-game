
from image_ACS import death, knight_shield, bottle


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
 
    def remove_shield(self):
        """Removing the shield, the hero's defense is reduced by the number of shield units"""
        if self._hp > 0:
            if Knight.HAS_SHIELD is True:
                self._defence -= self._shield
                Knight.HAS_SHIELD = False
                return Knight.HAS_SHIELD
    
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