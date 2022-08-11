#This program is the starter code for the Programming Caesar's Cipher Project. 
# This code is inspired by Cracking Codes with Python: An Introduction to Building and Breaking Ciphers by Al Sweigart https://www.nostarch.com/crackingcodes (BSD Licensed)

# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
intialPosition = 0
shiftedPosition = 0
shiftedMessage = " "

# Run code

# Introduction
print("\033[1;35;40mWelcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters:\033[0m " + possibleCharacters + "\033[1;35;40m\n\nLet's get started!\n")

# Receive user input
initialMessage = input("What is your message?\033[0m ")
key = int(input("\033[1;35;40mWhat is the key? Choose a number from 0 to 25.\033[0m "))
          
mode = input("\033[1;35;40mDo you want to encrypt or decrypt the message?\033[0m ")
# Encrypt or decrypt the message
for character in initialMessage:
  if character in possibleCharacters:
    intialPosition = possibleCharacters.find(character)
  
    if mode.lower() == "encrypt":
      shiftedPosition = intialPosition + key
  
    elif mode.lower() == "decrypt":
      shiftedPosition = intialPosition - key
  
    if shiftedPosition >= len(possibleCharacters):
      shiftedPosition = shiftedPosition - len(possibleCharacters)
  
    elif shiftedPosition < 0 :
      shiftedPosition = shiftedPosition + len(possibleCharacters)
   
    shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]
    
  else:
    shiftedMessage = shiftedMessage + character
# Print the shifted message

print("\033[1;35;40mYour " + mode.lower() + "ed message is:\033[0m " + shiftedMessage)