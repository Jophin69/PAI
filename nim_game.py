def nim_sum(piles):
    result = 0
    for pile in piles:
        result ^= pile
    return result

def is_winning_position(piles):
    return nim_sum(piles) != 0

def nim_game():
    piles = [3, 4, 5]  # Example piles, you can change this
    player = 1
    
    while True:
        print("Current piles:", piles)
        print("Player", player, "'s turn")
        selected_pile = int(input("Select a pile (0-indexed): "))
        selected_stones = int(input("Select number of stones to remove: "))
        
        if selected_pile < 0 or selected_pile >= len(piles) or selected_stones < 1 or selected_stones > piles[selected_pile]:
            print("Invalid move! Try again.")
            continue
        
        piles[selected_pile] -= selected_stones
        
        if is_winning_position(piles):
            print("Player", player, "wins!")
            break
        
        player = 3 - player

nim_game()
