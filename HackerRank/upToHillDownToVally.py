n = int(input())
arr = input()

level = valley = 0
for i in arr:
    level += 1 if i == 'U' else -1
    valley += level == 0 and i == 'U'

print(valley)
