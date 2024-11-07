def minimax(depth, node_index, is_maximizing, scores, max_depth):
   
    if depth == max_depth:
        return scores[node_index]

    if is_maximizing:
        best = float('-inf')
       
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, False, scores, max_depth)
            best = max(best, value)
        return best
    else:
        best = float('inf')
       
        for i in range(2):
            value = minimax(depth + 1, node_index * 2 + i, True, scores, max_depth)
            best = min(best, value)
        return best


scores = [2, 4, 6, 8, 1, 2, 10, 12 ]  
max_depth = 3
optimal_value = minimax(0, 0, True , scores, max_depth)
print("The optimal value is:", optimal_value)
