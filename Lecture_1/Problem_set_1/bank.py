# A program that prompt the user for greeting then outputs an amount for each of the greetings

def main():
    user_input = input("Greetings: ")
    output = bank_greetings(user_input)
    print(f"${output}")

def bank_greetings (greeting):
    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

main()