r = int(input())
c = int(input())
sum1 = 0
_row = 0
temp = 0

for i in range(r):
    for j in range(c):
        sum1 += int(input())
    if(sum1 > temp):
        temp = sum1
        _row = i+1
    sum1 = 0

print(_row)
