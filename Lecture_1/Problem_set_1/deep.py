

def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    output = greatest_question(question)
    print(output)

def greatest_question (user_input):
    if (user_input.lower() == '42') or (user_input.lower() == 'forty-two') or (user_input.lower() == 'forty two'):
        return "Yes"
    else:
        return "No"

main()