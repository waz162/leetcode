class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        # handle cases where k > length of n
        k %= len(nums)

        # reverse whole list
        rev(0, len(nums) - 1)

        # reverse k elements
        l, r = 0, k - 1
        rev(0, k - 1)

        # reverse remaining elements
        rev(k, len(nums) - 1)