# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring 
# houses are of the same color.
# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves 
# this goal.

def painting_houses(costs):
    """
    Calculate the minimum cost to paint N houses with K colors such that no two adjacent houses have the same color.

    :param costs: A 2D list where costs[i][j] represents the cost of painting house i with color j.
    :return: The minimum cost to paint all houses.
    """
    if not costs:
        return 0

    n = len(costs)
    k = len(costs[0])

    result = [[0] * k for _ in range(n)]
    # Initialize the first house's costs
    for j in range(k):
        result[0][j] = costs[0][j]
    # Fill the result array
    for i in range(1, n):
        for j in range(k):
            # Find the minimum cost of painting the previous house with a different color
            min_cost = float('inf')
            for m in range(k):
                if m != j:
                    min_cost = min(min_cost, result[i - 1][m])
            result[i][j] = costs[i][j] + min_cost
    # Find the minimum cost of painting all houses
    min_cost = float('inf')
    for j in range(k):
        min_cost = min(min_cost, result[n - 1][j])
    return min_cost