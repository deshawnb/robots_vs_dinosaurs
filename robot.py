from weapon import Weapon
class Robot:

    def __init__(self, name, hp):
        self.name = name
        self.health = hp
        self.active_weapon = Weapon('', 0)
        self.toaster = ['toaster', 10]
        self.droid = ['droid', 100]
        self.robo_cop = ['robocop', 200]
        self.terminator = ['terminator', 300]
        self.gundam = ['gundam', 500]
        self.autobot = ['autobot', 1000]

    def attack(self, dinosaur):
        self.dino_hp = dinosaur
        print(f'the dinosaurs hp is {self.dino_hp}')
        print(f'{self.name} attacks the dinosuar with {self.active_weapon.name} for {self.active_weapon.attack_power}')
        self.dino_hp = self.dino_hp - self.active_weapon.attack_power
        print(f'the dinosaurs hp is now {self.dino_hp}')
        print('')

    def set_robot(self, list):
        self.name = list[0]
        self.health = list[1]

    def weapon_select(self):
        user_input = 0
        while user_input == 0:
            print('select a weapon for the robot.')
            print('1 = stick, 2 = pistol, 3 = laser gun, 4 = beam sword, 5 = plasma rifle, 6 = mech suit')
            user_input = input()
            if user_input == '1':
                self.active_weapon.set_wepon(self.active_weapon.stick)
            elif user_input == '2':
                self.active_weapon.set_wepon(self.active_weapon.pistol)
            elif user_input == '3':
                self.active_weapon.set_wepon(self.active_weapon.laser_gun)
            elif user_input == '4':
                self.active_weapon.set_wepon(self.active_weapon.beam_sword)
            elif user_input == '5':
                self.active_weapon.set_wepon(self.active_weapon.plasma_rifle)
            elif user_input == '6':
                self.active_weapon.set_wepon(self.active_weapon.antimatter)
            else:
                print('invalid input')
                user_input = 0
        print(f'{self.name} will use {self.active_weapon.name} to fight')