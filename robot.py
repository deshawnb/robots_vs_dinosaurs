from weapon import Weapon
class Robot:

    def __init__(self, name):
        self.name = name
        self.helth = 0
        self.active_weapon = Weapon('', 0)

    def attack(self, dinosaur):
        pass
