import random
digits = list(range(10))
random.shuffle(digits[:3])

print(digits[:3])


def generate_code():
    """
    generates a 3 digit list for the code
    """
    digits = list(range(10))
    random.shuffle(digits[:3])
    print(digits[:3])
    
    return digits


def get_guess():
    """ ask for a number guess """
    guess = input("What is your guess? ")
    
    return guess
get_guess()

def generate_clues(code, userGuess):
    pass


  

  

  

    
    
    


    



