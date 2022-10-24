import random
color = random.choice(["red","yellow","green","black","white"])
guess = input("[red|yellow|green|black|white] please pick a color\n")
while color != guess:
    if color == "red":
        print("The sky is red today")
        guess = input("[red|yellow|green|black|white] please pick a color again\n")
    elif color == "yellow":
        print("bananas are yellow")
        guess = input("[red|yellow|green|black|white] please pick a color again\n")
    elif color == "black":
        print("i like black")
        guess = input("[red|yellow|green|black|white] please pick a color again\n")
    elif color == "green":
        print("the leaves are green")
        guess = input("[red|yellow|green|black|white] please pick a color again\n")
    elif color == "white":
        print("the clouds are white")
        guess = input("[red|yellow|green|black|white] please pick a color again\n")
print("Well done")