from re import S


s = input()
n = len(s)

print(s.count('a') * (n//len(s)) + s[:n % len(s)].count('a'))
