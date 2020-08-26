def generate_code():
    """
    generates a 3 digit list for the code
    """
    digits = list(range(10))
    random.shuffle(digits)
    print(digits[:3])
    
    return digits[:3]


def get_guess():
    """ ask for a number guess """
    guess = input("What is your guess? ")
    
    return guess
get_guess()

if get_guess in (digits[:3]):
  print("Match")
elif get_guess not in (digits[:3]):
  print("Close")
else:
  print("None")

