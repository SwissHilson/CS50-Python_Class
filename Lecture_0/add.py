# A program that takes an input from user and find the addition rounded up

# Ask user for input
x = float(input("Enter your first number: "))
y = float(input("Enter your second number: "))

# Add and round up
z = round(x + y)

#Display Output
print(f"{z:,}")