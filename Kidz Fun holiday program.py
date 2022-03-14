fun_in_sun = []
active_kidz = []

loop = True

print("Welcome to the averaging program.")

while loop:
    program = input("\nWhat program is your child attending?"
                    "\n'Fun in the Sun' [A]"
                    "\n'Active Kidz' [B]"
                    "\n quit [X]"
                    "\n>>> ").lower().strip()

    if program == "a" or program == "fun in the sun":
        age = int(input("\nWhat is your child's age?"
                        "\n>>> "))
        fun_in_sun.append(age)
        print("\nChild added to Fun in the Sun program.")
    elif program == "b" or program == "active kidz":
        age = int(input("\nWhat is your child's age?"
                        "\n>>> "))
        active_kidz.append(age)
        print("\nChild added to Active Kidz program.")

    elif program == "x" or program == "quit":
        loop = False

    else:
        print("\nPlease enter a valid program option!")

try:
    total_fun_sun = len(fun_in_sun)
    total_active_kidz = len(active_kidz)
    print(f"\nThe total number of kids in 'Fun in the Sun' is {total_fun_sun}."
          f"\nThe total number of kids in 'Active Kidz' is {total_active_kidz}.")
    fun_sun_aver = sum(fun_in_sun) / len(fun_in_sun)
    active_kidz_aver = sum(active_kidz) / len(active_kidz)

    fun_sun_aver = round(fun_sun_aver)
    active_kidz_aver = round(active_kidz_aver)
    print(f"\nThe average age for 'Fun in the Sun' is {fun_sun_aver}."
          f"\nThe average age for 'Active Kidz' is {active_kidz_aver}.")
    exit()

except ZeroDivisionError:
    print("Please enter at least one value for each program!")
    exit()
