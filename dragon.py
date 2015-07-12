# Dragon Realm game where player selects one of two caves to 
# explore for treasure. Code covers topics:
#	1. time.sleep() function
#	2. using keyword 'def' to create function
# 	3. keyword 'return'
#	4. 'and', 'or', 'not' Boolean operators
#	5. truth tables
#	6. global & local variable scope
#	7. parameters & arguments
#	8. flow charts
import random
import time

def displayIntro():
	print('You are in a land full of dragons. In front of you,')
	print('you see two caves. In one cave, the dragon is fiendly')
	print('and will share his treasure with you. The other dragon')
	print('is greedy and hungry, and will eat you on sight.')
	print()
	
def chooseCave():
	cave = ''
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()
		
	return cave
def checkCave(chosenCave):
	print('You approach the cave...')
	time.sleep(2)
	print('It is dark and spooky...')
	time.sleep(2)
	print('A large dragon jumps out in front of you! He opens his jaws and ...')
	print()
	time.sleep(2)
	
	friendlyCave = random.randint(1,2)
	
	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
		print('Gobbles you down in one bite!')
		
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

	displayIntro()
	
	caveNumber = chooseCave()
	
	checkCave(caveNumber)
	
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	