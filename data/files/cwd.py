#OS
import os

#Defining cwd function
def cwd():
    path = os.getcwd()
    print (f"The current working directory is {path}")
    print (f"The directory contains the following:")
    for file in os.listdir(path):
        print (file)

#Defining run function
def run():
    print ("Prosessing...")
    cwd()

#Call first function

if __name__ == "__main__":
    run()


