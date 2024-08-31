from library import Library

library = Library()

while True:
    print("\nWelcome to the Library!")
    print("1. View available games")
    print("2. Lend a game")
    print("3. Return a game")
    print("4. Donate a game")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        library.games()
    elif choice == '2':
        library.lend()
    elif choice == '3':
        library.returnb()
    elif choice == '4':
        library.donate()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
