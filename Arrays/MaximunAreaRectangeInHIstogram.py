
# RequireThungs
from turtle import clear


arr = input("Enter the histogram heights")
heights = arr.split()
n = len(heights)
left = [0] * n
right = [0] * n
stack = []

# ITS FOR GETTING LEFT INDEX
'''If left is greater pop the top element if empty stack then index is zero and push the current index in stack
If left is less then top of stack+1 is the the index'''

for i in range(n):
    if not stack:
        left[i] = 0
    else:
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1]+1 if stack else 0
    stack.append(i)
stack.clear()

# ITS FOR GETTING RIGHT INDEX
'''If right is greater pop the top element if empty stack then index is n-1 and push the current index in stack
If right is less then top of stack-1 is the the index'''

for i in range(n-1, -1, -1):
    if not stack:
        right[i] = n-1
    else:
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1]-1 if stack else n-1
    stack.append(i)
stack.clear()

# Calculating the Area
max_area = 0
for i in range(n):
    height = int(heights[i])
    witdth = (right[i] - left[i])+1
    area = height * witdth
    if area > max_area:
        max_area = area
print(max_area)
