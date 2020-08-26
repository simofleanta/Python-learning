import random

number = list(range(10))
digits=(number[:3])
random.shuffle(digits)
print(digits)

def get_guess():
    """ ask input"""
    guess = input("what's on your mind?")
    
    return guess

get_guess()

if get_guess in (digits):
    print("Match")
elif get_guess not in (digits):
    print("Close")
else:
    print("No")








    
   



