# A program that displays user input with three periods as whitespaces

# The main function
def main():
    n= input()
    print(user_input(n))

# function for adding three period
def user_input(user):
    result = "...".join(user.split())
    return result
        

main()