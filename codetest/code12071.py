import random

lotto_set = set({})
while len(lotto_set) < 6:
    lotto_set.add(random.randint(1, 46))
print(lotto_set)