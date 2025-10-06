class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = {0:0,1:0,2:0}
        for ele in nums:
           color_counts[ele] += 1
       
        i = 0
        for color in range(3):
            for x in range(color_counts[color]):  # loop count times
                nums[i] = color
                i += 1
