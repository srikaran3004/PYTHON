#Keyword Variable Length data
#def details(name,**data):
#    print(name)
#    print(data)
#    for i,j in data.items():
#        print(i,j)

#details("Srikaran", place="Warangal",age=18)

def sum_recursion(num):
    if num==0:
        return num
    return num+sum_recursion(num)