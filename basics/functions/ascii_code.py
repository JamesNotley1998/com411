def get_name():
    print ("Please enter your name")
    name = input()
    return name

def display_name():
    print (f"*** {get_name()} ***")

display_name()









def get_weight():
    print("Please enter weight")
    weight = float(input())

def get_height():
    print ("What is your height")
    height = float(input())

bmi = weight / (height ** 2)
print (f"{name} your BMI is {bmi}")
