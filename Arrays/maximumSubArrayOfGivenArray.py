
arr = list(map(int, input().split()))
maxi = arr[0]
sumi = arr[0]
for i in range(1, len(arr)):
    sumi = max(arr[i], arr[i]+sumi)
    maxi = max(maxi, sumi)
print(maxi)
