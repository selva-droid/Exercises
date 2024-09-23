import random

def play_game():
    # Generate a random number between 0 and 10
    number_to_guess = random.randint(0, 10)
    tries = 0
    
    while True:
        # Get the player's guess
        guess = int(input("Guess the number (between 0 and 10): "))
        tries += 1
        
        if guess < number_to_guess:
            print("Try a greater number.")
        elif guess > number_to_guess:
            print("Try a smaller number.")
        else:
            print(f"That's right! Number of tries: {tries}")
            break

def main():
    print("Welcome to the guessing game!")
    play_game()

if __name__ == "__main__":
    main()