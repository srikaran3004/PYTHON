#cars = ["Tata","BMW","Audi","Kia","Ford"]

#for i in cars:
#    print(i)
#   if i == "Kia":
#       break
#str = "Hello World"
#for i in str:
#    print(i)

#for i in range(0,10,2):
#    print(i)

#colors=["red","yellow","blue"]
#cars=["Tata","BMW","Ford"]

#for i in cars:
#    for j in colors:
#        print(j,i)

#x=["telangana","madhya pradesh","tamil nadu","uttar pradesh"]
#y=["india","france","italy","spain","usa","germany"]
#for i in y:
#    for j in x:
#        print(i,j)

#accept a number from the user
#calculate and print the sum of all the numbers
#from 1 to input
#using for loop

x = int(input("Enter a number"))
sum = 0
for  i in range(1,x+1):
    sum = sum+i
    print(sum)