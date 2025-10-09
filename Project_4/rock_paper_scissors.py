import random

symbols: dict[str, str] = {'rock': '🪨', 'paper': '📄', 'scissors': '✂️'}

player_choice: str = input('Choose rock (🪨), paper (📄) or scissors (✂️): ').strip().lower()
computer_choice: str = random.choice(tuple(symbols))

print("\nResults")
print("-" * 10)
print(f"User choice: {player_choice} {symbols[player_choice]}")
print(f"User choice: {computer_choice} {symbols[computer_choice]}")
print("-" * 10)

if player_choice == computer_choice:
    print("It's a draw!")
elif player_choice == 'rock' and computer_choice == 'scissors':
    print("You Win!")
elif player_choice == 'scissors' and computer_choice == 'paper':
    print("You Win!")
elif player_choice == 'paper' and computer_choice == 'rock':
    print("You Win!")
else:
    print("You Lose!")