import math as m
print('This is a square function solving machine')
a = input('Please input the coefficient of x^2:')
b = input('Please input the coefficient of x:')
c = input('Please input the coefficient of x^0:')
a = int(a)
b = int(b)
c = int(c)
A = (-b+m.sqrt(b**2-4*a*c))/(2*a)
B = (-b-m.sqrt(b**2-4*a*c))/(2*a)
print('The answer of the function is:',A,'or',B)