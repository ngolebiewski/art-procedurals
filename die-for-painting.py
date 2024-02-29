import random

print("Make a chance derived painting based on these parameters.")
print("*" * 40)

dieNumber = int(input("how many sides do you want your die to have?: "))
numRolls = int(input("how many rolls do you want to take?: "))
colors = input("which colors will you use? (separate each with comma + space): ")

if len(colors) == 0:
	colors = "red, orange, yellow, green, blue, purple"
	
colorList = colors.split(", ")
colorLocation = 0

for x in range(1, numRolls+1):
	print(f'Roll {x}: {random.randint(1,dieNumber)} {colorList[colorLocation]}')
	colorLocation += 1
	if colorLocation == len(colorList):
		colorLocation = 0
		print("*" * 40)

