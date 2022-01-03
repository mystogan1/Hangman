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

end_of_game = False
word_list = ['school', 'classroom', 'curriculum', 'chalkboard', 'homework', 'lesson', 'study ', 'lecture ', 'student', 'teach',
             'educational', 'students', 'classes', 'kindergarten', 'dormitory', 'teacher', 'math', 'education', 'playground', 'semester', ]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# random index number from chosen_word
index_no = random.randrange(word_length)
random_letter = chosen_word[index_no]
# Create blanks
display = []
for _ in range(word_length):
    display += "_"


print('''
                Welcome to the hangman.py
                all words are school related
''')

# display with hints
for pos in range(word_length):
    letter = chosen_word[pos]
    if letter == random_letter:
        display[pos] = letter

print(display)


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('''
                        YOU_LOSE

            ''')
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print('''
                        YOU_WIN

            ''')

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
