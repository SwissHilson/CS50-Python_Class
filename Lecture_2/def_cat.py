def main():
     # Get the number of iterations from the user
    number = get_number()
    # Call the meow function with the provided number of iterations
    meow(number)

def get_number():
    # Keep prompting the user for input until a positive integer is entered
    while True:
        n  = int(input("How many times doyou want to iterate? "))
        if n > 0:
            break
    return n


def meow(x):
     # Print "meow" the specified number of times
    for _ in range(x):
        print("meow")
    
main()