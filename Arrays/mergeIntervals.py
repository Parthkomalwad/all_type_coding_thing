intervals = [[1, 4], [0, 4]]
new_li = [0, 0]
li = []
n = len(intervals)
i = 0
while(i < n):
    if(i+1 < n and intervals[i][1] >= intervals[i+1][0]):
        new_li = [min(intervals[i][0], intervals[i+1][0]), intervals[i+1][1]]
        i += 1
        li.append(new_li)
    else:
        li.append(intervals[i])
    i += 1
print(li)
