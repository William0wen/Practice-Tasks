import random

options = ["paper", "scissors", "rock"]
rounds = range(0, 3)
victory_rounds = range(1, 4)

computer_score = 0
player_score = 0
total_computer_score = 0
total_player_score = 0

print("Welcome to Paper Scissors Rock")
for number_ in victory_rounds:
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
        print(f"\nFor round {number_} there were three draws.")
    elif player_score < computer_score:
        print(f"\nFor round {number_} Computer wins with {computer_score} points to {player_score}.")
        total_computer_score += 1
    else:
        print(f"\nFor round {number_} Player wins with {player_score} points to {computer_score}.")
        total_player_score += 1

if total_player_score == 0 and total_computer_score == 0:
    print(f"\nThere were three draws.")
elif total_player_score < total_computer_score:
    print(f"\nComputer wins with {total_computer_score} rounds to {total_player_score}.")
else:
    print(f"\nPlayer wins with {total_player_score} rounds to {total_computer_score}.")
