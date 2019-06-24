import random
import string
# function to generate strong password
stringLength = int(input("Enter how long your password should be: \n>"))
def generatePassword(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
print(generatePassword(stringLength))


#import random
#import string
# function to generate strong password
#input = str(input("Enter how long your password should be: \n>"))
#def generatePassword(stringLength="input"):
#    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
#    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
#    charsUpper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
#    charsLow = "abcdefghijklmnopqrstuvwxyz"
#    charsNumber = "0123456789"
#    charsSpecial = "!§$%&/(){}[]=?#*_-"
#    password = ''
#    password += random.choice(charsUpper)
#    password += random.choice(charsLow)
#    password += random.choice(charsNumber)
#    password += random.choice(charsSpecial)
#    password += random.choice(charsUpper)
#    password += random.choice(charsLow)
#    password += random.choice(charsNumber)
#    password += random.choice(charsSpecial)
#    return ''.join(random.choice(password_characters) for input in range(stringLength))
#print(generatePassword())
#def generateWeakPassword():
#    defaultPass = ['0123456789', '123456', 'abcdef', 'qawseedrf']
#    return random.choice(defaultPass)

#print('Generating password 1', generateStrongPassword())
#print('Generating password 2', generateStrongPassword())
#print('Generating password 3', generateStrongPassword())
#print('Generating password 4', generateStrongPassword())

#answer = str(input('Do you want a strong or weak password? \n'))
#if answer == 'strong':
#    print('\nYour strong password is ', generateStrongPassword())
#elif answer == 'weak':
#    print('\nYour weak password is ', generateWeakPassword())
#else:
#    print('\nERROR, you have typed a wrong word, please try again typing "strong" or "weak".')
