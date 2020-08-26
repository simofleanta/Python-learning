import random


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


def generate_clues(code, userGuess):
    if code==userGuess:
        return "correct"

clues = []

for ind, num in enumerate(userGuess):
    if num== code[ind]:
        clues.append("Match")
    elif num in code:
        clues.append("Close")
    if clues == []:
        return ["None"]
    else:
        return clues
        

    
    
