import random

def get_guess():
    
    return list(input("What is your guess?"))

def generate_code():
    
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,userGuess):
    
    if userGuess == code:
        return "CODE CRACKED"

    clues = []

    
    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
    if clues == []:
        return ["Nope"]
    else:
        return clues