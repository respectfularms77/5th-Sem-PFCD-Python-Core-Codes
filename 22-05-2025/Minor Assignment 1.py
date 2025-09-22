Python 3.10.12 (main, Aug 15 2025, 14:32:43) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
print(type(int('123')))
<class 'int'>
print(10.0%2)
0.0
print(10.0//2)
5.0
a="nana "
b=8
c=a*b
print(c,"Batman")
nana nana nana nana nana nana nana nana  Batman
#Q9
print("""Hi! We are studying "Python". \n I hope you all are doing well""")
Hi! We are studying "Python". 
 I hope you all are doing well
print("""Hi! We are studying "Python". \nI hope you all are doing well""")
Hi! We are studying "Python". 
I hope you all are doing well
#Q10)
value = """Name: Arpit Kumar Mohanty \nAddress: XYZ123, \nCity_AB, \nState_AB""""
SyntaxError: incomplete input
value = """Name: Arpit Kumar Mohanty \nAddress: XYZ123, \nCity_AB, \nState_AB"""
print(value)
Name: Arpit Kumar Mohanty 
Address: XYZ123, 
City_AB, 
State_AB
a=int(input("Enter the Value of A: "))
Enter the Value of A: 25
a=20
b=10
print(a+b)
30
def(c):
    
SyntaxError: invalid syntax
def function(x):
    return (x**3) + (2*x**2) + (3*x) + 4
print(function(2))
SyntaxError: invalid syntax
def function(x):
    return ((x**3) + (2*x**2) + (3*x) + 4)
print(function(2))
SyntaxError: invalid syntax
def function(x):
    return ((x**3) + (2*x**2) + (3*x) + 4)

print(function(2))
26
import math as mt
def areaC(r):
    return mt.pi*(r**2)

def voluC(r):
    return (4/3)*(mt.pi*(r**3))

rad = float(input("Enter the Value of Radius of Circle: "))
Enter the Value of Radius of Circle: 10
print("The Area of Circle is: ",areaC(rad))
The Area of Circle is:  314.1592653589793
print("The Volume of Circle is: ",voluC(rad))
The Volume of Circle is:  4188.79020478639
n = int(input("Enter the Value to Calculate the Sum of integers from 1 to n: "))
Enter the Value to Calculate the Sum of integers from 1 to n: 5
sum_n = ((n*(n+1))/2)
print(sum_n)
15.0
a=10, b=5, c=0
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=10
b=5
c=0
print((a<b) or (not(c==b) and (c<a)))
True
a=1.21

b=1.20
c=1.22
print((a<b) or (not(c==b) and (c<a)))
False
def funds(p, r, n):
    return p*(1+(r**n))

p=1000
r=12
n=10
print("Amount adding up after 10 Years: ",funds(p,r,n))
Amount adding up after 10 Years:  61917364225000
def funds(p, r, n):
    return p*(1+(r/100))**n

print("Amount adding up after 10 Years: ",funds(p,r,n))
Amount adding up after 10 Years:  3105.8482083442123
n=20
print("Amount adding up after 20 Years: ",funds(p,r,n))
Amount adding up after 20 Years:  9646.293093274951
n=20
n=30
print("Amount adding up after 30 Years: ",funds(p,r,n))
Amount adding up after 30 Years:  29959.92212091116
if(mt.e**mt.pi > mt.pi**mt.e):
    print("Ok e**PI > PI**e")

    
Ok e**PI > PI**e
else:
    
SyntaxError: invalid syntax
else:
    
SyntaxError: invalid syntax
if(mt.e**mt.pi > mt.pi**mt.e):
    print("Ok e**PI > PI**e")
else:
    print("Ok e**PI < PI**e")

    
Ok e**PI > PI**e
if(mt.e**mt.pi > mt.pi**mt.e):
    print("Ok e**PI > PI**e")
else:
    print("Ok, Anyways e**PI < PI**e")

    
Ok e**PI > PI**e
a=-7*20+8/16*2+54
b=7**2//9%3
c=(7-4*2)*10-25*8//5
d=5%10+10-25*8//5
print(a, b, c, d)
-85.0 2 -50 -25
a = "hi" > "hello" and "bye" < "Bye"
print(a)
False
b = "hi" > "hello" or "bye" < "Bye"
c = """7 > 8 or 5 < 6 and 'I am fine >'I am not fine'"""
d = 10 != 9 and 29 >=29
e = 10 != 9 and 29 >=29 and 'hi' > 'hello' or 'bye' < 'Bye' and 7 <= 2.5
f = 5 % 10 + 10 < 50 and 29 >= 29
g = 7**2 <= 5//9%3 or 'bye'<'Bye'
print(b, eval(c), d, e, f, g)
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#96>", line 1, in <module>
  File "<string>", line 1
    7 > 8 or 5 < 6 and 'I am fine >'I am not fine'
                                                 ^
SyntaxError: unterminated string literal (detected at line 1)
amount = int(input("Enter the Value of the Meal ordered to get the Total Amount including Tax and tip: ")
             
KeyboardInterrupt
amount = int(input("Enter the Value of the Meal ordered to get the Total Amount including Tax and tip: "))
             
Enter the Value of the Meal ordered to get the Total Amount including Tax and tip: 1200
tax = amount*0.05
             
tip = amount*0.18
             
total = round((amount+tax+tip), 2)
             
print(total)
             
1476.0
amount = int(input("Enter the Value of the Meal ordered to get the Total Amount including Tax and tip: "))
             
Enter the Value of the Meal ordered to get the Total Amount including Tax and tip: 100
tax = amount*0.05
             
tip = amount*0.18
             
print(round((amount+tax+tip), 2))
             
123.0
a=int(input("Enter the Value of a: ))
            
SyntaxError: incomplete input
a=int(input("Enter the Value of a: "))
            
Enter the Value of a: 10
b=int(input("Enter the Value of b: ))
            
SyntaxError: incomplete input
b=int(input("Enter the Value of b: "))
            
Enter the Value of b: 5
print(a+b)
            
15
print(a-b)
            
5
print(a*b)
            
50
print(a/b)
            
2.0
print(a%b)
            
0
print(mt.log(a))
            
2.302585092994046
print(ab)
            
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#117>", line 1, in <module>
NameError: name 'ab' is not defined. Did you mean: 'a'?
distance = int(input("Enter the Value of Height(m): "))
            
Enter the Value of Height(m): 10
print("The Final Velocity is: ", mt.sqrt(2*9.8*distance))
            
The Final Velocity is:  14.0
celsi = float(input("Enter the Temp in Celsius: "))
            
Enter the Temp in Celsius: 60
faren = celsi*(9/5) + 32
            
kel = (faren-32)(5/9) + 273.15
            
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#122>", line 1, in <module>
TypeError: 'float' object is not callable
kel = (faren-32)*(5/9) + 273.15
            
print("The Temp in Farenheit is: ",faren)
            
The Temp in Farenheit is:  140.0
print("The Temp in Kelvin is: ",kel)
            
The Temp in Kelvin is:  333.15
num_str = input("Enter the Value of a Number: ")
            
Enter the Value of a Number: 1234
>>> num = [int(x) for x in num_str]
...             
>>> print("Sum of Digits are: ",sum(num))
...             
Sum of Digits are:  10
>>> a = int(input("Enter the Value of a: "))
...             
Enter the Value of a: 40
>>> b = int(input("Enter the Value of b: "))
...             
Enter the Value of b: 100
>>> c = int(input("Enter the Value of c: "))
...             
Enter the Value of c: 30
>>> max_v = max(a,b,c)
...             
>>> min_v = min(a,b,c)
...             
>>> mid_v = (a+b+c) - (max_v+min_v)
...             
>>> print("Ascending Order: ",min_v, mid_v, max_v)
...             
Ascending Order:  30 40 100
>>> time_str = input("Enter the Value of Days, Hours, Minutes & Seconds: ")
...             
Enter the Value of Days, Hours, Minutes & Seconds: 1 1 1 1
>>> d, h, m, s= [int(x) for x in time_str]
...             
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#137>", line 1, in <module>
  File "<pyshell#137>", line 1, in <listcomp>
ValueError: invalid literal for int() with base 10: ' '
