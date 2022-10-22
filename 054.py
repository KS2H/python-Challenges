import random
ht = random.choice(["h","t"])
answer = input("enter a head or tails (h/t)")
if ht == answer:
    print("You win")
else:
    print("Bad luck")