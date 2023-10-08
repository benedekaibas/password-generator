import random
#import re 
#lists that we can get the data from 
letters = ["A", 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','<',',','>','.','?','/']
#converting letters to string so we can lower the letters
def toString():
    letters_string = str(letters)
    small_letters = letters_string.lower()
    return small_letters
#function that can multiply by random numbers
result = random.choice(letters)
print(result)

#get random characters from letters
def random_letters():
    new = random.choice(letters) + random.choice(letters)
    multiply = new
    return multiply
print(random_letters())

#get random characters from lower letters
def lower_letters():
    new = random.choice(toString())
    multiply = new
    return multiply
print(lower_letters())
#get random characters from symbols
def random_symbols():
    new = random.choice(symbols) + random.choice(symbols)
    multiply = new
    return multiply
print(random_symbols())

#store the functions 

def store():
    storage = random_letters() + lower_letters() + random_symbols()
    #while len(storage) > 10:
        #print(storage)
    return storage

print(f"the password is: {store()}")



