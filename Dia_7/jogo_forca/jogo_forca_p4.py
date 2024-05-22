#Step 1 

word_list = ["aardvark", "baboon", "camel"]


#passo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

lives = 6

word = []
for letter in chosen_word:
  word.append("_")
print(word)

#passo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
w_len = len(chosen_word)
end_game = False

while not end_game:

  guess = input("Guess a letter: ")

  #passo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

  for i in range(w_len):
    letter = chosen_word[i]
    if letter == guess:
      word[i] = letter
    
  if guess not in chosen_word:
    lives -= 1
    
  if lives == 0:
    print("You lose.")
    end_game == True
      
  print(word)
  
  if "_"  not in word:
    end_game = True
    print("You win")
    
  print(stages[lives])
