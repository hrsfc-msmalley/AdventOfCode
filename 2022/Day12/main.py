# Advent of Code 2022 - Day 12
# Signals in the hills

with open('input.txt') as f:
  map_input = [x.rstrip() for x in f.readlines()]

# Go from S to E in the shortest route, only changing height by 1 level at a time (a->b, e->f etc), and only moving orthogonally

# Find S and E
for i in range(len(map_input)):
  for j in range(len(map_input[0])):
    if map_input[i][j] == 'S':
      #print(f"S i {i}, j {j}")
      S = (i, j)
    if map_input[i][j] == 'E':
      #print(f"E i {i}, j {j}")
      E = (i, j)


def is_valid_move(char1, char2):
  if char1 == "S" and (char2 == "a" or char2 == "b"):
    return True
  elif (char1 == "z" or char1 == "y") and char2 == "E":
    return True  
  elif char2 != "E" and char2 <= chr(ord(char1) + 1):
    return True
  else:
    return False

def move(start_pos, direction, maps):
  if direction == 0:
    new_pos = (start_pos[0]-1, start_pos[1])
  elif direction == 1:
    new_pos = (start_pos[0]+1, start_pos[1])
  elif direction == 2:
    new_pos = (start_pos[0], start_pos[1]+1)
  else:
    new_pos = (start_pos[0], start_pos[1]-1)
  
  try:
    if is_valid_move(maps[start_pos[0]][start_pos[1]], maps[new_pos[0]][new_pos[1]]):
      return new_pos
    else:
      return start_pos
  except:
    return start_pos


def breadth_first_search(maps, starting_position, target):
  start = (starting_position, 0) # (node, distance)
  visited = [starting_position]
  queue = [start]

  while queue:
    s = queue.pop(0)
    position = s[0]
    count = s[1]
 
    if position == target:
        return s[1]
    
    for direction in range(4):
      new_position = move(position, direction, maps)
      if new_position not in visited:
        next_node = (new_position, count+1)
        visited.append(new_position)
        queue.append(next_node)
      
  #print_map(maps, visited, s)
  return -1 #target not found

def find_all_as(maps):
  locations = []
  for i in range(len(maps)):
    for j in range(len(maps[0])):
      if maps[i][j] == 'a' or maps[i][j] == "S":
        locations.append((i,j))
  return locations

def find_min_steps(starting_points, maps, target):
  min_steps = 99999999999
  for point in starting_points:
    steps = breadth_first_search(maps, point, target)
    if steps < min_steps and steps != -1:
      min_steps = steps
  return min_steps
  
# def print_map(map_input, visited, current):
#   print("\033[H\033[2J", end="")
#   height = len(map_input)
#   width = len(map_input[0])
#   for i in range(height):
#     print()
#     for j in range(width):
#       if (i,j) == current:
#         print("X", end="")
#       elif (i,j) in visited:
#         print("x", end = "")
#       else:
#         print(".",end="")
      
        


print(f"Task 1 steps: {breadth_first_search(map_input, S, E)}")
print(f"Task 2 steps: {find_min_steps(find_all_as(map_input), map_input, E)}")
