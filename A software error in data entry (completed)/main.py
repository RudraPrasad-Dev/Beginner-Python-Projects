# 1. Taking the n value and names
names = [] # Original
fNames = [] # Formatted

def solvingError(): # 27 Lines
    n = int(input("The number of institutes: "))
    print("Type the institute name(s) here:")
    for i in range(n): 
        names.append(input(f"{i+1}."))

# 2. Removing 'MGPT' from the names 
    for item in names:
        # 2A. Checking mgpt in the names 
        if 'mgpt' in item.lower():
            mgptRemover(item, fNames)
        else:
            fNames.append(item)

# 3. Alphabetical Order
    for i in range (0, n):
        for j in range(i+1, n):
            if (fNames[i] > fNames[j]): # We can compare the letters 
                temp = fNames[i]
                fNames[i] = fNames[j]
                fNames[j] = temp

# 4. Printing all of the formatted names                  
    for i in range(0, n):
        if i == 0:
            print(f"\n{i+1}.{fNames[i]}")
        else:
            print(f"{i+1}.{fNames[i]}")

def mgptRemover(name, listToStore): # 30 lines
    # 2B. Checking the 'mgpt' place value 
    nameLen = len(name)
    checkStr = ""
    for m in range(0, nameLen):
        for g in range(m+1, nameLen):
            for p in range(g+1, nameLen):
                for t in range(p+1, nameLen):
                    checkStr= f"{name[m]}{name[g]}{name[p]}{name[t]}"

                    if checkStr.lower() == 'mgpt' and (m-t) == -3:
                        break
                if checkStr.lower() == 'mgpt' and (m-t) == -3:
                    break
            if checkStr.lower() == 'mgpt' and (m-t) == -3:
                break
        if checkStr.lower() == 'mgpt' and (m-t) == -3:
            break
    
    # 2C. Removing 'mgpt' from the names 
    formattedStr = '' # Empty String
    if checkStr.lower() == 'mgpt':
        for letter in range(0, nameLen):
            if letter== m or letter== g or letter== p or letter== t: 
                None
            elif letter != m or letter != g or letter != p or letter != t:
                formattedStr = formattedStr+name[letter]

    return listToStore.append(formattedStr)

solvingError()