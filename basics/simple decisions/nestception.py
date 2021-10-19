# Display where to look
print("Where should I look?")
place = input()

# Check the bedroom
if place == "bedroom":
    print ("Where in the bedroom should I look?")
    bedroom_place = input()

    if bedroom_place == "under the bed":
        print ("Found some shoes but no battery")
    else:
        print ("Found some mess but no battery")

# Check the bathroom
elif place == "bathroom":
    print ("Where in the bathroom should I look?")
    bathroom_place = input()

    if bathroom_place == "in the bathtub":
        print ("Found a rubber duck but no battery")
    else:
        print ("Found a wet surface but no battery")

# Check the Lab
elif place == "lab":
    print ("Where in the lab should I look?")
    lab_place = input()

    if lab_place == "on the table":
        print ("Yes! I found my battery!")
    else:
        print ("Found some tools but no battery")

else:
    print ("I do not know where that is but I will keep looking")


