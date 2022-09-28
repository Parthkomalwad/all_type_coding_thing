arr = input('Enter the arr')
n = len(arr)
k = int(input('Enter the rotations'))

mod = k % n

for i in range(n):
    print(arr[(mod + i) % n], end=',')
print
