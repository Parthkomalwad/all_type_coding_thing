a1 = input('Enter the FirstArray')
b1 = input('Enter the SecondArray')
a = a1.split()
b = b1.split()
n = len(a)
m = len(b)
mp = {}
for i in range(n):
    mp[a[i]] = i
for i in range(m):
    mp[b[i]] = i
print(len(mp))
