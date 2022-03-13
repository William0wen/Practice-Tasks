import time

dog_list = []
loop = True


def drop_off():
    name = input("\nWhat is the dog's name: ")
    dog_list.append(name)
    print(f"\n{name} has been added to the list.")
    time.sleep(1)


def pick_up():
    name = input("\nWhat is the dog's name: ")
    if name in dog_list:
        dog_list.remove(name)
        print(f"\n{name} has been checked out, and is awaiting pickup.")
    else:
        print("\nThere are no dogs with that name currently staying.")
    time.sleep(1)


def print_list():
    print("\nHere is a list of the dogs staying:")
    print(dog_list)
    time.sleep(1)


def calculate_price():
    days = int(input("How many days are the dogs staying for: "))
    price = len(dog_list) * 22.50 * days
    print(f"The total price for {len(dog_list)} dogs is ${price}")
    time.sleep(1)


# Intro Loop
def intro():
    global loop
    choice = input("\nWould you like to:"
                   "\n\t[A] Drop off a dog"
                   "\n\t[B] Pick one up"
                   "\n\t[C] Print a list of the dogs staying"
                   "\n\t[D] Calculate the amount to pay for the stay"
                   "\n\t[E] Exit the program"
                   "\n>>>  ").lower().strip()

    if choice == "a":
        drop_off()
    elif choice == "b":
        pick_up()
    elif choice == "c":
        print_list()
    elif choice == "d":
        calculate_price()
    elif choice == "e":
        loop = False
    else:
        print("\nPlease enter a valid answer.")
        time.sleep(1)


# Main
print("Welcome to the DogsRus dog sitting service!")
while loop:
    intro()
    print()

exit("\nHave a nice day.")
