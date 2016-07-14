from random import randint
x = randint(1,10)
print x
y = randint(1,10) 
print y
for i in range(2,(x*y)+2):
    if (x%i == 0) and (y%i == 0):
        print i 
        break  

