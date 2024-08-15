"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, 
and the sign represents its direction (positive meaning right, negative meaning left). 
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.


Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

def asteroid_collision(asteroids: list[int]) -> list[int]:
  # use a stack to add all positive elements
  # if negative
  # while absolute value of negative is greater then last stack, pop the stack
  # if equal, pop the stack and move on to next iteration
  # if less, move on to next iteration
  stack = []
  for asteroid in asteroids:
    if asteroid > 0:
      stack.append(asteroid)
    else:
      while abs(asteroid) > stack[-1]:
        stack.pop()
      if abs(asteroid) == stack[-1]:
        stack.pop()
        continue
      if abs(asteroid) < stack[-1]:
        continue

  return stack

print(asteroid_collision([5, 10, -5])) # [5, 10]
print(asteroid_collision([8, -8])) # []
print(asteroid_collision([10, 2, -5])) # [10]