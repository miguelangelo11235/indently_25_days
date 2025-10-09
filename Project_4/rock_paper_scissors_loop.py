import random

symbols: dict[str, str] = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}
player_choice: str
computer_choice: str
continue_game: str
user_points: int = 0
computer_points: int = 0

print("Rock, paper or scissors?")

while True:

    player_choice = input('Choose rock (🪨), paper (📄) or scissors (✂️): ').strip().lower()
    computer_choice = random.choice(tuple(symbols))

    print("\nResults")
    print("-" * 10)
    print(f"User choice: {player_choice} {symbols[player_choice]}")
    print(f"User choice: {computer_choice} {symbols[computer_choice]}")
    print("-" * 10)

    if player_choice == computer_choice:
        print("It's a draw!")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("You Win!")
        user_points += 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("You Win!")
        user_points += 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("You Win!")
        user_points += 1
    else:
        print("You Lose!")
        computer_points += 1

    print(f"\nTotal Points")
    print(f"Your Points: {user_points}")
    print(f"Computer Points: {computer_points}")

    continue_game = input("\nKeep playing? (y/n): ").lower()
    if continue_game != 'y':
        print("Thank you for playing!")
        break



