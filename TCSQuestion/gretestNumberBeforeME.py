arr1 = input()
arr = arr1.split()
count = 0
for i in range(len(arr)):
    flag = False
    for j in range(i, -1, -1):
        if(arr[i] > arr[j]):
            flag = True
        else:
            flag = False
    if(flag):
        count += 1
print(count)


# ------------------OR----------------------

n = int(input('Enter the length'))
m = 0
c = 0
while n:
    n -= 1
    a = int(input())
    if a > m:
        c += 1
        m = a
print(c)
