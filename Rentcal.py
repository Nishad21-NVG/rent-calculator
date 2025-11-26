##Inputs we need from user
#Total Rent
#Total food ordered for Snacks,Lunch,Dinner,etc..
#Electricity units speed
#Charge per unit
#Persons living in room/flat.
## Output
# Total amount you've to pay is
def get_int(prompt):
    """Ask for an integer until the user enters a valid number."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def calculate_share(rent, food, electricity_units, charge_per_unit, persons):
    """Return the amount each person has to pay."""
    total_electricity_bill = electricity_units * charge_per_unit
    total_bill = rent + food + total_electricity_bill
    return total_bill / persons


def main():
    print("===== Rent Calculator =====")

    rent = get_int("Enter your hostel/flat rent: ")
    food = get_int("Enter the total amount spent on food/snacks: ")
    electricity_units = get_int("Enter the total electricity units used: ")
    charge_per_unit = get_int("Enter the charge per electricity unit: ")

    # Make sure persons is at least 1
    while True:
        persons = get_int("Enter the number of persons living in the room/flat: ")
        if persons == 0:
            print("Number of persons cannot be 0. Please enter at least 1.")
        else:
            break

    each_share = calculate_share(rent, food, electricity_units, charge_per_unit, persons)

    print("\n===== Result =====")
    print(f"Total rent: ₹{rent}")
    print(f"Total food: ₹{food}")
    print(f"Electricity bill: ₹{electricity_units * charge_per_unit}")
    print(f"Number of persons: {persons}")
    print(f"\nEach person will pay: ₹{each_share:.2f}")


if __name__ == "__main__":
    main()
