# Asking user for 5 numbers 
fst_num = int(input("Enter the first number: "))
snd_num = int(input("Enter the second number: "))
trd_num = int(input("Enter the third number: "))
fth_num = int(input("Enter the fourth number: "))
fifth_num = int(input("Enter the fifth number: "))

# storing the first number in a list 
sorted = [fst_num]

# Code for the Second Number
if snd_num > fst_num:
    sorted.append(snd_num) # If 2nd is bigger than 1st add it to the last
elif snd_num < fst_num:
    sorted = [snd_num, fst_num] # If smaller it will come first
else:
    sorted = [fst_num, snd_num] # If equal last

# Third Number 
if trd_num > sorted[0]:
    if trd_num > sorted[1]:
        sorted.append(trd_num)
    elif trd_num < sorted[1]:
        sorted.append(None)
        sorted[-1] = sorted[-2]
        sorted[-2] = trd_num
    else:
        sorted.append(None)
        sorted[-1] = sorted[-2]
        sorted[-2] = trd_num
elif trd_num < sorted[0]:
    sorted.append(None)
    sorted[-1] = sorted[-2]
    sorted[-2] = sorted[-3]
    sorted[-3] = trd_num
else:
    sorted.append(None)
    sorted[-1] = sorted[-2]
    sorted[-2] = sorted[-3]
    sorted[-3] = trd_num

# Fourth Number 
if fth_num > sorted[0]:
    if fth_num > sorted[1]:
        if fth_num > sorted[2]:
            sorted.append(fth_num)
        elif fth_num < sorted[2]:
            sorted.append(None)
            sorted[-1] = sorted[-2]
            sorted[-2] = fth_num
        else:
            sorted.append(fth_num)
    elif fth_num < sorted[1]:
        sorted.append(None)
        sorted[-1] = sorted[-2]
        sorted[-2] = sorted[-3]
        sorted[-3] = fth_num
    else:
        sorted.append(None)
        sorted[-1] = sorted[-2]
        sorted[-2] = sorted[-3]
        sorted[-3] = fth_num
elif fth_num < sorted[0]:
    sorted.append(None)
    sorted[-1] = sorted[-2]
    sorted[-2] = sorted[-3]
    sorted[-3] = sorted[-4]
    sorted[-4] = fth_num
else:
    sorted.append(None)
    sorted[-1] = sorted[-2]
    sorted[-2] = sorted[-3]
    sorted[-3] = sorted[-4]
    sorted[-4] = fth_num

# Fifth Number 
if fifth_num > sorted[0]:
    if fifth_num > sorted[1]:
        if fifth_num > sorted[2]:
            if fifth_num > sorted[3]:
                sorted.append(fifth_num)
            elif fifth_num < sorted[3]:
                sorted.append(None)
                sorted[-1] = sorted(-2)
                sorted[-2] = fifth_num
            else:
                sorted.append(fifth_num)
        elif fifth_num > sorted[2]:
            sorted.append(None)
            sorted[-1] = sorted[-2]
            sorted[-2] = sorted[-3]
            sorted[-3] = fifth_num
        else:
            sorted.append(None)
            sorted[-1] = sorted[-2]
            sorted[-2] = sorted[-3]
            sorted[-3] = fifth_num
    elif fifth_num < sorted[1]:
        sorted.append(None)
        sorted[-1] = sorted[-2]
        sorted[-2] = sorted[-3]
        sorted[-3] = sorted[-4]
        sorted[-4] = fifth_num
    else:
        sorted.append(None)
        sorted[-1] = sorted[-2]
        sorted[-2] = sorted[-3]
        sorted[-3] = sorted[-4]
        sorted[-4] = fifth_num
elif fifth_num < sorted[0]:
    sorted.append(None)    
    sorted[-1] = sorted[-2]
    sorted[-2] = sorted[-3]
    sorted[-3] = sorted[-4]
    sorted[-4] = sorted[-5]
    sorted[-5] = fifth_num
else:
    sorted.append(None)    
    sorted[-1] = sorted[-2]
    sorted[-2] = sorted[-3]
    sorted[-3] = sorted[-4]
    sorted[-4] = sorted[-5]
    sorted[-5] = fifth_num

print("\n", sorted)