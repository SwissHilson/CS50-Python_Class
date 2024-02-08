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
                parts = user_input.split(' ')
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
        tuple: Tuple containing month, day, and year integers.
    '''
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    if '/' in parts[0]:
        month, day, year = map(int, parts)
        return month, day, year
    else:
        month_name, day, year = parts
        month = months.index(month_name) + 1
        day = int(day.strip(','))
        year = int(year)
        return month, day, year


def is_leap_year(year):
    '''
    Function to check if a year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if it's a leap year, False otherwise.
    '''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def convert_to_iso_date():
    '''
    Function to convert the data input into ISO 8601 format.

    Returns:
        str: Date string in ISO 8601 format (YYYY-MM-DD).
    '''
    while True:
        try:
            parts = get_user_input()
            month, day, year = parse_date(parts)

            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Invalid date. Month and day should be within reasonable range.")

            if month == 2 and day > 29:
                raise ValueError("Invalid date. February cannot have more than 29 days.")

            if month in [4, 6, 9, 11] and day > 30:
                raise ValueError("Invalid date. This month cannot have more than 30 days.")

            if month == 2 and day == 29 and not is_leap_year(year):
                raise ValueError("Invalid date. February 29 is only valid in a leap year.")

            iso_date = f"{year:04d}-{month:02d}-{day:02d}"
            return iso_date
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
