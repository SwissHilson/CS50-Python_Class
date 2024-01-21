'''
A program that enables user to perform an arithmetic maths
'''
print("Note: Always add a space in-between your input!!!")

# user input, call interpreter function and print the result
def main():
    user_input = input("Expression: ").strip()
    print(arithmetic_interpreter(user_input))


def arithmetic_interpreter(expression):
    #Split and differtiate the integers from string
    x, y, z = expression.split()
    x, z = float(x), float(z)
    
    #Performing arithmetic operators
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
    #Handling Division
        if z == 0:
            return f"Error: {x} cannot be divided by zero"
        else:
            result = x / z
    #Calculate result and output
    if y == '/':
        return f"{round(result, 1)}"
    else:
        return f"{round(result, 1)}"
    
main()

    