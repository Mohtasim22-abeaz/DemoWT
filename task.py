import math

def alphabeta(depth, index, is_max, values, alpha, beta):

    if depth == 3:
        print(f"Visited leaf {values[index]}")
        return values[index]

    if is_max:  
        best = -math.inf

        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i,
                            False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if alpha >= beta:
                print("PRUNE at MAX node")
                break

        return best

    else: 
        best = math.inf

        for i in range(2):
            val = alphabeta(depth + 1, index * 2 + i,
                            True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if alpha >= beta:
                print("PRUNE at MIN node")
                break

        return best

values = [6, 5, 8, 7, 2, 1, 3, 4]

result = alphabeta(
    depth=0,
    index=0,
    is_max=True,
    values=values,
    alpha=-math.inf,
    beta=math.inf
)

print("\nOptimal value:", result)