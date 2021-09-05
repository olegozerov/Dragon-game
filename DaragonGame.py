class Hiroes:
    """
    hp - жизненная энергия, запас здоровья
    defence - защита
    srong - сила
    weapon - оружие
    shield - щит
    magic - магия
    (на будующее)
    """
    def __init__(self, hp, defence, strong, weapon, shield, magic):
        self.hp = hp
        self.defence = defence
        self.strong = strong
        self.weapon = weapon
        self.shield = shield
        self.magic = magic


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

