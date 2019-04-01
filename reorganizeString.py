# Reorganize a  string such that same character are not next to one another
# Leetcode - level medium
"""
This approach uses the inbuilt priority queue/heap of python
At every level, the 2 most common characters left in the string(heap) are picked and appended to the final string
Example: s = "abbac"
pq = [[2, 'a'], [2, 'b'], [1, 'c']]
Iteration 1: ans = ab       pq = [[1, 'a'], [1, 'b'], [1, 'c']]
Iteration 2: ans = abab     pq = [[1, 'c']]
Iteration 3: ans = ababc

Heapify - creates a min heap , therefore negative counts are store so that the max occurrences will be at root
Complexity : O(NlogA) A - size of the alphabet, N is the length of string

"""
import heapq

s = "aabbnnkjhgeerrhstuffbbbkkl"

# List of lists containing negative count and character
pq = [[-s.count(x), x] for x in set(s)]

# creates a min heap, but since we have negative counts the most common character is at root
heapq.heapify(pq)

# check if any count is > n+1/2 , n is length of string
max_rep = (len(s) + 1)/2
if any(-count > max_rep for count, x in pq):
    print("")
    exit(0)

ans = []


while len(pq) >= 2:
    ct1, char = heapq.heappop(pq)       # get the first 2 characters with max count, heappop maintains the heap property
    ct2, char2 = heapq.heappop(pq)
    ans.extend([char, char2])           # adds the 2 characters to the ans

    if ct1 + 1: heapq.heappush(pq, [ct1 + 1, char])
    if ct2 + 1: heapq.heappush(pq, [ct2 + 1, char2])    # if there are more occurences add back to heap

print("".join(ans) + (pq[0][1] if pq else ''))  # if there is any element left in pq - append it
