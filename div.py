# Function to perform division
def divide_numbers(num1, num2):
    try:
        # Perform division
        result = num1 / num2
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Division by zero is not allowed."
    except TypeError:
        # Handle wrong data types
        return "Error: Please provide numbers for division."
    else:
        # Return the result if no exceptions
        return result

# Example usage
number1 = 10
number2 = 2

result = divide_numbers(number1, number2)
print("Result:", result)
