#This is a guess the number game
import random
secretNumber = random.randint(1,50)
print ('I am thinking of a number between 1 and 50.')

# Ask the player to guess 6 times
for guessesTaken in range(1,7):
    print ('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess was too high')
    elif guess < secretNumber:
        print ('Your guess was too low.')
    else:
        break

if guess == secretNumber:
    print ('Good job you guessed my number in '  + str(guessesTaken) + ' guesses!!')
else:
    print ('Nope, the number i was thinking of was ' + str(secretNumber))
