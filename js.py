# Let’s say I give you a list saved in a variable:#even
numbers3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

numbers4 = list(filter(lambda x: (x % 2 == 0), numbers3))
numbers4


   