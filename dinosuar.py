from unicodedata import name


class Dinosaur:

    def __init__(self, name, attack_power, hp):
        self.name = name
        self.attack_power = attack_power
        self.health = hp

    def attack(self, robot):
        robot_hp = robot
        print(f'the robots hp is {robot_hp}')
        print(f'{self.name} attacks the robot for {self.attack_power}')
        robot_hp = robot_hp - self.attack_power
        print(f'the robots hp is now {robot_hp}')

    