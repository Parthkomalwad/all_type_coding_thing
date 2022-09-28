n = int(input())
arr = list(map(int, input().split()))

count = {}
for i in range(n):
    if arr[i] not in count:
        count[arr[i]] = 1
    else:
        count[arr[i]] += 1
c = 0
for i in count.values():
    c += int(i/2)

print(c)
