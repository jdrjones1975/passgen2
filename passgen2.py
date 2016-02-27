#!/usr/bin/env python3
import random
import os
import string

ver = 0.02

specChars = '!@#$%^&*()-=_+,.<>?/\| '
charset = string.ascii_letters + string.digits + specChars

def introduction():
    print('***************************************')
    print('* This is password generator ver', ver, '*')
    print('*                                     *')
    print('* Present functionality is limited    *')
    print('* to psuedorandomness.                *')
    print('* Future versions to be in a GUI.     *')
    print('***************************************')

def menu():
    print()
    print("1. Generate a random password from 1 to 64 characters.")
    print("2. Generate a diceware password.")
    print("3. Quit")
    selection = input("     Please make a selection(1-4): ")
    if selection == '1':
        generated_pwd = randomPassword(ask_length())
        copyOption(generated_pwd)
    elif selection == '2':
        diceWare()
    elif selection == '3':
        quit()
    else:
        print("Invalid choice")
        return
        

def ask_length():
    '''Ask user for password length, validate user input'''
    try:
        length = int(input("Input your desired password length (1-64): "))
    except ValueError:
        print("ValueError: Input should be integer")

    if length not in range(1, 65):
        raise ValueError("Length should be between 1 to 64") # raise exception would break while loop
        return None
    
    return length

def randomPassword(password_length):
    '''Generate random password of length password_length from charset'''
    password = ''.join((random.choice(charset) for _ in range(password_length)))
    print('Password generated: {}'.format(password))
    return password

def copyOption(element):
    copy = input("type 'y' to copy this password to the clipboard: ")
    if copy == 'y':
        os.system("echo '%s' | pbcopy" % element) # This does not work on linux
        print (element, "is in the clipboard")

def diceWare():
    '''
    Learn more about diceware at http://world.std.com/~reinhold/diceware.html
    '''
    
    print()
    print("Diceware™ is a method for picking passphrases that uses dice to select words at random from a special list called the Diceware Word List.")
    print()
    
    dic = {} #creates empty dictionary for key/values from dicewaremaster.txt
    length = 5 #begin with 5, can make this a var as input later to determine how many words returned as password
    try:
        length = int(input("Input your desired number of words: "))
    except ValueError:
        print ("ValueError, using default of 5")
    password = [] #initialize an empty password / word holder
    
    f = open('dicewaremaster.txt', 'r') #opens dicewaremaster file
    for l in f:
        '''
        writes diceware dictionary to dic
        '''
        k, v = l.split()
        if k in dic:
            dic[k].extend(v)
        else:
            dic[k] = [v]

    f.close() #closes txt file

    #initialize the five dice and roll them length times
    for i in range(0,length):
        ones = (random.randint(1,6))
        tens = 10 * (random.randint(1,6))
        huns = 100 * (random.randint(1,6))
        thous = 1000 * (random.randint(1,6))
        tenthous = 10000 * (random.randint(1,6))
        rawRoll = tenthous + thous + huns + tens + ones
        rawRoll = str(rawRoll)
        password.append(dic[rawRoll])

    flatPass = list(flatten(password))
    password = ' '.join(flatPass)
    print()
    print(password)
    print()
    #increaseentropy function option here
    copyOption(password)


def flatten(lst):
    for elem in lst:
        if type(elem) in (tuple, list):
            for i in flatten(elem):
                yield i
        else:
            yield elem

if __name__ == '__main__':
    introduction()
    while True:
        menu()
