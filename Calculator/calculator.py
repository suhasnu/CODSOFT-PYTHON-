import math
print("\n1.ADDITION")
print("\n2.SUBTRACTION")
print("\n3.MULTIPLICATION")
print("\n4.DIVISION")
print("\n5.SQUARE ROOT")
print("\n6.SQUARE ")
print("\n7.CUBE")

print("\nSelect an operation to perform:")

operation = input()

if operation == "1":
    num1 = input("\nEnter the First number: ")
    num2 = input("\nEnter the Second number: ")
    print("\nThe Addition of two number is : " + str(int(num1) + int(num2)))
    
elif operation == "2":
     num1 = input("\nEnter the First number: ")
     num2 = input("\nEnter the Second number: ")
     print("\nThe Subtraction of two number is : " + str(int(num1) - int(num2)))
     
elif operation == "3":
     num1 = input("\nEnter the First number: ")
     num2 = input("\nEnter the Second number: ")
     print("\nThe Multiplication of two number is : " + str(int(num1) * int(num2)))
    
elif operation == "4":
     num1 = input("\nEnter the First number:")
     num2 = input("\nEnter the Second number:")
     print("\nThe Division of two number is :" + str(int(num1) / int(num2)))
     
elif operation == "5":
     num = int(input("\nEnter the number:"))
     print("\nThe Square Root of the number is :" + str(math.sqrt(num)))
     
elif operation == "6":
     num = int(input("\nEnter the number:"))
     print("\nThe Square of the number is :" + str(pow(num,2)))
     
elif operation == "7":
     num = int(input("\nEnter the number:"))
     print("\nThe Cube of the number is :" + str(pow(num,3)))
    
else:
    print("\nInvalid operation")
