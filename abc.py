#write a python program which accepts the radius of a circle from the user and computes area.

pi=3.14
r=float(input("Input the radius of the circle :"))
print("The area of the circle with radius " + str(r) + "is:" + str(pi*r**2))

#write a program to accept a filename from the user and print the extension of that.

filen = input("Input the Filename: ")
fextension = filen.split(".")
print ("The extension of the file is : " + repr(fextension[-1]))
