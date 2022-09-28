arr = list(map(int, input().split()))
n = len(arr)

maxi = 0
for i in range(n):
    if(arr[i] < arr[i+1] and i+1 < n-1):
        maxi = arr[i+1]
