from emoji import emojize

def main():
    user_input = input("Input: ")
    emojized_string = emojize(user_input)
    print("Output: ", emojized_string)

if __name__=="__main__":
    main()