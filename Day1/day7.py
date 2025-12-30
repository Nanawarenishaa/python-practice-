import random

print("random():",random.random())

print("random Number in (1-10):",random.randint(1,10))

print("random alternative numbers:",random.randrange(1,20,2))

colors=["red","Brown","Burgundy","cyan"]

print("random chooice color:",random.choice(colors))

numbers=[1,2,3,4,5]
random.shuffle(numbers)
print("shuffled numbers in array:",numbers)


