from weapon import Weapon
import random
class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon('', 0)

    def attack(self, dinosaur):
        pass

    def weapon_list(self):
        stick = ['stick', 5]
        laser_gun = ['laser gun', 10]
        beam_sword = ['beam sword', 15]
        
        self.weapons = [stick, laser_gun, beam_sword,]
        

    def random_weapon(self):
        list_index = len(self.weapons) - 1
        random_number = random.randint(0, list_index)
        chosen_weapon = self.weapons[random_number]
        weapon_name = chosen_weapon[0]
        weapon_attack = chosen_weapon[1]
        self.active_weapon = Weapon(weapon_name, weapon_attack)
        print(f'{weapon_name} {weapon_attack}')
        