class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = sorted(nums1[:m] + nums2[:n]) 
        for i in range(len(merged)):
            nums1[i] = merged[i]
        return nums1
#time complexity = O((m + n) log(m + n))
#space complexity = O(m+n)
