arr = [-2, 2, 3, -13, -44, 22, 3, 8, 9, -22]
arr1 = []
for i in range(len(arr)):
    if(arr[i] < 0):
        arr1.insert(0, arr[i])
    else:
        arr1.append(arr[i])
print(arr1)

# --------------------OR-------------------

arr.sort()
print(arr)
