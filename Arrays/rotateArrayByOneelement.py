
arr = list(map(int, input().split()))
m = arr[-1]
arr.pop()
arr.insert(0, m)

print(arr)
