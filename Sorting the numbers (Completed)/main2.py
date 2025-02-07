# Asking user for 5 numbers
fst_num = int(input("Enter the first number: "))
snd_num = int(input("Enter the second number: "))
trd_num = int(input("Enter the third number: "))
fourth_num = int(input("Enter the fourth number: "))
fifth_num = int(input("Enter the fifth number: "))

# Adding all of the numbers in a list 
sorted = [fst_num, snd_num, trd_num, fourth_num, fifth_num]

# Using two for loop - i and j are variables
for i in range(0, 5): # i is starting from the first number
    for j in range(i+1, 5):
        #print(i, j) # j is starting from 2nd number
        if sorted[i] > sorted[j]: # checking if i is bigger than j
            temp = sorted[i] # temprory variable stroing a value
            sorted[i] = sorted[j] # changing the smaller number postion
            sorted[j] = temp # changing the bigger number postion

print(sorted) # Printing it