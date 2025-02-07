from random import randint

# Asks user to choose anything and computer to choose
pl = input("What you will choose to beat me\n Snake(s) Water(w) Gun(g): ")
com = randint(1, 3)

# Converts computer's random number to a decision 
if com == 1:
    com = 's'
elif com == 2:
    com = 'w'
elif com == 3:
    com = 'g'
print(com)  

# It's game's rule 
if pl == "s" and com == 'w':
    print("You Win!")
   
elif pl == "w" and com == 'g':
    print("You Win!")

elif pl == "g" and com == 's':
    print("You Win!")

elif pl == com:
    print("Tie")

else:
    print("Ha, Ha, I won")        