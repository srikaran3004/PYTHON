# def isEven(i):
    # return i%2==0
# 
# list1=[3,4,10,9,18,66,13,15]
# evenNum = list(filter(lambda i : i%2==0,list1))
# print(evenNum)
# A = list(filter(lambda i : i>5,list1))
# print(A)
# squareNum = list(map(lambda i : i**2,list1))
# print(squareNum)

# python decorators

# list1=[10,20,30,40,50]
# triple = list(map(lambda i : i*3,list1))
# print(triple)

# list2=["a","B","c","D","e","f"]
# x = list(map(lambda i : i.swapcase(),list2))
# print(x)

# def div(a,b):
#     print(a/b)
# print(div(4,2))

# def good_div(func):

#     def inner_div(a,b):
#         if a>b:
#             a,b=b,a
#         return func(a,b)

#     return inner_div
#div = good_div(div)  
#div(2,4)



