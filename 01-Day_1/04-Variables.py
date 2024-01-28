a = input ("Enter the A variable : ")
b = input ("Enter the B variable : ")

print()
print ("Before switching, Value of A is " + a)
print ("Before switching, Value of B is " + b)

temp = a
a = b
b = temp
print()

print ("After switching, Value of A is " + a)
print ("After switching, Value of B is " + b)