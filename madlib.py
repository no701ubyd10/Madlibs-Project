# random
import random
# open madlibtext file
f = open('madlibtext.txt','r')
# read file
madlibtxt = f.readlines()
madlib = random.choice(madlibtxt)
noun = input('Enter noun: ')
# replace word ioi! in txt to noun
madlib = madlib.replace('ioi!',noun)
print(madlib)