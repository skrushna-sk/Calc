def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print ("select operations:")
print ("1. add")
print ("2. substract")
print ("3. multiply")
print ("4. divide")

choice = input ("enter choice (1/2/3/4):")
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

if choice == '1':
    print (f"{num1}+{num2}= {add(num1, num2)}")
elif choice == '2':
    print (f"{num1}-{num2}= {substract(num1, num2)}")
elif choice == '3':
    print (f"{num1}*{num2}= {multiply(num1, num2)}")
elif choice == '4':  
    if num2!= 0:
        print (f"{num1}/{num2}= {divide(num1, num2)}")
    else:
        print ("error! division by zero is not allowed.")
else:
    print ("invalid output")