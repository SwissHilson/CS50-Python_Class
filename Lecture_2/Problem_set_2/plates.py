''''A program that prompt user for vanity plate then output *Valid* 
    if meets all of the requirements or *Invalid* if it does not.'''
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(s):
        # Check lenght
        if 2 <= len(s) <= 6:
            # Check if two number are letters
            if s[:2].isalpha():
                # Check if all characters are alphanumeric
                if all(char.isalnum() for char in s):
                    # Check if th elast character is a digit and not '0'
                    if s[-1].isdigit() and s[-1] != '0':
                        return True
        return False


if __name__ == "__main__":
    main()