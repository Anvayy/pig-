import random

def roll():
    min_roll = 1
    max_roll = 6
    roll = random.randint(min_roll, max_roll)
    return roll

while True:
    players = int(input("Enter the number of players (2-4): "))
    if 2 <= players <= 4:
        print(players, "players are playing")
        break
    else:
        print("Invalid number / input")
        False

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        current_score = 0
        print("\nPlayer ", player_idx + 1," is playing!")
        print("Your total score is ", player_scores[player_idx], "\n")

        while True:
            should_roll = input("Would you like to roll? (y)?: ")
            if should_roll.lower() != "y":
                print("Not rolling.")
                break
            elif should_roll.lower == "exit":
                exit()

            value = roll()
            if value == 1:
                print(("You rolled a 1. Turn end!"))
                current_score = 0
            else:
                current_score += value
                print("You rolled a ", value)
            
            print("You score is", current_score)

        player_scores[player_idx] = current_score
        print("Your total score is ", player_scores[player_idx])
        
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("\nPlayer ", winning_idx + 1, " won the game with a score of ", max_score, "!\n")

        