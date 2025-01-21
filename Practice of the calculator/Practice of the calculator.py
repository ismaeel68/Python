#(Even Number Calculator)
def is_even(num):
    return num%2==0
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0: 
        return "Error! Division by zero."
        return x/y
def calculator():
    print("Welcome to the even number calculator!")

    num1=int(input("Enter the first even number:"))
    if not is_even(num1):
       print(f"{num1}is not an even number. Exiting the  program.")
       return #Exiting the function,effectively ending the program.
    num2=int(input("Enter the second even number:"))
    if not is_even(num2):
       print(f"{num2}is not an even number. Exiting the  program.")
       return #Exiting the function,effectively ending the program.
    print("/nselect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. divide")

    choice=input("Enter choice(1/2/3/4)")
    if choice =='1':
        result=add(num1,num2)
        print(f"{num1}+{num2}={result}")
    elif choice =='2':
          result=subtract(num1,num2)
          print(f"{num1}-{num2}={result}")
    elif choice =='3':
          result=multiply(num1,num2)
          print(f"{num1}*{num2}={result}")
    elif choice=='4':
          result=divide(num1,num2)
          print(f"{num1}/{num2}={result}")
    else:
         print("Error!please try again")
calculator()

#(ODD Number Calculator)
def is_odd(num):
    return num%2!=0
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0: 
        return "Error! Division by zero."
        return x/y
def calculator():
    print("Welcome to the odd number calculator")
    num1=int(input("Enter the first odd number:"))
    if not is_odd(num1):
       print(f"{num1}is not an odd number. Exiting the  program.")
       return #Exiting the function,effectively ending the program.
    num2=int(input("Enter the second odd number:"))
    if not is_odd(num2):
       print(f"{num2}is not an odd number. Exiting the  program.")
       return #Exiting the function,effectively ending the program.
    print("/nselect operations:")
    print("1. Add") 
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice=input("Enter choice (1/2/3/4)")
    if choice =='1':
        result=add(num1,num2)
        print(f"{num1}+{num2}={result}")
    elif choice =='2':
        result=subtract(num1,num2)
        print(f"{num1}+{num2}={result}")
    elif choice =='3':
        result=multiply(num1,num2)
        print(f"{num1}+{num2}={result}")
    elif choice=='4':
        result=multiply(num1,num2)
        print(f"{num1},{num2}={result}")
    else:
        print("Error!please try again")
calculator()

#calcutaor 
def Add(x,y):
    return x+y
def Subtract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Divide(x, y):
    if y != 0:
        return x / y
    return "Error! Division by zero."
num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
print("/n selct operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice=input("Enter choice(1/2/3/4):")
if choice=='1':
    print(f"{num1}+{num2}={Add(num1,num2)}")
elif choice=='2':
    print(f"{num1}-{num2}={Subtract(num1,num2)}")
elif choice=='3':
    print(f"{num1}*{num2}={Multiply(num1,num2)}")
elif choice=='4':
    print(f"{num1}/{num2}={Divide(num1,num2)}")
else:
    print("Invalid input!Please try again")
   