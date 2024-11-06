def solve_knapsack():
    val = list(map(int,input("enter the values:").split()))
    wt = list(map(int,input("enter the weights:").split()))
    W = int(input("enter the capacity:"))
    n = len(val) -1
    
    def knapsack(W,n):
        if n<0 or W<=0:
            return 0
        if wt[n]>W:
            return knapsack(W,n-1)
        else:
            include = val[n] + knapsack(W - wt[n], n-1)
            exclude = knapsack(W,n-1)
            return max(include,exclude)
    print("max value is:",knapsack(W,n))

if __name__ =="__main__":
    solve_knapsack()
