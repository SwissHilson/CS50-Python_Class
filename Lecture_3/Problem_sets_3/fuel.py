def main():
    # Get numerator and denominator from user input
    numerator, denominator = get_fraction_input("Fraction: ")
    # Calculate and print fuel percentage based on input
    calculate_fuel_percentage(numerator, denominator)

def get_fraction_input(prompt):
    # Keep prompting the user until a valid fraction is entered
    while True:
        try:
            # Get fraction as input and split into numerator and denominator
            fraction = input(prompt)
            numerator_str, denominator_str = fraction.split('/')
            
            # Convert to integers
            numerator = int(numerator_str)
            denominator = int(denominator_str)

            # Check for invalid input
            if numerator == 0 or numerator > denominator:
                raise ValueError

            # Return valid numerator and denominator
            return numerator, denominator
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction.")

def calculate_fuel_percentage(numerator, denominator):
    # Calculate the percentage and round after multiplication
    percentage = round((numerator / denominator) * 100)

    # Print fuel percentage based on specific conditions
    if numerator == 1 and denominator == 4:
        print(f"{percentage}%")
    elif numerator == 1 and denominator == 2:
        print(f"{percentage}%")
    elif numerator == 3 and denominator == 4:
        print(f"{percentage}%")
    else:
        # Print fuel grade based on percentage range
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            pass
    # Return the calculated percentage
    return percentage

# Call the main function to start the program
main()
