
def add_item(item, shopping_list):
    shopping_list.append(item)
    return f"'{item}' has been added to the shopping list."
def remove_item(item, shopping_list):
    if item in shopping_list:
        shopping_list.remove(item)
        return f"'{item}' has been removed from the shopping list."
    else:
        return f"'{item}' is not in the shopping list."
def view_list(shopping_list):
    if shopping_list:
        return "Shopping List:\n" + "\n".join(f"- {item}" for item in shopping_list)
    else:
        return "The shopping list is currently empty."
def clear_list(shopping_list):
    shopping_list.clear()
    return "The shopping list has been cleared."

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            print(add_item(item, shopping_list))
            
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            print(remove_item(item, shopping_list))
            pass
        elif choice == '3':
            print(view_list(shopping_list))
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()