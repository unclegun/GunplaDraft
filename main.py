from game_logic.draft import Draft
from game_logic.player import Player


def get_players():
    num_players = int(input("Enter the number of players: "))
    players = []
    for i in range(num_players):
        name = input(f"Enter name for Player {i + 1}: ")
        players.append(Player(name))
    return players


def main():
    # Get players
    players = get_players()

    # Initialize draft
    draft = Draft(players)
    # Start draft
    draft.start()


if __name__ == "__main__":
    main()
