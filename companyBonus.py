

#company will give bonus base on following criteria

#Time spent in company       Bonus
#    greater than 10 years    10%

#morethan 6 and lessthan 10    8%

#less than 6                   5%

#ask the salary and time spent from the user 
#print the net bonus amount accordingly


a = int(input("Salary"))
b = int(input("Years of Experience"))

if b>=10:
    print("Net bonus amount",a+a*10/100)
elif b>=6:
    print("Net bonus amount",a+a*8/100)
else :
    print("Net bonus amount",a+a*5/100)