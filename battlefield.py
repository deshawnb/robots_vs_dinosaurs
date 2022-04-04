import random
from robot import Robot
from dinosuar import Dinosaur
class Battlefield:

    def __init__(self):
        self.robot = Robot('', 0)
        self.dinosuar = Dinosaur('', 0, 0)

    def run_game(self):
        self.combatant_list()
        self.combatant_randomizer(self.dinosaurs)
        self.combatant_randomizer(self.robots)
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def combatant_list(self):
        raptor = ['raptor', 100, 10]
        triceratops = ['triceratops', 200, 20]
        t_rex = ['t rex', 300, 30]
        self.dinosaurs = [raptor, triceratops, t_rex]
        droid = ['droid', 50, 0]
        terminator = ['terminator', 150, 0]
        robo_cop = ['robocop', 400, 0]
        self.robots = [droid, terminator, robo_cop]

    def combatant_randomizer(self,list):
        list_index = len(list) - 1
        random_number = random.randint(0, list_index)
        chosen_combatant = list[random_number]
        name = chosen_combatant[0]
        health = chosen_combatant[1]
        attack = chosen_combatant[2]
        if list is self.dinosaurs:

            self.dinosuar = Dinosaur(name, attack, health)
        elif list is self.robots:
            self.robot = Robot(name, health)
            self.robot.weapon_list()
            self.robot.random_weapon()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosuars !!!')
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
        