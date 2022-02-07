
from math import sqrt

def risheh_moadele2(a,b,c):
    d=(b**2 - 4*a*c)
    if d>=0:
        x_0=(-b + sqrt(d))/(2*a)
        x_1=(-b - sqrt(d))/(2*a)
        return round(x_0,2), round(x_1,2)
    else:
        return 'risheh haghighi nadarad' 
   
x=risheh_moadele2(2,4,-3)
print(x)

