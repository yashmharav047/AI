def minimax(depth, isMax):
    # Possible scores (for simplicity)
    scores = [10, 0, -10]

    # Base condition
    if depth == 0:
        return scores[depth]

    # If it's the MAX player's turn
    if isMax:
        best = -100
        print(f"Depth {depth}: MAX's turn")
        for i in range(2):  # Two possible moves
            value = minimax(depth - 1, False)
            best = max(best, value)
            print(f"MAX considers move {i}, value = {value}, best = {best}")
        return best

    # If it's the MIN player's turn
    else:
        best = 100
        print(f"Depth {depth}: MIN's turn")
        for i in range(2):  # Two possible moves
            value = minimax(depth - 1, True)
            best = min(best, value)
            print(f"MIN considers move {i}, value = {value}, best = {best}")
        return best


# Main Function
print("---- Minimax Algorithm Demonstration ----")
score = minimax(2, True)
print("-----------------------------------------")
print("Best value for MAX player:", score)
