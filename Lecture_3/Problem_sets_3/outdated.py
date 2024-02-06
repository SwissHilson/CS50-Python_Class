def main():
    '''
    Main function to execute the program.
    '''
    iso_date = convert_to_iso_date()
    print(iso_date)


def get_user_input():
    '''
    Function to prompt the user for a date input and validate its format.

    Returns:
        list: List containing month, day, and year parts of the date input.

    '''
    while True:
        try:
            user_input = input("Date: ")
            parts = user_input.split('/')

            if len(parts) == 3:
                return parts
            else: 
                parts = user_input.split('/')
                if len(parts) == 3:
                     return parts
                else:
                    raise ValueError("Invalid input format.")
        except ValueError as e:
             print(e)

def parse_date(parts):
    '''
    Function to parse the date input into month, day, and year.

    Args:
        parts (list): List containing month, day, and year parts of the date.

    Returns:
        tuple: Tuple containing month, day and year integers.
    '''
    months = [
        "January", "Febuary", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]

    if '/' in parts:
        month, day, year = map(int, parts)
        return month, day, year
    else:
        month_name, day, year = parts
        month = months.index(month_name) + 1
        day = int(day.strip(','))
        year = int(year)
        return month, day, year
    
def convert_to_iso_date():
    '''
    Function to convert the data input into ISO 8601 format.

    Returns:
        str: Date string in ISo 8601 format (YYYY-MM-DD).
    '''
    while True:
        try:
            parts = get_user_input()
            month, day, year = parse_date(parts)

            if 1 <= 12 and 1 <= day <= 31:
                iso_date = f"{year:04d}-{month:02d}-{day:02d}"
                return iso_date
            else:
                print(" Invalid date. Month and day should be within raesonable range.")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()

