#tuples store multiple variables in a single variable
#tuples are also ordered
#tuples are immutable (which means they can't be append or remove or add ) , they are unchangable
#We use () to represent tuples
#This allows duplicate values (ex:We can have two apples ,two mangoes)
#myTuple = ('apple','orange','pineapple')
#print(myTuple)
#print(len(myTuple))
#Don't think that for example
#tuple=('apple','mango')
#print(tuple[0])....here in order to get output as apple use index as [] only don't use () in order as we used tuple!!
#myTuple=('car','bike','train')
#myList=list(myTuple)
#myList.append('boat')
#myTuple = tuple(myList)
#print(myTuple)
#The above operation describes that to add any element to tuple first we need to covnert to list and then append the element the again convert it to the tuple.

# tuple1=(1,2,3)
# tuple2=(4,5,6)
# tuple1 +=tuple2
# print(tuple1)

# ctrl + / - to select all elements in python code with hastag

# tuple1=(1,2,3,4,5)
# #reverse the above tuple
# tuple1=(1,2,3,4,5)[::-1]
# print(tuple1)

# tup=("Srikaran")[::-1]
# print(tup)

#use of astric sign

#Write  a program to unpack the following tuple into four variables and print each variable 
#tuple1=(10,20,30,40)

# tuple1=(10,20,30,40)
# (a,b,c,d)=tuple1
# print(a)
# print(b)
# print(c)
# print(d)

# tuple1 = (10,20)
# tuple2 = (30,40)
#swap above tuples
#output - tuple1 = (30,40)
#tuple2 = (10,20)

# temp=tuple1
# tuple1=tuple2
# tuple2=temp
# print("tuple1 =",tuple1)
# print("tuple2 =",tuple2)

#or
#directly=(tuple1,tuple2 = tuple2,tuple1)

# tuple1 = (1,[6,7],2,3,4,5)
# a = tuple1[1][0]=(8)
# print(tuple1)


