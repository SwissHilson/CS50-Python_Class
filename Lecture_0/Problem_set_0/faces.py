def main():
    user_input = input().strip()
    print(convert(user_input))


def convert(input_str):
    emoji = input_str.replace(':)' , '🙂').replace( ':(' , '🙁')
    return emoji

main()