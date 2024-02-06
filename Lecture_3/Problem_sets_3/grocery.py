'''A program for taking Grocery list and also take a count of the items in the list '''
def main():
    user_input = create_grocery_list()
    sorted_grocery_list(user_input)
    
def create_grocery_list():
    grocery_list = [] # Empty list
    print("Enter your grocery list (press Ctrl+D to finish:)")

    while True:
        try:
            # Take user input and convert it lower case
            item = input().strip().lower()
            if not item:
                continue
            grocery_list.append(item)
            
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
    sorted_items = sorted(item_count.items())
   
    print(f"\nMy Grocery list:")
    # Output the grocery list in the specified format(upper case)
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")
  
if __name__ == "__main__":
    main()