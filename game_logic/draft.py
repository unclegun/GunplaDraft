import csv
import os
import random


class Draft:
    def __init__(self, players):
        self.players = players
        self.round = 1
        self.parts = self.load_parts(os.path.join('Data', 'mech_data.csv'))
        self.selected_parts = {player: {"Torso": [], "Arms": [], "Legs": []} for player in players}


    def start(self):
        while self.round <= 5:  # Each player selects 5 pieces
            print(f"\nRound {self.round}")
            for player in self.players:
                print(f"{player.name}'s turn:")
                self.draft_part(player)
            self.round += 1

        # Print selected parts for each player
        print("\nSelected parts for each player:")
        for player, parts in self.selected_parts.items():
            print(f"{player.name}:")
            for part, stats in parts.items():
                print(f"{part}: {stats}")
            print()

    def draft_part(self, player):
        if not player:
            print("Invalid player. Please provide a valid player.")
            return

        # Display available parts for each mech
        print("Available parts:")
        for mech, parts in self.parts.items():
            print(f"{mech}:")
            for part, stats in parts.items():
                if (part not in self.selected_parts[player].values() and
                        (part == "Arms" or part == "Legs" or
                         len(self.selected_parts[player][part]) < 2)):
                    print(f"- {part}: {stats}")

        # Prompt player to choose a mech and part
        while True:
            mech = input("Choose a mech: ")
            part = input("Choose a part: ")
            if (mech in self.parts and part in self.parts[mech] and
                    part not in self.selected_parts[player].values() and
                    (part == "Arms" or part == "Legs" or
                     len(self.selected_parts[player][part]) < 2)):
                break
            else:
                print("Invalid choice. Please choose from available mechs and parts.")

        # Check if the part is Arms or Legs, and if the player has not already selected two of the same type
        if (part == "Arms" or part == "Legs") and len(self.selected_parts[player][part]) < 2:
            self.selected_parts[player][part].append((mech, part))
            print(f"{player.name} selects {part} from {mech}")
        # Check if the part is not Arms or Legs, and if it has not been selected before
        elif part != "Arms" and part != "Legs" and part not in self.selected_parts[player]:
            self.selected_parts[player][part] = self.parts[mech][part]
            print(f"{player.name} selects {part} from {mech}")
        else:
            print("Invalid choice. Please choose from available mechs and parts.")

    def load_parts(self, filepath):
        parts = {}
        with open(filepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                mech = row['Mech']
                part = row['Part']
                durability = int(row['Durability']) if row['Durability'] else 0
                attack = int(row['Attack']) if row['Attack'] else 0
                defense = int(row['Defense']) if row['Defense'] else 0
                weight = int(row['Weight']) if row['Weight'] else 0
                stats = {
                    'Durability': durability,
                    'Attack': attack,
                    'Defense': defense,
                    'Weight': weight
                }
                if mech not in parts:
                    parts[mech] = {}
                parts[mech][part] = stats
        return parts
