#Distance from the cave
print("How far are we from the cave?")
distance_from_cave = int(input())

# Display count down
print()

for count in range(distance, 0, -1):
    print(f"{count} steps remaining")

print("We have reached the cave!")