from image_ACS import start_game, pass_round
from heroes_damage import Damage

def main():
    #There's a battle going on here
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
        damage.show_line_whiht_hp_hiroes()
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


if __name__ == '__main__':
    main()
