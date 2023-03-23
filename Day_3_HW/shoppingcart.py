shopping_list = {}


def add_item(item, quantity):
    shopping_list[item] = quantity
    print(f"{quantity} {item}(s) added to the shopping list.")


def remove_item(item):
    if item in shopping_list:
        del shopping_list[item]
        print(f"{item} removed from the shopping list.")

def print_list():
    print("Current shopping list:")
    for item, quantity in shopping_list.items():
        print(f"{quantity} {item}")


while True:
    
    print("press 'a' to add")
    print("Press 'r' to remove")
    print("Enter 'c' to see cart.")
    print("Enter 'q' to quit")
    
    user_input = input(" ")
    
    
    if user_input == "a":
        item = input("Food item: ")
        quantity = input("Enter item quantity: ")
        add_item(item, quantity)
    elif user_input == "r":
        item = input("Food to remove: ")
        remove_item(item)
    elif user_input == "c":
        print_list()
    elif user_input == "q":
        break
    else:
        print("Invalid input. Please try again.")


print_list()










