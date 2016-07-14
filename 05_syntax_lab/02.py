from random import randint
randint(1, 100)
numbers = [randint(1, 100) for i in range (7)]
n = sum(numbers)
print (numbers, n,)
if n%7==0:
    text = "boom divid by 7"
    print text.title()




