#  calculate pi
# neo ramotlou
# 15 march 2018

x = 0

fraction = 2
import math

p = 2

while x !=2:
    x = math.sqrt(x+2)
    fraction = (2/x)
    p = p*fraction
    
print('Approximation of pi:', round(p, 3))
radius = eval(input('Enter the radius: \n'))
print('Area:', round((p*(radius**2)), 3))
              