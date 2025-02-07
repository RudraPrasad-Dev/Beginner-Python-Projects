try:
    def generate_fibbonaci_series(nOfSeries):
        numbers = [0, 1]

        if nOfSeries == 0:
            print([0])
        elif nOfSeries > 0: 
            while 0 < (nOfSeries-1):
                addedNO = numbers[-1] + numbers[-2] 
                numbers.append(addedNO)
                nOfSeries-=1
            print(numbers)
        else:
            while 0 > (nOfSeries+1):
                addedNO = numbers[-2] - numbers[-1] 
                numbers.append(addedNO)
                nOfSeries+=1
            output = (str(numbers)).replace(("[", "]"), "")
            print(output)
        

    nOfSeries = int(input("Enter the number of series: "))
    generate_fibbonaci_series(nOfSeries)
except ValueError as v:
    print("Invalid Value")