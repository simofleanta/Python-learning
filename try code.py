import random

def get_guess():
    
    return list(input("What is your guess?"))

def generate_code():
    
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]

def generate_clues(code,userGuess):
    
    
#https://gist.github.com/haridutt12/ec7a594c70ab41ce282e4d97e5dd1873
    for ind,num in enumerate(userGuess):
        if num == code[ind]:
            clues.append("Match")
        elif num in code:
            clues.append("Close")
        if clues == []:
            return ["Nope"]
        else:
            return clues
print("Welcome Code Breaker! Let's see if you cint(guess[2]) == digits[2] oran guess my 3 digit number!")


secretCode = generate_code()
print("Code has been generated, please guess a 3 digit number")

ClueReport= []

while ClueReport != "CODE CRACKED":
    guess = get_guess()

ClueReport = generate_clues(guess,secretCode)
print("Here is the result of your guess:")
for clue in ClueReport:
    print(clues)


    
    
    



    







