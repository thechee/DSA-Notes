"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter
you can get after performing the above operations.


Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.


Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

"""
Method:
Use a sliding window to keep track of length
Use a char counts hash to keep track of chars in the window
Track max len on every iteration

Iterate over the str with the r pointer
Update the counts hash with r pointer value
Check to see if the current length of window minus the max value of counts
Is greater than k (meaning too many letters needed to be changed)
Remove the left value from the hash
Increment the l pointer

Update the max len
"""


def character_replacement(s, k):
  # use sliding window
  # use a hash to keep counts
  # return max len
  l = 0
  counts = {}
  max_len = 0

  # iterate over the string tracking r pointer
  for r in range(len(s)):
    # add the right pointer to the counts hash
    counts[s[r]] = 1 + counts.get(s[r], 0)

    # if the length of the window minus the maximum of the counts is greater than k
    # slide the l pointer up and remove it's value from the counts hash
    if r - l + 1 - max(counts.values()) > k:
      counts[s[l]] -= 1
      l += 1

    max_len = max(max_len, r - l + 1)

  return max_len

print(character_replacement("ABBA", 2)) # 4
print(character_replacement("AABABBA", 1)) # 4