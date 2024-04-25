class Mech:
    def __init__(self):
        self.parts = {
            "Head": None,
            "Body": None,
            "Arms": None,
            "Legs": None
        }

    def add_part(self, mech, part_name):
        if part_name == "Arms" or part_name == "Legs":
            self.parts[part_name].append(mech)
        else:
            self.parts[part_name] = mech
