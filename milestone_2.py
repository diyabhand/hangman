import random

#Task 1
# Step 1: Create a list of 5 favorite fruits
favorite_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Grapes"]

# Step 2: Assign the list to a variable called word_list
word_list = favorite_fruits

# Step 3: Print out the newly created list
print(word_list)

#Task 2
# Step 1: Create a random word from the word_list
word = random.choice(word_list)

#step 2
print(word)

# Task 3: Take user input
# Step 1: Using the input function, ask the user to enter a single letter.
guess = input("Please enter a single letter: ")

# Step 2: Assign the input to a variable called guess.
print(f"You entered: {guess}")

# Task 4: Check that the input is a single letter
# Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    # Step 2: In the body of the if statement, print a message that says "Good guess!".
    print("Good guess!")
else:
    # Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
    print("Oops! That is not a valid input.")