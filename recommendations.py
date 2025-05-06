def main():
    difficulty = input("Difficult or Casual?")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return
    
    players = input("Multiplayer or Single-player? ")
    if not (difficulty == "Mutiplayer" or difficulty == "Single-playerl"):
        print("Enter a valid number of players")
        return
    
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty =="Difficlt" and players == "Single-player":
        recommend ("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend ("Hearts")

main()