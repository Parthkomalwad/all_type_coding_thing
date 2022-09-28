l1 = 0


class Solution:
    def kthSmallest(self, arr, l, r, k):
        for i in range(l, r):
            for j in range(l, r):
                if(arr[j] > arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return(arr[k-1])


n = int(input())
arr = list(map(int, input().strip().split()))
k = int(input())
ob = Solution()
print(ob.kthSmallest(arr, 0, n-1, k))
