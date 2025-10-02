def input_checker():
    validated_values=["rock","paper","scissors"]
    
    while True:
        print(
        """
        ----------------------------------------
        For playing choose one of this objects:
        ----------------------------------------
        .... Rock, Paper, Scissors ....
        
        """
        )
        player_input = input("Enter: ").strip().lower()

        if player_input in validated_values:
            return player_input
        else:
            print("❌ Invalid input! Please enter rock, paper, or scissors.")

check=input_checker()
print(f"You choosed: {check} ")