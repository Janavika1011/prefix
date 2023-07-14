def construct_prefix_sum(A):
    n = len(A)
    
    for i in range(1, n):
        A[i] += A[i-1]
    
    return A
arr = list(map(int,input("Enter: ").split()))
prefix_sum = construct_prefix_sum(arr)
print(prefix_sum)
