arr = [1231, 332, 445, 543, 43, 2, 5, 43, 3]
m_ax = max(arr)
m_in = min(arr)
print(m_ax, m_in)

# ---------------OR----------------

arr = [1231, 332, 445, 543, 43, 2, 5, 43, 3]
arr.sort()
m_ax = arr[len(arr)-1]
m_in = arr[0]
print(m_ax, m_in)
