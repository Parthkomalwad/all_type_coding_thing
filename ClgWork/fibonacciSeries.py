n = int(input('Enter the series length'))
n1, n2 = 0, 1
count = 0
if(n == 1):
    print(n)
elif(n < 0):
    print('Enter a positive Number')
else:
    while count < n:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# ----------------------OR------------------------


def recursive_fibo(n):
    if n <= 1:
        return n
    else:
        return(recursive_fibo(n-1)+recursive_fibo(n-2))


print()
for i in range(n):
    print(recursive_fibo(i), end=' ')
