import random

def play_game():
    print("\n--- Welcome to the Number Guessing Game ---")
    print("I am thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # The inner loop runs until the user guesses the correct number
    while True:
        try:
            # Input validation: prevents crashing if the user types a letter
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is within the valid range
            if guess < 1 or guess > 100:
                print("Please keep your guess between 1 and 100!")
                continue
                
            # Compare the guess to the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                return attempts # Returns the score back to the main loop
                
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Main program starts here
high_score = None

# The outer loop allows the user to play multiple rounds
while True:
    current_score = play_game()
    
    # Update high score if it's the first game or if the new score is better (lower attempts)
    if high_score is None or current_score < high_score:
        high_score = current_score
        print(f"*** New High Score! {high_score} attempts ***")
    else:
        print(f"Your score: {current_score} | Current High Score: {high_score}")
        
    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes' and play_again != 'y':
        print("Thanks for playing! Goodbye.")
        break