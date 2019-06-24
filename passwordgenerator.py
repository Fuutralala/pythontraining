import random
import string

# function to generate strong password
# params{int} length of password
# returns{String} random strong password 
def generateStrongPassword(length):
    randomChars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(randomChars) for i in range(0, length))


def generateWeakPassword():
    defaultPass = ['0123456789', '123456', 'abcdef', 'qawseedrf']
    return random.choice(defaultPass)


answer = input('Do you want a strong or weak password?\n')
if answer == 'strong':
    length = int(input('How long should it be?\n'))
    print('Your strong password is ', generateStrongPassword(length))
elif answer == 'weak':
    print('Your weak password is ', generateWeakPassword())
else:
    print('ERROR, you have typed a wrong word, please try again typing "strong" or "weak".')
