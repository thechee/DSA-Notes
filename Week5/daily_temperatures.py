"""
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, 
keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

def daily_temperatures(temperatures: list[int]) -> list[int]:
  answer = [0] * len(temperatures)
  stack = []
  # as we iterate through temperatures
  for i in range(len(temperatures)):
  # while this temp is greater than the last temp on the stack
    while stack and temperatures[i] > stack[-1][0]:
  # pop off the stack
      popped = stack.pop()
  # replace answers[stack_index] the difference between current index and stack index
      answer[popped[1]] = i - popped[1] 
  # save current temp into stack the temp and the index
    stack.append([temperatures[i], i])

  return answer

print(daily_temperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60])) # [1,1,1,0]
print(daily_temperatures([30,60,90])) # [1,1,0]