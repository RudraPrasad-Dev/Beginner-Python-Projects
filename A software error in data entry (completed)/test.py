name = "Romgptn"

# Proves that we can check 'mgpt' in the names
if 'mgpt' in name.lower():
    name = name+"u" # We can add letters to the name
    print(name)
else:
    print('no')

# Checking the place value where mgpt is 
nameLen = len(name)
checkStr = ""
for i in range(0, nameLen):
    for j in range(i+1, nameLen):
        for k in range(j+1, nameLen):
            for l in range(k+1, nameLen):
                checkStr= f"{name[i]}{name[j]}{name[k]}{name[l]}"
                if checkStr == 'mgpt':
                    break
            if checkStr == 'mgpt':
                break
        if checkStr == 'mgpt':
            break
    if checkStr == 'mgpt':
        break
        
if checkStr == 'mgpt':
    print(i, j, k, l)
    print(checkStr)

# Sorting The words
words = ["hat", "mat", "cat", 'bat', "fat"]
for i in range (0, 5):
    for j in range(i+1, 5):
        if (words[i] > words[j]): # We can compare the letters 
            temp = words[i]
            words[i] = words[j]
            words[j] = temp
print(words)