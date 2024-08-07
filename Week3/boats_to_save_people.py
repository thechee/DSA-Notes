"""
You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, 
provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)


Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)


Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""

def num_rescue_boats(people: list[int], limit: int) -> int:
  boats = 0
  # sort the people list
  people.sort()

  l, r = 0, len(people) - 1
  while l <= r: # 4, 4
  # see if current person plus the next is less or equal to limit,
    if people[l] + people[r] <= limit:  # 2 + 3 <= 3
      l += 1
      r -= 1 # 
    else:
      r -= 1 # l = 4

    boats += 1 # boats = 3
  # if so, move the pointer up two
  # increment boats
  return boats 

print(num_rescue_boats([1,2], 3)) # 1
print(num_rescue_boats([3, 2, 2, 1], 3)) # 3
print(num_rescue_boats([3, 5, 3, 4], 5)) # 4