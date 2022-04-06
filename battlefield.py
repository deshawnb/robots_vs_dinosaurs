from robot import Robot
from dinosuar import Dinosaur
from fleet import Fleet
from herd import Herd
class Battlefield:

    def __init__(self):
        self.robot = Robot('', 0)
        self.dinosuar = Dinosaur('', 0, 0)
        self.fleet = Fleet()
        self.herd = Herd()
        self.is_a_group_battle = False

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosuars !!!')
        user_input = 0
        while user_input == 0:
            print('would you like a 1v1 or a 3v3?')
            user_input = input('1 = 1v1  2 = 3v3: ')
            if user_input == '1':
                self.is_a_group_battle = False
                self.robot.select_robot()
                self.dinosuar.select_dino()
                print(f'we will now have a battle between {self.dinosuar.name} and {self.robot.name}')
            elif user_input == '2':
                self.is_a_group_battle = True
                self.fleet.select_fleet()
                self.herd.select_herd()
                print('we will now have a battle between the fleet and the herd')
            else:
                print('invalid input')
                user_input = 0

    def battle_phase(self):
        input('press enter to start the fight!')
        print('')
        if self.is_a_group_battle == False:
            while self.dinosuar.health > 0 or self.robot.health > 0:
                self.robot.attack(self.dinosuar.health)
                self.dinosuar.health = self.robot.dino_hp
                self.dinosuar.attack(self.robot.health)
                self.robot.health = self.dinosuar.robot_hp
                input('press enter to continue')
                print('')
                if self.dinosuar.health <= 0 or self.robot.health <= 0:
                    break
        else:
            while self.fleet.fleet_health > 0 or self.herd.herd_health > 0:
                self.fleet.fleet_attack(self.herd.dino_one.health, self.herd.dino_two.health, self.herd.dino_three.health)
                self.herd.herd_health = self.fleet.herd_hp
                self.herd.dino_one.health = self.fleet.dino_one_hp
                self.herd.dino_two.health = self.fleet.dino_two_hp
                self.herd.dino_three.health = self.fleet.dino_three_hp
                self.herd.herd_attack(self.fleet.robot_one.health, self.fleet.robot_two.health, self.fleet.robot_three.health)
                self.fleet.fleet_health = self.herd.fleet_hp
                self.fleet.robot_one.health = self.herd.robot_one_hp
                self.fleet.robot_two.health = self.herd.robot_two_hp
                self.fleet.robot_three.health = self.herd.robot_three_hp
                input('press enter to continue')
                print('')
                if self.herd.herd_health <= 0 or self.fleet.fleet_health <= 0:
                    break

    def display_winner(self):
        if self.is_a_group_battle == False:
            if self.dinosuar.health <= 0 and self.robot.health <= 0:
                print('its a tie!')
            elif self.dinosuar.health <= 0:
                print('Robots win!')
            elif self.robot.health <= 0:
                print('Dinosuars win!')
        elif self.is_a_group_battle == True:
            if self.herd.herd_health <= 0 and self.fleet.fleet_health <= 0:
                print('its a tie!')
            elif self.herd.herd_health <= 0:
                print('Robots win!')
            elif self.fleet.fleet_health <= 0:
                print('Dinosuars win!')
        