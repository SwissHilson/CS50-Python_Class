import sys
import random
import pyfiglet

def main():

    user_input = input("Input: ")
    output = text_in_font(user_input, font_name)
    print(f"Output: \n{output}")


    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python figlet.py [-f FONT_NAME] [TEXT]")

    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] not in ['-f', '--font']):
        font_name = random.choice(pyfiglet.FigletFont.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        font_name = sys.argv[2]
    else:
        sys.exit("Invalid argument. Usage: python figlet.py [-f FONT_NAME] [TEXT]")

    if font_name not in pyfiglet.FigletFont.getFonts():
        sys.exit(f"Font '{font_name}' not found.")

def text_in_font(text, font_name):
    figlet = pyfiglet.Figlet(font=font_name)
    return figlet.renderText(text)

if __name__ == "__main__":
    main()
