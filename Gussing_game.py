import random

# Function to play the guessing game
def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        # Prompt the user to input their guess
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1
        
        # Compare the guess to the generated number
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            # Correct guess
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
            break

# Run the game
if __name__ == "__main__":
    guessing_game()
