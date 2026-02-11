R = input ("input Radius of a circle")
R = int (R)
Area = 22.0/7 * R * R
Area = int (Area)
primetre = 2*22.0/7.0 * R
primetre = int (primetre)
print (Area,'is your area and',primetre,'is your primetre')

P = input ('input your principle number')
P = float (P)
N = input ('input your time in years')
N = float (N)
R1 = input ('input your annual rate of interest')
R1 = float (R1)
SI = (P * N * R1)/100.0
SI = float (SI)
print ('your simple interest is',SI)

num1 = input ('enter your first number')
num1 = float (num1)
num2 = input ('enter your second number')
num2 = float (num2)
if (num1 < num2):
    print ('the smaller number is your first number')
if (num1 > num2):
    print ('the smaller number is second number')
    
    
    
A = input ('what age are you')
A = int (A)
if (A >=18):
     print ('elligible for role')
if (A <= 18):
    print ('you are NOT elligible for the role')
    
