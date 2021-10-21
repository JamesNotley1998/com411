#How many cables to avoid
print ("How many live cables must I avoid?")
live_cables_to_avoid = int(input())

#Declare control variable
cables_avoided = 0

#Avoid cables
print()

while cables_avoided < live_cables_to_avoid:
    print ("Avoiding...", end="")
    cables_avoided = cables_avoided +1
    print ("...Done! {cables_avoided} live cables avoided. ")
else:
    print ("All live cables have been avoided.")
