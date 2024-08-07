"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', 
each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, 
that is, if at any time you are on a location you have previously visited. 
Return false otherwise.

Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Constraints:
1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.
"""

def is_path_crossing(path):
  coords = [0, 0]
  visited = set()
  visited.add(tuple(coords))

  for char in path:
    if char == "N":
      coords[1] += 1
    if char == "S":
      coords[1] -= 1
    if char == "E":
      coords[0] += 1
    if char == "W":
      coords[0] -= 1

    if tuple(coords) in visited:
      return True
    else:
      visited.add(tuple(coords))

  return False

    



print(is_path_crossing("NES")) # false
print(is_path_crossing("NESWW")) # true
