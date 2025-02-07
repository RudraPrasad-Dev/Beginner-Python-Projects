'''Just Run the Code '''

try:
    array = []
    def findTriplets():
        # N value and the array 
        n = int(input("Number of elements (3 or greater than 3): ")) # N Value
        if n >= 3:
            None
        else:
            return print("It should be 3 or more than 3")

        for i in range(n):
            array.append(int(input(f"Enter the {i+1} Element: "))) # Asking for Numbers for array
        
        # Adding all the possible ways 
        sum = 0
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    sum =  (array[i] + array[j] + array[k])
                    # Checking such triplets 
                    if sum == 0:
                        break
                if sum == 0:
                    break
            if sum == 0:
                break

        # Printing accordingly
        if sum != 0:
            return print("0 Possibilities")
        else:
            return print(f"\n Array:- {array} \n Sum:- {array[i]} + {array[j]} + {array[k]}")

    findTriplets()
except ValueError:
    print("Enter a valid input")
