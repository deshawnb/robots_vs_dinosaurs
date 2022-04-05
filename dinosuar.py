class Dinosaur:

    def __init__(self, name, attack_power, hp):
        self.name = name
        self.attack_power = attack_power
        self.health = hp
        self.chicken = ['chicken', 1, 10]
        self.raptor = ['raptor', 10, 100]
        self.triceratops = ['triceratops', 20, 200]
        self.t_rex = ['t rex', 30, 300]
        self.spinosaurus = ['spinosaurus', 50, 500]
        self.dragon = ['dragon', 100, 1000]

    def attack(self, robot):
        self.robot_hp = robot
        print(f'the robots hp is {self.robot_hp}')
        print(f'{self.name} attacks the robot for {self.attack_power}')
        self.robot_hp = self.robot_hp - self.attack_power
        print(f'the robots hp is now {self.robot_hp}')
        print('')

    def set_dino(self, list):
        self.name = list[0]
        self.attack_power = list[1]
        self.health = list[2]