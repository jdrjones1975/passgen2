#!/usr/bin/env python3
import random
import os
import string

ver = 0.02

specChars = '!@#$%^&*()-=_+,.<>?/\| '
charset = string.ascii_letters + string.digits + specChars

#TODO
#add increaseentropy function option to diceWare

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
        generated_pwd = diceWare()
        copyOption(generated_pwd)
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


def dice_seq(seq_length):
    '''
    Generate sequence of dice roll, returns int of seq_length
    dice_seq(seq_length)
    '''
    return ''.join( [str(random.randint(1, 6)) for _ in range(seq_length)] )

def diceware_seq(ware_length, seq_length):
    '''
    Generate diceware sequences, return a list of dice sequences
    '''
    return [dice_seq(seq_length) for _ in range(ware_length)]

def diceWare():
    '''
    Ask user for desired word length
    Generate $length of diceroll sequence
    Generate password from given diceroll sequence
    return password
    '''
    
    try:
        word_length = int(input("Input your desired number of words: "))
    except ValueError:
        print ("Invalid input, fallback to default length of 5")
        word_length = 5

    SEQ_LENGTH = 5 # dicewaremaster only has index of 5 digits

    ware = {ware_seq : 0 for ware_seq in diceware_seq(word_length, SEQ_LENGTH)} # initializa a dictionary of indexes with value of 0

    with open('./dicewaremaster.txt', 'r') as f: # open dicewaremaster file
        for line in f.readlines():
            index, word = line.split()
            
            if index in ware:
                ware[index] = word

    password = ' '.join( [val for val in ware.values()] )
    print('Password generated: {}'.format(password))

    return password

def diceware_about():
    print("Diceware™ is a method for picking passphrases that uses dice to select words at random from a special list called the Diceware Word List.")
    print("Learn more about diceware at http://world.std.com/~reinhold/diceware.html")

def copyOption(element):
    '''Prompt user to confirm copy password to clipboard'''
    copy = input("type 'y' to copy this password to the clipboard: ")
    if copy == 'y':
        os.system("echo '%s' | pbcopy" % element) # This does not work on linux
        print (element, "is in the clipboard")

if __name__ == '__main__':
    introduction()
    while True:
        menu()

