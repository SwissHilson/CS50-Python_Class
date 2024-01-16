# A program that return whether an integer is even or odd number

# The main function
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

# even / odd function
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    #return True if n % 2 == 0 else False
    #return n % 2 == 0

main()