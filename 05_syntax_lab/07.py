from random import randint
x = int(randint(1,10))
print x
y = int(input("Please enter your gess: "))
print y
if y > x:
    print ("Your number is bigger!")  
elif y < x:
    print ("Your number is smaller!")
else:
    print ("bingo!")   
