#Step 1 

word_list = ["aardvark", "baboon", "camel"]


#passo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

word = []
for letter in chosen_word:
  word.append("_")
print(word)

#passo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
w_len = len(chosen_word)


guess = input("Guess a letter: ")

#passo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for i in range(w_len):
  letter = chosen_word[i]
  if letter == guess:
    word[i] = letter
print(word)

