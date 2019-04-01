# Given two arrays, write a function to compute their intersection.
# Example: Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2] 

nums1 = [1, 2, 2, 2, 1]
nums2 = [1, 2, 2]

def intersect(nums1, nums2):
	if nums1 == nums2:
		return nums1

	result = []
	combined = set(nums1).intersection(set(nums2)) # useful if the intersection is small as compared to the length of individual lists
	if len(combined) != 0:
		for num in combined:
			min_count = min(nums1.count(num), nums2.count(num))
			result += [num] * min_count
	return result

#Solution if arrays are sorted

def intersectSorted(nums1, nums2):
	result = []
	if len(nums1) < len(nums2):
		temp = set(nums1)
	else:
		temp = set(nums2)

	for num in temp:
		min_count = min(nums1.count(num), nums2.count(num))
		if min_count > 0:
			result += [num] * min_count   #This can be quite expensive if there are lots of repeated numbers
	return result	




print(intersect(nums1, nums2))