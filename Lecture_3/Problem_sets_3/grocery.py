'''A program for taking Grocery list and also take a count of the items in the list '''
def main():
    prompt = " "
    user_input = create_grocery_list(prompt)
    output = sorted_grocery_list(user_input)
    print(output)
    

def create_grocery_list(prompt):
    grocery_list = [] # Empty list
    while True:
        try:
            # Take user input and convert it lower case
            item = input(prompt)
            grocery_list.append(item.lower())
        except EOFError:
            # Control - D to exit the program
            break
    return grocery_list

# Count the occurrences of each item in the list
def sorted_grocery_list(grocery_list):
    item_count = {}
    for item in set(grocery_list):
        count = grocery_list.count(item)
        item_count[item] = count

    # Sort the item aphabetically
    sorted_items = sorted(item_count.keys())
    # Output the grocery list in the specified format(upper case)
    for item in sorted_items:
        count = item_count[item]
        return (f"{count} {item.upper()}")

  


if __name__ == "__main__":
    main()