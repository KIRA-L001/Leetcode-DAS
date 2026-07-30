"""
268. Missing Number
Find missing number from 0..n.
Approach: XOR all indices and values, missing = xor of all indices ^ all values ^ n.
Time: O(n)  Space: O(1)
"""
def missingNumber(nums):
    xor = len(nums)
    for i, x in enumerate(nums):
        xor ^= i ^ x
    return xor
if __name__ == "__main__":
    assert missingNumber([3,0,1]) == 2
    assert missingNumber([0,1]) == 2
    print("0268 OK")
