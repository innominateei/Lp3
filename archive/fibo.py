def recursive(n):
    if n <=1:
        return n
    else:
        return recursive(n-1) + recursive(n-2)

def non_recursive(n):
    first = 0
    second = 1
    print(first)
    print(second)
    while n-2>0:
        third = first + second
        first = second
        second = third
        print(third)
        n-=1
if __name__=="__main__":
    n = int(input("enter the value:"))
    print("\nrecursive:")
    for i in range(n):
        print(recursive(i))
    print("\nnon_recursive:")
    non_recursive(n)
    
