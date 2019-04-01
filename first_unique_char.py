#Given a string, find the first non-repeating character in it 
# and return it's index.
# If it doesn't exist, return -1.


s = "ABDEFGABEF"

def firstUniqueChar(s):
	chars = set(s)
	indices = [s.index(char) for char in chars if s.count(char) == 1]
	if len(indices) > 0:
		return min(indices)
	else:
		return -1
print(firstUniqueChar(s))
		

