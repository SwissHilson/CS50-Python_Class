# A simple program that identifies State with name

name = input("What's your name? ")

match name:
    case "John" |"Henry" | "Benard":
        print("Anambra State")
    case "Oluwayo" |"Tunde" | "Ola":
        print("Lagos State")
    case "Aisha" |"Musa" | "Hassan":
        print("Kano State")
    case _:
        print("Who?")