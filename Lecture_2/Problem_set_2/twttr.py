def main():
    user_input = input("Input: ")
    output = omit_vowels(user_input)
    print(f"Output: ", output)

def omit_vowels(text):
    vowels = "aeiouAEIOU"
    text_without_vowels = ''
    for char in text:
        if char not in vowels:
            text_without_vowels += char
    return text_without_vowels


    
if __name__ == "__main__":
    main()