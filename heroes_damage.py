import random
from image_ACS import dragon_att_fire, dragon_sleep, knight_att, dragon_att, fack
from heroes import Dragon, Knight


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

    def show_line_whiht_hp_hiroes(self):
        print("\n+" + "DRAGON hp - " + f"{self.dragon._hp}" + "-" * 120 + f"{self.knight._hp}" + " - hp KNIGHT" + "+\n")