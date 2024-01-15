# A program that returns string input to emojis

# The main function
def main():
    user_input = input().strip()
    print(convert(user_input))

# The  emoji conversion function
def convert(input_str):
    emoji = input_str.replace(':)' , '🙂').replace( ':(' , '🙁')
    return emoji

main()