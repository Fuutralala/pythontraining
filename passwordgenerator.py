# imports the random module
import random
# sets all the letters, signs n shit
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# tells us how long our password will be
passlen = 36
# takes all the letters and signs we gave it in the string
# random.sample makes it take as much stuff from the string we need
# to reach our passlen from string s
p = "".join(random.sample(s,passlen))
# prints out the suggested password
print(p)
