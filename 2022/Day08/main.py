# Advent of Code 2022 Day 8
# Treehouse planning

# Import file
with open('input.txt') as f:
  inputgrid = [x.rstrip() for x in f.readlines()]

GRID_WIDTH = len(inputgrid[0])
GRID_DEPTH = len(inputgrid)

# Check a given tree is visible
def check_tree_visible(x,y,grid, grid_width, grid_depth):
  height_of_current_tree = grid[x][y]
  is_visible = True
  x1_visible = True
  x2_visible = True
  y1_visible = True
  y2_visible = True
  if x == 0 or y == 0 or x == grid_width - 1 or y == grid_depth - 1:
    return is_visible
  # Check heights for i < x
  for i in range(x):
    if grid[i][y] >= height_of_current_tree:
      x1_visible = False
      break
  # Check heights for i > x
  for j in range(x+1,grid_width):
    if grid[j][y] >= height_of_current_tree:
      x2_visible = False
      break
  # Check heights for j < y
  for k in range(y):
    if grid[x][k] >= height_of_current_tree:
      y1_visible = False
      break
  # Check heights for j > y
  for l in range(y+1, grid_depth):
    if grid[x][l] >= height_of_current_tree:
      y2_visible = False
      break
  if not (x1_visible or x2_visible or y1_visible or y2_visible):
    is_visible = False
    return is_visible
  else:
    return is_visible

# Number of trees visibile
def count_visible_trees(grid, width, depth):
  count = 0
  for i in range(width):
    for j in range(depth):
      if check_tree_visible(i,j,grid,width,depth):
        count += 1
      #   print(1, end = "")
      # else:
      #   print(0,end="")
    # print()
  return count

# Scenic score (distance to >= tall tree in all 4 directions, multiplied together)
def scenic_score(x,y,grid, grid_width, grid_depth):
  height_of_current_tree = grid[x][y]
  x1_distance = 0
  x2_distance = 0
  y1_distance = 0
  y2_distance = 0
  # Check distances for i < x
  for i in reversed(range(x)):
    if x == 0:
      x1_distance = 0
      break
    elif grid[i][y] >= height_of_current_tree or i == 0:
      x1_distance = (x - i)
      break
  # Check heights for i > x
  for j in range(x+1,grid_width):
    if x == grid_width - 1:
      x2_distance = 0
      break
    elif grid[j][y] >= height_of_current_tree or j == grid_width - 1:
      x2_distance = (j - x)
      break
  # Check heights for j < y
  for k in reversed(range(y)):
    if y == 0:
      y1_distance = 0
      break
    elif grid[x][k] >= height_of_current_tree or k == 0:
      y1_distance = (y - k)
      break
  # Check heights for j > y
  for l in range(y+1, grid_depth):
    if y == grid_depth - 1:
      y2_distance = 0
      break
    elif grid[x][l] >= height_of_current_tree or l == grid_depth - 1:
      y2_distance = (l - y)
      break
  return x1_distance * x2_distance * y1_distance * y2_distance

# Get max scenic score
def max_scenic_score(grid, width, depth):
  score = 0
  for i in range(width):
    for j in range(depth):
      temp = scenic_score(i, j, grid, width, depth)
      # print(f"{i}, {j}, {temp}")
      if temp > score:
        score = temp
  return score

print(f"Task 1: {count_visible_trees(inputgrid, GRID_WIDTH, GRID_DEPTH)}")
print(f"Task 2: {max_scenic_score(inputgrid, GRID_WIDTH, GRID_DEPTH)}")
