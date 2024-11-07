def solve_knapsack():
    val = list(map(int, input("enter the values: ").split()))
    wt = list(map(int, input("enter the weights: ").split()))
    W = int(input("enter the capacity: "))
    n = len(val)

    # Initialize a memoization table with -1 (indicating uncomputed results)
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)]

    def knapsack(W, n):
        # Base case: if no items or no capacity, return 0
        if n < 0 or W <= 0:
            return 0

        # Check if the value is already computed
        if dp[n][W] != -1:
            return dp[n][W]

        # If the current item's weight is more than the capacity, skip it
        if wt[n] > W:
            dp[n][W] = knapsack(W, n - 1)
        else:
            # Calculate the maximum value with and without including the item
            include = val[n] + knapsack(W - wt[n], n - 1)
            exclude = knapsack(W, n - 1)
            dp[n][W] = max(include, exclude)

        return dp[n][W]

    # Calling the knapsack function and printing the result
    print("Max value is:", knapsack(W, n - 1))

if __name__ == "__main__":
    solve_knapsack()
