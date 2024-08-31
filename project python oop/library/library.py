class Library:
    def __init__(self):
        self.gameslist = ['Fifa', 'pes', 'pubg', 'chess']
        self.lenders = {}
        self.donors = {}

    def games(self):
        if len(self.gameslist) == 0:
            print("No games are available in the library.")
        else:
            print("\nAvailable games in the library:")
            print(" - ".join(self.gameslist))
            print()

    def lend(self):
        borrower = input("Enter your name: ")
        game = input("Enter the name of the game you want to borrow: ")
        if game in self.gameslist:
            self.gameslist.remove(game)
            self.lenders[borrower] = game
            print(f"{borrower} has borrowed '{game}'.")
        else:
            print(f"'{game}' is not available in the library.")

    def returnb(self):
        borrower = input("Enter your name: ")
        if borrower in self.lenders:
            game = self.lenders.pop(borrower)
            self.gameslist.append(game)
            print(f"{borrower} has returned '{game}'.")
        else:
            print(f"{borrower} has not borrowed any game.")

    def donate(self):
        donor = input("Enter your name: ")
        game = input("Enter the name of the game you want to donate: ")
        self.gameslist.append(game)
        self.donors[donor] = game
        print(f"'{game}' has been donated by {donor}.")