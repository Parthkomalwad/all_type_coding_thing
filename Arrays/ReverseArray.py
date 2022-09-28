n = input('Enter the string')
str1 = n.split()
print(str1)
for i in range(len(str1)-1, -1, -1):
    print(str1[i], end=' ')
