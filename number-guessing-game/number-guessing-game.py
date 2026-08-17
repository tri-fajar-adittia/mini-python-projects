import random

def check_guess(guess, number):
    attempt = 0

    while True:
        attempt += 1 
        if(guess < number):
            print("Too Low\n")
            guess = input_number()

        elif(guess > number):
            print("Too Big\n") 
            guess = input_number()

        else:
            attempt_word = "attempt" if attempt == 1 else "attempts"
            print("\nCorrect!")
            print(f"You guessed it in {attempt} {attempt_word}.\n")
            break
            

def generate_number():
    return random.randint(1,10)

def input_number():
    while True:
        try:
            guess = int(input("Enter your number (1-10): "))
            if guess >= 1 and 10 >= guess:
                return guess
            else:
                print("Please enter (1-10)\n")
        except ValueError:
                print("Invalid input. Please enter a number.\n")


def display():
    print("=================================")
    print("       NUMBER GUESSING GAME      ")
    print("=================================")
    print("       By Tri Fajar Adittia      ")
    print("=================================\n")
    print("I'm thinking of a number between 1 and 10.")
    print("Can you guess it?\n")

def main():
    display()
    number = generate_number()
    guess = input_number()   
    check_guess(guess, number)

main()