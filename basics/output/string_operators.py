#Read in bots data
print("Please enter number of lives")
lives = int(input())
print("Please enter the energy level")
energy = int(input())
print("Please enter the shield level")
shield = int(input())
print("Health has been set.")

#Display bot data
print(f"Lives: {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")