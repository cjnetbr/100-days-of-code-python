#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#passo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

#passo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ")

#passo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
