import random 
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbol = '()[]{};_#@.$&'
number = '0123456789'

all = lower + upper + number + symbol
lenght = 10
password = "".join(random.sample(all,lenght))
print("The Generated Password is : ",password)