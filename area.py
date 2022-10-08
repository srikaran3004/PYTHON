#Area of triangle using herons formula

a = float(input("enter first number: "))
b = float(input("enter second number:"))
c = float(input("enter third number:"))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print(area)



