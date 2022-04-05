from dinosuar import Dinosaur
class Herd:

    def __init__(self):
        self.dino_one = Dinosaur('', 0, 0)
        self.dino_two = Dinosaur('', 0, 0)
        self.dino_three = Dinosaur('', 0, 0)
        self.herd_attack_power = self.dino_one.attack_power + self.dino_two.attack_power + self.dino_three.attack_power
        self.herd_health = self.dino_one.health + self.dino_one.health + self.dino_one.health 

    def herd_attack(self, robot_one, robot_two, robot_three):
        self.robot_one_hp = robot_one
        self.robot_two_hp = robot_two
        self.robot_three_hp = robot_three
        self.fleet_hp = self.robot_one_hp + self.robot_two_hp + self.robot_three_hp
        self.herd_attack_power = self.dino_one.attack_power + self.dino_two.attack_power + self.dino_three.attack_power
        print(f'the fleet of robots has {self.robot_one_hp}, {self.robot_two_hp} and {self.robot_three_hp} health')
        print(f'the fleet has a total of {self.fleet_hp}')
        print(f'{self.dino_one.name}, {self.dino_two.name} and {self.dino_three.name} attack the fleet for {self.herd_attack_power}')
        if self.robot_one_hp > 0:
            self.robot_one_hp = self.robot_one_hp - self.herd_attack_power
        elif self.robot_two_hp > 0:
            self.robot_two_hp = self.robot_two_hp - self.herd_attack_power
        elif self.robot_three_hp > 0:
            self.robot_three_hp = self.robot_three_hp - self.herd_attack_power
        else:
            print('the fleet has fallen!')
        self.fleet_hp = self.robot_one_hp + self.robot_two_hp + self.robot_three_hp
        print(f'the fleet now has {self.fleet_hp}')
        print()

    def select_herd(self):
        print('select three dinosuars for the herd:')
        self.dino_one.select_dino()
        self.dino_two.select_dino()
        self.dino_three.select_dino()
        self.herd_health = self.dino_one.health + self.dino_one.health + self.dino_one.health
        print(f'the dinosuar herd will have {self.dino_one.name}, {self.dino_two.name}, and {self.dino_three.name}')