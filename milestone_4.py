import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        # Initialize Hangman attributes
        self.word_list = word_list
        self.word = random.choice(word_list) # Word to be guessed
        self.word_guessed = ['_' for _ in self.word] # List of guessed letters and underscores
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = [] # List of guessed letters

    def check_guess(self, guess):
        guess = guess.lower()  # Convert guess to lowercase
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            self.display_word_guessed()
        self.end_game()

    def display_word_guessed(self):
        print("Word: " + ' '.join(self.word_guessed))
        print(f"Lives left: {self.num_lives}")

    def end_game(self):
        if self.num_letters == 0:
            print("Congratulations, you guessed the word!")
            print(f"The word was: {self.word}")
        else:
            print("Game over. You ran out of lives.")
            print(f"The word was: {self.word}")

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "grape", "kiwi"]
    game = Hangman(word_list)
    game.ask_for_input()
