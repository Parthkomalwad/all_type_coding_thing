arr = [0, 1, 2, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 1, 1, 1, 2]
ones = []
zeros = []
twos = []
for i in range(len(arr)):
    if(arr[i] == 0):
        zeros.append(arr[i])
    elif(arr[i] == 1):
        ones.append(arr[i])
    elif(arr[i] == 2):
        twos.append(arr[i])
    else:
        print('Not Valid Number')
        continue

arr = zeros + ones + twos
print(arr)

# --------------------------OR--------------------------

arr1 = []
indexOfOne = 0
for i in range(len(arr)):
    if(arr[i] == 2):
        arr1.append(arr[i])
    elif(arr[i] == 1):
        arr1.insert(indexOfOne, arr[i])
        indexOfOne += 1
    elif(arr[i] == 0):
        arr1.insert(0, arr[i])
        indexOfOne += 1
    else:
        print('Not Valid Number')
        continue
print(arr1)
