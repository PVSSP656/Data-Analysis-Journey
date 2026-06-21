mystring = "burger"
myfloat = 5.0
myint = 6
if mystring == "hello" :
    print("String: %s" %mystring)
else:
    print(mystring.capitalize(), "is not hello")
if isinstance(myfloat,float) and myfloat == 7.0:
    print("Float number: %.2f" %myfloat)
else:
    print(myfloat, " is not equal to 7.0" )
if isinstance(myint, int) and myint == 6:
    print("True")

x = None
print(x)
x = "hello"
print(x)
print(repr(x))