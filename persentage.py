english = int(input("Enter your english marks: "))
maths = int(input("enter your maths marks: "))
computer = int(input("enter your computer marks: "))
science = int(input("enter your science marks: "))
history = int(input("enter your history marks: "))

sum= english + maths + computer + science + history
print("total:",sum)
percentage = (sum / 500) * 100
print("percentage:",percentage)