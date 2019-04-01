"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
 valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
 So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
 So the output should be 5.
"""

def countSum(S, coins , sum):

    #required sum is 0 - 1 solution to not include any coin
    if sum == 0:
        return 1
    elif sum < 0: #negative value , no solution
        return 0
    elif coins <= 0 and sum > 0:
        return 0
    else:
        return countSum(S, coins - 1, sum ) + countSum(S, coins, sum-S[coins-1])

S = [1, 2, 3, 4]
print(countSum(S, 3, 5))