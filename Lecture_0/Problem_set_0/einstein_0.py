# A program that solve E = mc2

# main function
def main():
    mass = int(input("m: "))
    Energy= mass * speed_doubled(mass)
    print("E: ",Energy)

# Finding C square
def speed_doubled(c):
    c = 300000000
    double_c = pow(c, 2)
    return double_c

main()