def main():
    prompt = "Item: "
    user = place_orders(prompt)
    print(user)


def place_orders(prompt):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    order_total = 0.0

    while True:
        try:
            user_input = input(prompt)

            # Check if the item is in the menu (case-insensitive)
            item = user_input.title()
            if item in menu:
                order_total += menu[item]
                print(f"Total: ${order_total:.2f}")
            else:
                print("Invalid item. Please choose from the menu.")
        except EOFError:
            # Ctrl-D pressed, exit the loop
            break
    return order_total

if __name__ == "__main__":
    main()
