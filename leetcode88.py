class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m] = nums2[i]
            m += 1
        nums1.sort()


"""
将nums2合并到nums1中
然后直接使用内置排序方法sort
"""