def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Take user input outside of the function
number = int(input("Enter a non-negative integer: "))
result = factorial(number)

# Print the result outside of the function
print(f"The factorial of {number} is: {result}")
