from random import randint

number = randint(1, 100)
attempts = 0

print('''Welcome to the Game of Guess!
Here You have to guess a number based on the clues I will give after every guess
So let's start:''')

while True:
    attempts = attempts + 1
    guess = input("\nGuess The Number: ")
    score = attempts * 10

    if guess == 'q':
        print("OK, We will play next time")
        break

    elif int(guess) < number:
        print("Make a Higher Guess!")

    elif int(guess) > number:
        print("Make a Lower Guess!")

    else:
        print(f"You Guessed! The Number was {number}\nYou guessed in {attempts} attempt(s)\nYour score is {score}")
        break
        
print("Thanks for Playing")

s = open('highscore.txt')
old_score = s.read()

if score < int(old_score) :
    with open('highscore.txt', 'w') as hs:
        hs = hs.write(str(score))