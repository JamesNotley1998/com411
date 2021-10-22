#Numbers to add up
print ("How many numbers should I sum up?")
number_to_sum = int(input())

#Control Variable
summed = 0

#Display blank link
print ()

#Sum numbers
total = 0

while summed < number_to_sum:
    print (f"Please enter number {summed} of {number_to_sum}:")
    number = int(input())
    total = total + number
    summed = summed + 1

#Display result
print (f"The answer is {total}.")
