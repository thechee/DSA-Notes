"""
Given an integer array nums and an integer k, 
return the k most frequent elements. 
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: 

Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
"""

def topKFrequent(nums, k):
    # start with a hash to get value: freq
    counts = {}

    for num in nums:
      counts[num] = 1 + counts.get(num, 0)

    # to sort these nums better than n log n, we must use a bucket sort
    bucket = [[] for _ in range(len(nums) + 1)]
    
    for key, value in counts.items():
      bucket[value].append(key)

    result = []
    # result list to hold values
    # iterate from end of bucket
    for i in range(len(bucket) - 1, 0, -1):
      for n in bucket[i]:
        result.append(n)
        if len(result) == k:
          return result

    

print(topKFrequent([1,1,1,2,2,3], 2)) # [1, 2]
print(topKFrequent([1], 1)) # [1]