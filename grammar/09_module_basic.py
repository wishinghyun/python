import random
#print(dir(random))
pick = random.choice(range(10))
print(pick)

pick = random.choice([1, 2, 3, 4, 5])
print(pick)

# help(random.choice)

# help(random.sample)

pick = random.sample(range(10),3)