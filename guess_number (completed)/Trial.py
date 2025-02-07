from random import randint

score = 2
comp = randint(1, 100)
while True:
    user = input("Guess The Number: ")
    print(comp)


    if comp > int(user):
        print("You are smaller")

    if comp < int(user):
        print("You are bigger")

    if user == str():
        print("Ok, we will play next time")

    if int(user) == comp:
        print("You are Right the number is " + str(comp))
        break
        
    user = input("Guess The Number: ")
    score = score - 1

    if score == 0:
        print("Out Of Chance, Better Luck Next Time")
        break

s = open('hiscore.txt')
old_score = s.read()

if  score < int(old_score) :
    with open('hiscore.txt', 'w') as hs:
        hs = hs.write(str(score))