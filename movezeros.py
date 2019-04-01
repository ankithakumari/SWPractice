"""
Move zeros to end of array
"""
import time


nums = [1, 0, 12, 13, 0, 15, 0, 17, 19, 20, 0, 9, 0, 8, 0, 6, 0, 5, 0]

# Complexity O(N + M) - N numbers with M zeros
def moveZeros(nums):
	start = time.time()
	j = 0

	for num in nums:
		if num != 0:
			nums[j] = num
			j += 1
	for i in range(j, len(nums)):
		nums[i] = 0
	end = time.time()
	print(end - start)
	return nums

print(moveZeros(nums))





	

