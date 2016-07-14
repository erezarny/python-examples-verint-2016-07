
from random import randrange
number = randrange(1000) # from 0 to 9 and 10 is not included
print number
x = number % 10
y = (int(number) / 10) 
z = y / 10
f = number % 100
w = f / 10
m = int (w + x + z)
print x
print z
print w
print m