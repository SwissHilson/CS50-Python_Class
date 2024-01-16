# A program that solve E = mc2

# main function
def main():
    mass_kg = int(input("m: "))
    print("E: ", calculate_energy(mass_kg))

def calculate_energy(mass):
    light_speed = 300000000 # speed of light approximate measurement
    energy = mass * light_speed ** 2 # Albert Einstein's formular E = mc2
    return energy

main()
