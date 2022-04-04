from weapon import Weapon
import random
class Robot:

    def __init__(self, name, hp):
        self.name = name
        self.health = hp
        self.active_weapon = Weapon('', 0)

    def attack(self, dinosaur):
        self.dino_hp = dinosaur
        print(f'the dinosaurs hp is {self.dino_hp}')
        print(f'{self.name} attacks the dinosuar with {self.active_weapon.name} for {self.active_weapon.attack_power}')
        self.dino_hp = self.dino_hp - self.active_weapon.attack_power
        print(f'the dinosaurs hp is now {self.dino_hp}')
        print('')

    def weapon_list(self):
        stick = ['stick', 5]
        laser_gun = ['laser gun', 20]
        beam_sword = ['beam sword', 40]
        
        self.weapons = [stick, laser_gun, beam_sword,]

    def random_weapon(self):
        list_index = len(self.weapons) - 1
        random_number = random.randint(0, list_index)
        chosen_weapon = self.weapons[random_number]
        weapon_name = chosen_weapon[0]
        weapon_attack = chosen_weapon[1]
        self.active_weapon = Weapon(weapon_name, weapon_attack)
        print(f'{weapon_name} {weapon_attack}')
        