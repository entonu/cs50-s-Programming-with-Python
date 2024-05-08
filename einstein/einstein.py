def main():
    print(calculate_energy(int(input("m "))))
def calculate_energy(mass):
    C=300000000
    return mass*pow(C, 2)
main()