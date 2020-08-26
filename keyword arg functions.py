def my_function(c0,c1,c2,c3,c4,c5):
    print("hello from " + c2)
my_function(c0="FR",c1="Ger",c2="Dk",c3="Nth",c4="KR",c5="BG")


def my_function(**country):
    """This function tells where I am from using multiple keywordargs"""
    print("hello from " + country["city"], country['name'],country['hub'])
my_function(city="Paris",name="FR", hub="Impacthub")


def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable #operating a function

print(variable_test())# printing the result


def savings(mutualfunds,work,trading,spending):
    return mutualfunds + work + trading - spending
print (savings(20,200,100,50))

def my_f(x):
    """this function finds or returns value of x"""
    return 5*x
print (my_f(3))
print(my_f(5))

def my_f(x,y):
    return x/y
print(my_f(30,6))

def f(x):
    return x**2-30
print (f(6))

def variable_test():
    first_variable = 10
    second_variable = 20
    return first_variable * second_variable #operating a function

print(variable_test())# printing the result

def f(x,y):
    return x*y
print (f(10,20))


my_points=1000
message='I scored %s points'
print(message % my_points)


flattened_cans=100
cans="we've flttened %s cans"
print(cans % flattened_cans)

age=30
if age >= 10 and age <= 13:
    print('what is 13 + 49 + 84 + 155 + 97? mno!')
else:
    print('huh?')
    
    
def silly_joke(age):
    if age >= 10 and age <= 13:
        print('what is 13 + 49 + 84 + 155 + 97? headache!')
    else:
        print('huh?')
        
   