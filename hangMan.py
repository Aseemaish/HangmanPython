import random       # Importing the random module
from hangman_art import logo    # Importing the logo from hangman_art.py
from hangman_art import stages  # Importing the stages from hangman_art.py

from hangman_words import word_list  # Importing the word_list from hangman_words.py
print(logo)     # Printing the logo
print("Welcome to the Hangman Game!")   # Printing the welcome message
chosen_word = random.choice(word_list)  # Choosing a random word from the word_list
#print(f"Pssst, the solution is {chosen_word}.")  # Printing the chosen word. Uncomment this if having trouble in debugging.
display = []    # Creating an empty list
lives = 6   # Setting the number of lives to 6
for _ in range(len(chosen_word)):   # Looping through the length of the chosen_word
    display += "_"  # Adding "_" to the display list
print(display)  # Printing the display list
end_of_game = False     # Setting the end_of_game to False
while not end_of_game:      # Looping until end_of_game is True
    guess = input("Guess a letter: ").lower()       # Taking the input from the user
    if guess in display:    # Checking if the guess is already in the display list
        print(f"You've already guessed {guess}")    # Printing the message
    for i in range(len(chosen_word)):   # Looping through the length of the chosen_word
        if guess == chosen_word[i]:     # Checking if the guess is equal to the chosen_word at index i
            display[i] = guess  # Changing the display list at index i to guess
    if guess not in chosen_word:    # Checking if the guess is not in the chosen_word
        print(f"You guessed {guess}, that's not in the word. You lose a life.")   # Printing the message
        lives -= 1  # Decreasing the lives by 1 if the guess is not in the chosen_word
        if lives == 0:  # Checking if the lives are 0 to end the game
            end_of_game = True
            print("You lose")
            break
    print(f"{' '.join(display)}")   # Printing the display list with spaces
    print(f"Lives: {lives}")    # Printing the lives
    if "_" not in display:  # Checking if "_" is not in the display list
        print("You win.")   # Printing the message
        end_of_game = True  # Ending the game
    print(stages[lives])    # Printing the stages according to the lives
