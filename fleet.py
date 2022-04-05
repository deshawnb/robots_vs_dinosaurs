from robot import Robot
class Fleet:

    def __init__(self):
        self.robot_one = Robot('', 0)
        self.robot_two = Robot('', 0)
        self.robot_three = Robot('', 0)
        self.fleet_attack_power = self.robot_one.active_weapon.attack_power + self.robot_two.active_weapon.attack_power + self.robot_three.active_weapon.attack_power
        self.fleet_health = self.robot_one.health + self.robot_two.health + self.robot_three.health

    def fleet_attack(self, dino_one, dino_two, dino_three):
        self.dino_one_hp = dino_one
        self.dino_two_hp = dino_two
        self.dino_three_hp = dino_three
        self.herd_hp = self.dino_one_hp + self.dino_two_hp + self.dino_three_hp
        self.fleet_attack_power = self.robot_one.active_weapon.attack_power + self.robot_two.active_weapon.attack_power + self.robot_three.active_weapon.attack_power
        print(f'the herd of dinos has {self.dino_one_hp}, {self.dino_two_hp} and {self.dino_three_hp} health')
        print(f'the herd has a total of {self.herd_hp}')
        print(f'{self.robot_one.name}, {self.robot_two.name} and {self.robot_three.name} attack the herd for {self.fleet_attack_power}')
        if self.dino_one_hp > 0:
            self.dino_one_hp = self.dino_one_hp - self.fleet_attack_power
        elif self.dino_two_hp > 0:
            self.dino_two_hp = self.dino_two_hp - self.fleet_attack_power
        elif self.dino_three_hp > 0:
            self.dino_three_hp = self.dino_three_hp - self.fleet_attack_power
        else:
            print('the herd has fallen!')
        self.herd_hp = self.dino_one_hp + self.dino_two_hp + self.dino_three_hp
        print(f'the herd now has {self.herd_hp}')
        print()

    def select_fleet(self):
        print('select three robots for the fleet:')
        self.robot_one.select_robot()
        self.robot_two.select_robot()
        self.robot_three.select_robot()
        self.fleet_health = self.robot_one.health + self.robot_two.health + self.robot_three.health
        print(f'the robot fleet will have {self.robot_one.name}, {self.robot_two.name}, and {self.robot_three.name}')
