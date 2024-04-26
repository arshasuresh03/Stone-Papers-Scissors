import random

# Define winning patterns
winning_patterns = {
    "scissors": ["paper", "lizard"],
    "paper": ["rock", "Spock"],
    "rock": ["lizard", "scissors"],
    "lizard": ["Spock", "paper"],
    "Spock": ["scissors", "rock"]
}

# Define instructions
print("There are 6 rounds.\nYou are playing against Computron.\nYou will win if you have a higher point."
      "\nEnter scissors, paper, rock, lizard or Spock.\nLIVE LONG AND PROSPER🖖\n")

# Choices for the Computron to choose from
choices = ["scissors", "paper", "rock", "lizard", "Spock"]

# Initialize points
player_points = 0
computron_points = 0

# Run 6 rounds
for round_num in range(1, 7):
    print(f"Round {round_num}")

    # Player's move
    player_move = input("What is your move? ")
    computron_move = random.choice(choices)

    # Display Computron's move
    print(f"Computron chooses: {computron_move}")

    # Determine the winner
    if player_move == computron_move:
        print("Draw, both get 1 point")
        player_points += 1
        computron_points += 1
    elif computron_move in winning_patterns.get(player_move, []):
        print(f"{player_move.capitalize()} wins! You won this round.")
        player_points += 1
    else:
        print(f"{computron_move.capitalize()} wins! Computron won this round.")
        computron_points += 1

    print("")  # Empty line for clarity

# Compare points to determine the winner
if player_points > computron_points:
    print("You are the champion! 🏆")
elif player_points < computron_points:
    print("Computron is the champion. Try again! 💻")
else:
    print("It's a tie! You both are champions! 🏆🏆")
