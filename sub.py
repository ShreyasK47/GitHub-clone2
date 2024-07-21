def subtract(a, b,c):
    return a - b-c

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3=float(input("Enter the third number: "))

result = subtract(num1, num2,num3)
print(f"The result of subtracting {num2} from {num1} and {num3} is {result}")
