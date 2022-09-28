n = int(input('Enter the number of baloonds the vendor have'))
ballons = []
ballon_dict = {}
for i in range(n):
    ballons.append(input())
for i in ballons:
    if(i in ballon_dict):
        ballon_dict[i] += 1
    else:
        ballon_dict[i] = 1
for item in ballon_dict:
    if(ballon_dict[item] % 2 == 1):
        print(item, end=' ')
