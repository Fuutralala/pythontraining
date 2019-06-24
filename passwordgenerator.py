import random
import string
stringLength = int(input("Enter how long your password should be: \n>"))
def generatePassword(stringLength):
    lettersAndDigits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))
print(generatePassword(stringLength))

