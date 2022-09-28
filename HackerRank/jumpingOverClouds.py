c = list(map(int, input().split()))
jumps = 0
i = 0
while (i < len(c)-1):
    if(i < len(c)-2 and c[i+2] == 0):
        i += 2
    else:
        i += 1
    jumps += 1
print(jumps)
