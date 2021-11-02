def get_name():
    print ("Please enter your name")
    name = input()
    return name

def display_name(name):
    print (f"*** {name} ***")

name = get_name()
display_name(name)
