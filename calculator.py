import math

print("Simple Calculator")

try:

    x = float(input("Enter Any Number:"))
    y = (input("Enter opr. '+,-,/,*':"))
    z = float(input("Enter Any Number:"))

    if y == "+" :
        print(x + z)

    elif y == "-" :
        print(x - z)

    elif y == "/" :
        print(x / z)

    elif y == "*" :
        print(x * z)
        if z != 0:
            print(f"Result: {x / z}")
        else:
            print("⚠️ Cannot divide by zero")
    else:
        print("⚠️ Invalid operation")
    
        
except ValueError:
    print ("Enter Valid Number")