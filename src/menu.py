from dataclasses import dataclass

def load_recipes():
    print("Loading recipes...")
    # Code to load recipes goes here
    return

def menu():
    print("Menu for Builderment Helper Program.")
    print("Please select an option:")
    print("1 - View All Recipes")
    print("2 - Edit Recipes")
    print("3 - Build an Item Recipe Tree")
    print("4 - Exit")
    run = input("Enter your choice: ")
    if run == "1":
        print("Here's all recipes.")
        load_recipes()
    elif run == "2":
        print("Editing recipes.")
        print("Please select an option:")
        print("1 - Add Recipe")
    print("2 - Remove Recipe")
    print("3 - Edit Current Recipe")
    edit_choice = input("Enter your choice: ")
    if edit_choice == "1":
        print("Adding a new recipe.")
    elif edit_choice == "2":
        print("Removing an existing recipe.")
    elif edit_choice == "3":
        print("Editing a current recipe.")
    elif run == "3":
        print("Building an item recipe tree.")
        print("Pick an item for which to build a tree:")
        item = input("Enter the item name: ")
        print(f"Building recipe tree for {item}...")
    elif run == "4":
        print("Exiting the program.")
        
    return

@dataclass(frozen=True) # initialises basic data object properties
class Item:
    id: str
    name: str
    base_item: bool

@dataclass(frozen=True)
class Recipe:
    pass

@dataclass(frozen=True)
class Stack:
    item: Item
    qty: int

def main():
    return

if __name__ == "__main__":
    main()