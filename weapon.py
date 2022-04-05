class Weapon:

    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.stick = ['stick', 1]
        self.pistol = ['pistol', 10]
        self.laser_gun = ['laser gun', 20]
        self.beam_sword = ['beam sword', 30]
        self.plasma_rifle = ['plasma rifle', 50]
        self.antimatter = ['antimatter rocket', 100]

    def set_wepon(self ,list):
        self.name = list[0]
        self.attack_power = list[1]
