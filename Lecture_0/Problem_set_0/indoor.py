# A program that displays user input in lower case letter

# The main function
def main():
    n= input()
    print(user_input(n))

# lowercase conversion function
def user_input(user):
    return user.strip().lower()

main()