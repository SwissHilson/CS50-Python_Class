'''A program that tells you what to eat and when.'''


def main():
    #User's input and and conversion
    user_input = input('What time is it? ')
    time_conversion = convert(user_input)

    #Determining the time for each meal
    if 7.0 <= time_conversion <= 8.0:
        print("breakfast time")
    if 12.0 <= time_conversion <= 13.0:
        print("lunch time")
    elif 18.0 <= time_conversion <= 19.0:
        print("dinner time")
    
def convert(time):
    #Conversion of time in 24 hours format
    if ':' in time:
        hours, minutes = time.split(':')
        return int(hours) + (int(minutes) / 60.0)
    #Conversion of time in 12 hours format
    else:
        time_split = time.split()
        hours, minutes = time_split[0].split(':')
        if time_split[1].lower() == 'pm':
            hours = int(hours) + 12
        return int(hours) + (int(minutes) / 60.0)

if __name__ == "__main__":
    main()