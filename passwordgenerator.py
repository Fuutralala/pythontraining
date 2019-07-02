import random, string; print(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(int(input("Enter how long your password should be: \n>")))))
