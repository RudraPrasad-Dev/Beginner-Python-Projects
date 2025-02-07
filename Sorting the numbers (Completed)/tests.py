# To check whether we can change a list to another list 
# list1 = [10, 98]
# list2 = [10]
# list1[0] = list1[1] 
# print(list1)
# print(list2)

# for i in range(0, 5):
#     print(i)

# l = [45, 454, 5 ,56]

# for i in l:
#     print(i)

l = [45, 454, 5 ,56]

for i in range(0, len(l)):
    for j in range(i+1, (len(l))):
        print(i, j)
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print(l)
print(len(l))

'''temp = 454
   l[1] = 5 - [45, 5, 5, 56]
   l[2] = 454 - [45, 5, 454, 56]
   
   temp = 454
   l[2] = 56 - [45, 5, 56, 56]
   l[3] = 454 - [45, 5, 56, 454]
   
   temp = '''
   