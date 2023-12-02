#AoC Day2 Solution
#file_name = 'trial.txt' #Trial 1 expected 8, Trial 2 expected 2286
file_name = 'input.txt' 

max_red = 12
max_green = 13
max_blue = 14

with open(file_name, 'r') as f:
    input_lines = f.readlines()

# Find max cubes for each colour for each game
def find_max_cubes(input_line):
  game = input_line.split(":")[0][5:]
  #print(game)
  game_info = input_line.rstrip().split(":")[1].split(";")
  #print(game_info)
  max_counts = {'red': 0, 'green': 0, 'blue': 0 } #RGB
  for subset in game_info:
    cubes = subset.split(", ")
    for cube in cubes:
      count, colour = cube.split()
      count = int(count)
      max_counts[colour] = max(max_counts[colour], count)
  
  return [game, max_counts]

# Check which games are possible (max_cubes for each colour <= max_colour)
def is_game_valid(game, max_red, max_green, max_blue):
  if max_red >= game[1]['red'] and max_green >= game[1]['green'] and max_blue >= game[1]['blue']:
    return True
  else:
    return False


def task_1(input_lines, max_red, max_green, max_blue):
  game_sum = 0
  for line in input_lines:
    game_info = find_max_cubes(line)
    if is_game_valid(game_info, max_red, max_green, max_blue):
      game_sum += int(game_info[0])
  return game_sum

def task_2(input_lines):
  game_sum_powers = 0
  for line in input_lines:
    game_info = find_max_cubes(line)
    game_sum_powers += game_info[1]['red'] * game_info[1]['green'] * game_info[1]['blue']
  return game_sum_powers


print(f"Task 1: {task_1(input_lines, max_red, max_green, max_blue)}")
print(f"Task 2: {task_2(input_lines)}")
