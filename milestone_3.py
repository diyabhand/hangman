import random

# Task 1
def create_word_list():
    favorite_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Grapes"]
    return favorite_fruits

# Task 2
def choose_random_word(word_list):
    return random.choice(word_list)

# Task 3
def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

# Task 4
def check_guess(guess):
    word = choose_random_word(word_list)
    guess = guess.lower()
    
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

if __name__ == "__main__":
    word_list = create_word_list()
    print("Word List:", word_list)
    
    while True:
        ask_for_input()
        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
