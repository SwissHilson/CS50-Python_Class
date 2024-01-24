# Calling Function
def main():
    print(" Amount Due: 50")

    total_inserted = 0
    while total_inserted < 50:
        user_input = int(input(" Insert Coin: "))
        total_inserted= coke_machine(user_input, total_inserted)
    calculate_change(total_inserted)

# A function that iterates through a list under a conditon
def coke_machine(coin, total_inserted):
    accepted_coins = [5, 10, 25]
    
    if coin in accepted_coins:
        total_inserted += coin
        print(f"Amount Due: {50 - total_inserted}")
    else:
        print(f"Invalid value {coin}. Please insert 5, 10, 25 cents.")

    return total_inserted

# Calculating for change
def calculate_change(total_inserted):
    change = total_inserted - 50
    if change >= 0:
        print(f"Change owned: {change} cents.")

if __name__ == "__main__":
    main()