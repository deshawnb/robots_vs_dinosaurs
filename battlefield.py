from robot import Robot
from dinosuar import Dinosaur
class Battlefield:

    def __init__(self):
        self.robot = Robot('', 0)
        self.dinosuar = Dinosaur('', 0, 0)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def select_robot(self):
        user_input = 0
        while user_input == 0:
            print('select a robot for battle.')
            print('1 = toaser, 2 = droid, 3 = robocop, 4 = terminator, 5 = gundam, 6 = autobot')
            user_input = input()
            if user_input == '1':
                self.robot.set_robot(self.robot.toaster)
            elif user_input == '2':
                self.robot.set_robot(self.robot.droid)
            elif user_input == '3':
                self.robot.set_robot(self.robot.robo_cop)
            elif user_input == '4':
                self.robot.set_robot(self.robot.terminator)
            elif user_input == '5':
                self.robot.set_robot(self.robot.gundam)
            elif user_input == '6':
                self.robot.set_robot(self.robot.autobot)
            else:
                print('invalid input')
                user_input = 0
        print(f'you have selected {self.robot.name}')
        self.robot.weapon_select()

    def select_dino(self):
        user_input = 0
        while user_input == 0:
            print('select a dinosuar for battle.')
            print('1 = chicken, 2 = raptor, 3 = triceratops, 4 = t rex, 5 = spinosaurus, 6 = dragon')
            user_input = input()
            if user_input == '1':
                self.dinosuar.set_dino(self.dinosuar.chicken)
            elif user_input == '2':
                self.dinosuar.set_dino(self.dinosuar.raptor)
            elif user_input == '3':
                self.dinosuar.set_dino(self.dinosuar.triceratops)
            elif user_input == '4':
                self.dinosuar.set_dino(self.dinosuar.t_rex)
            elif user_input == '5':
                self.dinosuar.set_dino(self.dinosuar.spinosaurus)
            elif user_input == '6':
                self.dinosuar.set_dino(self.dinosuar.dragon)
            else:
                print('invalid input')
                user_input = 0
            print(f'you have selected {self.dinosuar.name}')

    def display_welcome(self):
        print('Welcome to Robots vs Dinosuars !!!')
        self.select_robot()
        self.select_dino()
        print(f'we will now have a battle between {self.dinosuar.name} and {self.robot.name}')

    def battle_phase(self):
        input('press enter to start the fight!')
        print('')
        while self.dinosuar.health > 0 or self.robot.health > 0:
            self.robot.attack(self.dinosuar.health)
            self.dinosuar.health = self.robot.dino_hp
            self.dinosuar.attack(self.robot.health)
            self.robot.health = self.dinosuar.robot_hp
            input('press enter to continue')
            print('')
            if self.dinosuar.health <= 0 or self.robot.health <= 0:
                break

    def display_winner(self):
        if self.dinosuar.health <= 0 and self.robot.health <= 0:
            print('its a tie!')
        elif self.dinosuar.health <= 0:
            print('Robots win!')
        elif self.robot.health <= 0:
            print('Dinosuars win!')
        