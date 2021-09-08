class Hiroes:

    """Тут мы плодим наших героев"""

    def __init__(self, hp, defence, strong, weapon, shield, magic):
        self.hp = hp                #  hp - жизненная энергия, запас здоровья
        self.defence = defence      #  defence - защита
        self.strong = strong        #  srong - сила
        self.weapon = weapon        #  weapon - оружие
        self.shield = shield        #  shield - щит
        self.magic = magic          #  magic - магия


class Dragon(Hiroes):
    def __init__(self, hp=2000, defence=120, strong=150, weapon=0):
        self.hp = hp
        self.defence = defence
        self.strong = strong
        self.weapon = weapon


class Knights(Hiroes):
    def __init__(self, hp=1000, defence=100, strong=120, weapon=250, shield=150):
        self.hp = hp
        self.defence = defence
        self.strong = strong
        self.weapon = weapon
        self.shield = shield



class DragonGame:

    """Здесь происходит сражение"""
    
    while True:
        pass