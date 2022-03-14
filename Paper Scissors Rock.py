import random

options = ["paper", "scissors", "rock"]
rounds = range(0, 3)

computer_score = 0
player_score = 0

print("Welcome to Paper Scissors Rock")

for number in rounds:
    ai_choice = random.choice(options)
    player_choice = input("\nWhat's your move? ")
    if player_choice == "paper":
        if ai_choice == "paper":
            print("Computer chose paper. Draw!")
        elif ai_choice == "scissors":
            print("Computer chose scissors. Computer wins!")
            computer_score += 1
        elif ai_choice == "rock":
            print("Computer chose rock. You win!")
            player_score += 1

    elif player_choice == "scissors":
        if ai_choice == "paper":
            print("Computer chose paper. Yow win!")
            player_score += 1
        elif ai_choice == "scissors":
            print("Computer chose scissors. Draw!")
        elif ai_choice == "rock":
            print("Computer chose rock. Computer wins!")
            computer_score += 1

    elif player_choice == "rock":
        if ai_choice == "paper":
            print("Computer chose paper. Yow win!")
            player_score += 1
        elif ai_choice == "scissors":
            print("Computer chose scissors. Draw!")
        elif ai_choice == "rock":
            print("Computer chose rock. Computer wins!")
            computer_score += 1

    else:
        print("\nPlease type [paper] [scissors] or [rock].")


if player_score == 0 and computer_score == 0:
    exit("\nThere were three draws.")
elif player_score < computer_score:
    exit(f"\nComputer wins with {computer_score} points to {player_score}.")
else:
    exit(f"\nPlayer wins with {player_score} points to {computer_score}.")
