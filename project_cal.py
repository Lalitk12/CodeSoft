# simple calculator
num1=eval(input("Enter the 1st number : - "))
num2=eval(input("Enter the 2nd number : - "))
print(" 1 = + ")
print(" 2 = - ")
print(" 3 = * ")
print(" 4 = // ")
print(" 5 = % ")

ope=int(input("Select the any opration " ))

if ope == 1:
     add=num1+num2
     print("Addition is : - ",add)
elif ope == 2:
     sub=num1-num2
     print("Subtraction is : - ",sub)
elif ope == 3:
     mul=num1*num2
     print("Multiplication is : - ",mul)
elif ope == 4:
     div=num1//num2
     print("Divition is : - ",div)
elif ope == 5:
     mod=num1%num2
     print("Modulration is : - ",mod)
else:
     print("Invalid option is ")
