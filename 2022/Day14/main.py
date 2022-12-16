# Advent of Code 2022 - Day 14
# Falling Sand

with open('input.txt') as f:
  input_contours = [x.rstrip() for x in f.readlines()]

def apply(item, fun):
    if isinstance(item, list):
        return [apply(x, fun) for x in item]
    else:
        return fun(item)

parsed_input_contours = [x.split(" -> ") for x in input_contours]
parsed_input_contours = apply(parsed_input_contours, eval)

def get_bounds(input_file):
  x_min = 9999999999
  y_min = 9999999999
  x_max = 0
  y_max = 0
  for line in input_file:
    for item in line:
      if item[0] > x_max:
        x_max = item[0]
      if item[0] < x_min:
        x_min = item[0]
      if item[1] > y_max:
        y_max = item[1]
      if item[1] < y_min:
        y_min = item[1]    
  return [x_min, x_max, y_min, y_max]

SOURCE = (500,0)
bounds = get_bounds(parsed_input_contours)

def make_grid(source, bounds):
  x_min = min(source[0], bounds[0] - 1)
  x_max = max(source[0], bounds[1] + 1)
  y_min = min(source[1], bounds[2] - 1)
  y_max = max(source[1], bounds[3] + 1)
  height = y_max - y_min + 1
  width = x_max - x_min + 1
  grid = [['.' for x in range(width)] for y in range(height)]
  return [grid, x_min, y_min]

grid, x_converter, y_converter = make_grid(SOURCE, bounds)

def add_contours(grid, x_conv, y_conv, contours):
  for contour in contours:
    for i in range(len(contour)):
      if i == 0:
        grid[contour[i][1]-y_conv][contour[i][0]-x_conv] = '#'
      else:
        if contour[i][0] == contour[i-1][0]:
          for j in range(abs(contour[i][1] - contour[i-1][1])):
            if contour[i][1] - contour[i-1][1] > 1:
              grid[contour[i][1]-y_conv-j][contour[i][0]-x_conv] = '#'
            else:
              grid[contour[i][1]-y_conv+j][contour[i][0]-x_conv] = '#'
        else:
          for j in range(abs(contour[i][0] - contour[i-1][0])):
            if contour[i][0] - contour[i-1][0] > 1:
              grid[contour[i][1]-y_conv][contour[i][0]-x_conv-j] = '#'
            else:
              grid[contour[i][1]-y_conv][contour[i][0]-x_conv+j] = '#'
      
  return grid

grid = add_contours(grid, x_converter, y_converter, parsed_input_contours)

# for i in range(len(grid)):
#   print(grid[i])

def add_sand(grid, SOURCE, x_conv, y_conv):
  falling = True
  source = list(SOURCE)
  source[0] = SOURCE[0] - x_conv
  source[1] = SOURCE[1] - y_conv
  sand_loc = source
  count = 0
  #print(sand_loc)
  while falling:
    # count += 1
    # print(count)
    # print(sand_loc)
    # input()
    if sand_loc[1] == len(grid)-1:
        status = 1
        return [grid, status]
    if grid[sand_loc[1]][sand_loc[0]] == 'o':
        status = 2
        return [grid, status]
    if grid[sand_loc[1]+1][sand_loc[0]] == '.':
      sand_loc[1] += 1
      continue
    elif grid[sand_loc[1]+1][sand_loc[0]-1] == '.':
      sand_loc[0] -= 1
      sand_loc[1] += 1
      continue
    elif grid[sand_loc[1]+1][sand_loc[0]+1] == '.':
      sand_loc[0] += 1
      sand_loc[1] += 1
      continue
    else:
      grid[sand_loc[1]][sand_loc[0]] = 'o'
      status = 0
      return [grid, status] #grid, status 0 for stopped, 1 for eternity

count = 0
while True:
  grid, status = add_sand(grid, SOURCE, x_converter, y_converter)
  count +=1
  if status == 1:
    break

  # for i in range(len(grid)):
  #   for j in range(len(grid[i])):
  #     print(grid[i][j], end="")
  #   print()
  # input("next")

print(count-1)

for i in range(len(grid)):
    for j in range(len(grid[i])):
      print(grid[i][j], end="")
    print()

def floor_coords(source, y_max):
  # Needs to be at y_max + 1
  # Needs to be around (y_max + 2) * 2 wide
  y_max = y_max + 0
  half_width = y_max + 4
  new_x1 = source[0] - half_width
  new_x2 = source[0] + half_width
  line = [(new_x1, y_max), (new_x2, y_max)]
  return line


parsed_input_contours.append(floor_coords(SOURCE, bounds[3]+2))
new_bounds = get_bounds(parsed_input_contours)
new_grid, new_x_converter, new_y_converter = make_grid(SOURCE, new_bounds)
new_grid = add_contours(new_grid, new_x_converter, new_y_converter, parsed_input_contours)

count2 = 0
while True:
  new_grid, status = add_sand(new_grid, SOURCE, new_x_converter, new_y_converter)
  count2 +=1
  if status == 2:
    break
  # for i in range(len(new_grid)):
  #   for j in range(len(new_grid[i])):
  #     print(new_grid[i][j], end="")
  #   print()
  # input("next")

print(count2 - 1)


for i in range(len(new_grid)):
    for j in range(len(new_grid[i])):
      print(new_grid[i][j], end="")
    print()
