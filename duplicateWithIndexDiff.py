""" Given an array of integers and an integer k, 
find out whether there are two distinct indices i and j in the array 
such that nums[i] = nums[j] and the absolute difference 
between i and j is at most k.  """

nums = [3,1, 2, 2, 4, 5, 1]
k = 4

def containsNearbyDuplicate(nums, k):
	for i, num in enumerate(nums):
		if (i + k) < len(nums) and nums[i + k] == num:
			return True
	return False

print(containsNearbyDuplicate(nums, k))


def otherSolution(nums, k):
	h = {}
	for i, num in enumerate(nums):
		if num in h and i - h[num] <= k:
			return True
		h[num] = i
	return False
print(otherSolution(nums,k))