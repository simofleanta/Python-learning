def silly_joke(age):
    if age >= 10 and age <= 13:
        print('what is 13 + 49 + 84 + 155 + 97? headache!')
    else:
        print('huh?')

silly_joke(10)
silly_joke(9)
silly_joke(7)
silly_joke(8)

import sys

def silly_joke():
    print('what is your age?')
    age=int(sys.stdin.readline())
    if age >= 10 and age <= 13:
        print('what is 13 + 49 + 84 + 155 + 97? headache!')
    else:
        print('huh?')
silly_joke()