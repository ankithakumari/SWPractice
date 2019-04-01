""" Remove duplicates from an array in place 
Return the length of new array
"""
nums = [1, 2, 2]

def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        j = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        
        nums[j] = nums[-1]
        return j + 1

print(removeDuplicates(nums))