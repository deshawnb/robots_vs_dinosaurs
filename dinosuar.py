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

    def select_dino(self):
        user_input = 0
        while user_input == 0:
            print('select a dinosuar for battle.')
            print('1 = chicken, 2 = raptor, 3 = triceratops, 4 = t rex, 5 = spinosaurus, 6 = dragon')
            user_input = input()
            if user_input == '1':
                self.set_dino(self.chicken)
            elif user_input == '2':
                self.set_dino(self.raptor)
            elif user_input == '3':
                self.set_dino(self.triceratops)
            elif user_input == '4':
                self.set_dino(self.t_rex)
            elif user_input == '5':
                self.set_dino(self.spinosaurus)
            elif user_input == '6':
                self.set_dino(self.dragon)
            else:
                print('invalid input')
                user_input = 0
            print(f'you have selected {self.name}')

    def set_dino(self, list):
        self.name = list[0]
        self.attack_power = list[1]
        self.health = list[2]