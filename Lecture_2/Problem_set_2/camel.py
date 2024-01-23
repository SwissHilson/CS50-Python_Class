# Calling function
def main():
    user_input = input("Camel case: ")
    output = camel_to_snake(user_input)
    print("Snake case: ", output)

# 
def camel_to_snake(camel_case):
    snake_case = "" # empty string
    for char in camel_case: # Iterate through the string
        if char.isupper(): # Checking if any char is upper case
            snake_case += '_' + char.lower() # If so concatenate the sting '_' , convert the upper case and apppend them all in the empty string.
        else:
            snake_case += char # if not just append them in the empty string
    return snake_case.lstrip('_')

main()