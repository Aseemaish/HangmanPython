import random
from hangman_art import logo
from hangman_art import stages
print(logo)
from hangman_words import word_list
print("Welcome to the Hangman Game!")
chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}.")
display = []
lives = 6
for _ in range(len(chosen_word)):
    display += "_"
print(display)
end_of_game = False
while not end_of_game and lives > 0:
    dash = True
    guess = input().lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
    if guess not in chosen_word:
        print(stages[lives - 1])
        lives -= 1
        if lives==0:
            end_of_game=True
            print("You lose")
            break
    print(f"{' '.join(display)}")
    print(f"Lives: {lives}")
    if "_" not in display:
        print("You win.")
        end_of_game = True