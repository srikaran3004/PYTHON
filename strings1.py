#take user input(string)
#if the len of string is greater than 3
#add 'ing' as a suffix in the orginal string
#else print the same string given by the user

x = str(input(""))
y=len(x)
if y>3:
    print(x+"ing")
else:
    print(x)