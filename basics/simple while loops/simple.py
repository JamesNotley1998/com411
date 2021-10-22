#Display 'How many cables'
print ("How many cables should I use?")
cables_to_remove = int(input())

cables_removed = 0

while cables_removed < cables_to_remove:
    print ("Removed Cable")
    cables_removed = cables_removed + 1