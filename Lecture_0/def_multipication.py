# A program that finds the square of the user input

def main():
    x = int(input("Enter a number you want to square: "))
    print("The square of {} = {} ".format(x, square(x)))

def square(n):
    return pow(n, 2)
    

main()