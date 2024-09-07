def divide(ourDividend, ourDivisor):
   
    if ourDivisor == 0:
        raise ValueError("Cannot divide by zero")

    
    sign = -1 if (ourDividend < 0) ^ (ourDivisor < 0) else 1

    
    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)

    quotientNumber = 0
    tempNumber = 0

    
    for i in range(31, -1, -1):
        
        if tempNumber + (ourDivisor << i) <= ourDividend:
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i

    
    quotientNumber *= sign

    return quotientNumber

# Input from the user
a = int(input("Enter a for a/b: "))
b = int(input("Enter b for a/b: "))

try:
    result = divide(a, b)
    print("Result of", a, "/", b, "is", result)
except ValueError as e:
    print(e)
