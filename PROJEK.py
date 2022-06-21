import random
import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.YELLOW+Back.BLUE+'******************** Welcome To Your Passsword Generator *********************')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*?0123456789'

number = input('Amount of Passwords to generate : ')
number = int(number)

length = input('Input your password length : ')
length = int(length)

print(Fore.BLUE+Back.YELLOW+'\nHERE ARE YOUR PASSWORDS : ')

for pwd in range(number):
    passwords =  ' '
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
    

    


    
    

    

