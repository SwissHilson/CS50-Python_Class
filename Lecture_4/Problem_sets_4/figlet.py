import sys
import random
import pyfiglet
def main():

    #Check the number of command-line arguments
    if len(sys.argv) not in [1, 3]:
        sys.exit("Usage: python figlet.py [-f FONT_NAME]")

    # Check if the user wants to output text in random font
    elif len(sys.argv) == 1:
        font_name = random.choice(pyfiglet.FigletFont.getFonts())
    else:
        # Check if the user provided correct argument for specifying font
        if  sys.argv[1] not in ['-f', '--font'] or len(sys.argv) != 3:
            sys.exit("Invalid argument. Usage: python figlet.py [-f FONT_NAME]")
        font_name = sys.argv[2]

    if font_name not in pyfiglet.FigletFont.getFonts():
        sys.exit(f"Font '{font_name}' not found.")

    user_input = input("Input: ")
    output = text_in_font(user_input, font_name)
    print(f"Output: \n {output}")

def text_in_font(text, font_name):
    figlet = pyfiglet.Figlet(font=font_name)
    return figlet.renderText(text)

if __name__ == "__main__":
    main()