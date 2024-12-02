# simple calculator program 
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
opt = input("Enter operation to perform : ")

if opt == 'add':
    result = num1 + num2
elif opt == 'sub':
    result = num1 - num2
elif opt == 'mul':
    result = num1 * num2
elif opt == 'div':
    if num2 != 0:
        result = num1/num2
    else:
        print("Error , Division by zero.")
else:
    result = 'invalid operation.'
print("Result : ",result)
        
