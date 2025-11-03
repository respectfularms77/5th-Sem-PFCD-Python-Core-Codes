import math
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

deg = float(input("Enter the Angel in Degrees: "))
n = int(input("Enter the Number of Terms: "))
x = math.radians(deg)
cos_x = 0
for i in range(n):
    power = i*2
    term = ((-1)**i) * (x**power) / fact(power)
    cos_x = cos_x + term

print("The Value of Cos x is: ",cos_x)
print("The Value of Cos x using the Math Module Directly is: ",math.cos(x))