# Read in user's data
print("What is your name?")
name = input()
# Ask user how old they are
print("What is your age (in years")
# Read in users age
age = int(input())
#Ask how much they weight
print("How much do you weigh (in kilograms)?")
weight = float(input())
#Ask how tall you are
print("How tall are you (in meters)?")
height = float(input())
#Calculate BMI
bmi = weight / (height ** 2)
#Display result
print(f"{name} your bmi is {bmi}")

