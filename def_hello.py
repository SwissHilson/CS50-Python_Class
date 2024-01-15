# Asimple function that print Hello to the user's name 

def main():
    name = input("What's your name? ").strip().title()
    hello(name)

def hello(to= "World"):
    print("Hello", to)


main()