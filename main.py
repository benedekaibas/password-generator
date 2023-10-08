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

#get random characters from letters
def random_letters():
    new = random.choice(letters)
    multiply = new * 8
    return multiply
print(random_letters())







