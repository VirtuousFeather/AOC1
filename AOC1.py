#PART 1
"""
file = open("input.txt").read()
reesplit = file.split('\n')

numbers = [int(s) for s in reesplit]
higherValues = 0

for i in range(len(numbers)-1):
    print("Comparing", numbers[i], "with", numbers[i+1])
    if numbers[i] < numbers[i+1]:
        higherValues +=1
print(higherValues)

# range(100) = [0, 1, 2, 3, 4, 5, 6, 7, 8, ....., 98, 99]

# for x in [1,5,7,4,2,3,7,5,3,2,4,7,8,8,4]:
#     print(x)


exit()
"""
#A + B + C < B + C + D

#PART2

file = open("input.txt").read()
reesplit = file.split('\n')

numbers = [int(s) for s in reesplit]
higherValues = 0

for i in range(len(numbers)-3):
    print("Comparing", numbers[i], "with", numbers[i+3])
    if numbers[i] < numbers[i+3]:
        higherValues +=1
print(higherValues)

# range(100) = [0, 1, 2, 3, 4, 5, 6, 7, 8, ....., 98, 99]

# for x in [1,5,7,4,2,3,7,5,3,2,4,7,8,8,4]:
#     print(x)


exit()