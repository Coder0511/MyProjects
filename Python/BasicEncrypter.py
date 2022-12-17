#BEGINNER LEVEL


#I wrote a basic program to encrypt and decrypt a message without private or public keys.

import os

#Function:
def checkOption(option):
    isDigit = False
    while isDigit == False:
        if option.isdigit() == True:
            option = int(option)
            return option
        else:
            print("Please try again.\n")
            print("Choose an option:")
            print("1. Encrypt")
            print("2. Decrypt\n")
            print("Option: ", end="")
            option = input()

#Main code:

print("Greetings, this is an encrypting and decrypting program, feel free to use it whenever you want.\n")
print("Choose an option: ")
print("1. Encrypt")
print("2. Decrypt\n")
print("Option: ", end="")
choice = input()

option = checkOption(choice)

while ((option > 2) or (option < 1)):
    print("Please try again.\n")
    print("Choose an option:")
    print("1. Encrypt")
    print("2. Decrypt\n")
    print("Option: ", end="")
    choice = input()
    option = checkOption(choice)

print("Paste your text here: ", end="")
text = input()
output = ""
    
if (option == 1):
    for i in text:
        if (i == " "):
            output += i
        else:
            unicode = ord(i)
            output += chr(unicode + 7)

else:
    for i in text:
        if (i == " "):
            output += i
        else:
            unicode = ord(i)
            output += chr(unicode - 7)
            
print(output)
os.system("pause")
