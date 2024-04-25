from game_logic.mech import Mech

class Player:
    def __init__(self, name):
        self.name = name
        self.mech = Mech()

    def choose_part(self, mech, part_name):
        self.mech.add_part(mech, part_name)
