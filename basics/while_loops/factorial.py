#Ask user for number
print ("Please enter a number")
number = int(input())

#Factorial variable
count = 0
total = 1

while count < number:
    count = total + 1
    total = total * count

print(f"The factorial is {total}.")



