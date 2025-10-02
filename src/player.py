def input_checker():
    while True:
        validated_values=["rock","paper","scissors"]
        player_input=input(
        """
        ----------------------------------------
        For playing choose one of this objects:
        ----------------------------------------
        .... Rock, Paper, Scissors ....

        """
        )
        if player_input in validated_values:
            return player_input
        else:
            print("❌ Invalid input! Please enter rock, paper, or scissors.")