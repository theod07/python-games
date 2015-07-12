# Extension/improvement of hangman.py.
# This version allows player 2 more guesses, and uses a dictionary
# data type to store possible choices of secret word.
# Demonstrates:
#	1. dictionary data type
#	2. key-value pairs
#	3. dictionary methods keys() and values()
#	4. multiple variable assignment
import random
HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

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
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
  |   |
 / \  |
=========''', '''

  +---+
  |   |
 [O   |
 /|\  |
  |   |
 / \  |
=========''', '''

  +---+
  |   |
 [O]  |
 /|\  |
  |   |
 / \  |
=========''']
words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crap deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}

def getRandomWord(words):
	# This function returns a random string from the passed list of strings, and the key also.
	# First, randomly select a key from the dictionary:
	wordKey = random.choice(list(words.keys()))
	
	# Second, randomly select a word from the key's list in the dictionary:
	wordIndex = random.randint(0, len(words[wordKey]) - 1)
	
	return [words[wordKey][wordIndex],wordKey]
	
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
	print(HANGMANPICS[len(missedLetters)])
	print()
	
	print('Missed Letters:', end=' ')
	for letter in missedLetters:
		print(letter, end=' ')
	print()
	
	blanks = '_' * len(secretWord)
	
	for i in range(len(secretWord)): # replace blanks with correctly guessed letters
		if secretWord[i] in correctLetters:
			blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
			
	for letter in blanks: # show the secret word with spaces in between each letter
		print(letter, end=' ')
	print()
	
def getGuess(alreadyGuessed): 
	# Returns the letter the player entered. This function makes sure the 
	# player entered a single letter, and not something else.
	while True:
		print('Guess a letter.')
		guess = input()
		guess = guess.lower()
		if len(guess) != 1:
			print('Please enter a single letter.')
		elif guess in alreadyGuessed:
			print('You have already guessed that letter. Choose again.')
		elif guess not in 'abcdefghijklmnopqrstuvwxyz':
			print('Please enter a LETTER.')
		else:
			return guess
			
def playAgain():
	# This function returns True if the player wants to play again, 
	# otherwise it returns False.
	print('Do you want to play again? (yes or no)')
	return input().lower().startswith('y')
	
	
print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
	#print('The secret word is in the set: ' + secretKey)
	displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
	
	# Let the player type in a letter.
	guess = getGuess(missedLetters + correctLetters)
	
	if guess in secretWord:
		correctLetters = correctLetters + guess
		
		# Check if the player has won
		foundAllLetters = True
		for i in range(len(secretWord)):
			if secretWord[i] not in correctLetters:
				foundAllLetters = False
				break
		if foundAllLetters:
			print('Yes! The secret word is "' + secretWord + '"! You win!')
			gameIsDone = True
	else:
		missedLetters = missedLetters + guess
		
		# Check if player has guesse too many times and lost
		if len(missedLetters) == len(HANGMANPICS) - 1:
			displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
			print('You have run out of guesses!\n After ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
			gameIsDone = True
			
	# Ask the player if they want to play again (but only if the game is done).
	if gameIsDone:
		if playAgain():
			missedLetters = ''
			correctLetters = ''
			gameIsDone = False
			secretWord, secretKey = getRandomWord(words)
		else:
			break