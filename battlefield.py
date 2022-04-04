import random
from robot import Robot
from dinosuar import Dinosaur
class Battlefield:

    def __init__(self):
        self.robot = Robot('')
        self.dinosuar = Dinosaur('', 0)

    def run_game(self):
        pass

    def combatant_list(self):
        raptor = ['raptor', 100, 10]
        triceratops = ['triceratops', 200, 20]
        t_rex = ['t rex', 300, 30]
        self.dinosaurs = [raptor, triceratops, t_rex]
        droid = ['droid', 50]
        terminator = ['terminator', 150]
        robo_cop = ['robocop', 400]
        self.robots = [droid, terminator, robo_cop]


    def combatant_randomizer(self,list):
        list_index = len(list) - 1
        random_number = random.randint(0, list_index)
        chosen_combatant = list[random_number]
        name = chosen_combatant[0]
        health = chosen_combatant[1]
        attack = chosen_combatant[2]
        if list is self.dinosaurs:
            self.dinosuar = Dinosaur(name, attack)
        elif list is self.robots:
            self.robot = Robot(name)

        

    def display_welcome(self):
        print('Welcome to Robots vs Dinosuars !!!')

        print('we will now have a battle between')
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass