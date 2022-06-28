import random

num = random.randint(0, 10)

if num == 0:
    print ('zero')
elif num%2 == 0:
    print ("%s is even" %num)
else:
    print ("%s is odd" %num)
