try:
    array = []
    def kthSmallestNum():
        n = int(input("Number of elements: ")) # N Value

        for i in range(n):
            array.append(int(input(f"Enter the {i+1} Element: "))) # Asking for Numbers for array

            if array[0] >=0 and array[-1] >= 0 or array[0] <=0 and array[-1] <= 0:
                None

            else:
                return print("Please Enter in array format")

        print(f"The Array : {array}")
        k = int(input("Enter the position of smallest of element you want: ")) # K value
        print("\n")
        # Sorting the numbers
        for i in range(0, n):
            for j in range (i+1, n):
                if array[i] > array[j]:
                    temp = array[i]
                    array[i] = array[j]
                    array[j] = temp
        return print(f"The Sorted Array - {array}\n The {k}th Smallest Element - {array[k-1]}")

    kthSmallestNum()
except IndexError or ValueError:
    print("You should have entered a valid input.")