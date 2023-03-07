import random
#color guessing game
colors = ["Blue","Purple","Red","Gray","Black","White"]
random_color = random.choice(colors)
print(colors)
while True:
    picked = input("Pick a color from the list: ")
    if picked != random_color:
        print("You should try again !")
    else:
        print("You got it right !")
        break
