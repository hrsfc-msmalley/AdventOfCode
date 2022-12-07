# Advent of Code Day 7
# No space on device
import re

with open('input.txt') as f:
  file = [x.rstrip() for x in f.readlines()]

# Navigate through directories
directories = {}
current_directory = 'root'
i = 0
for command in file:
  if command[0:4] == '$ cd':
    if command[5:] != '..':
      directories[str(i)+command[5:]] = {'location': current_directory, 'size_of_files': 0}
      current_directory = str(i)+command[5:]
    else:
      current_directory = directories[current_directory]['location']
  else:
    possible_size = re.search('[0-9]+', command)
    if possible_size != None:
      directories[current_directory]['size_of_files'] += int(possible_size.group())
  i += 1    
def find_total_size_of_directory(target, directories):
  running_total = 0
  for directory in directories:
    if directory == target:
      running_total += directories[directory]['size_of_files']
    elif directories[directory]['location'] == target:
      running_total += find_total_size_of_directory(directory, directories)
    # else:
    #   print(running_total)
  return running_total


def task1_output(directories, max_size):
  output = 0
  for directory in directories:
    # print(directory)
    size = find_total_size_of_directory(directory, directories)
    if size <= max_size:
      output += size
  return output

print(f"Task 1: {task1_output(directories, 100000)}")

def task2_output(directories, max_size):
  TOTAL_SPACE = 70000000
  free_space_needed = max_size
  current_space_used = find_total_size_of_directory('root', directories)
  target_file_size = max_size - (TOTAL_SPACE - current_space_used)
  best_size = TOTAL_SPACE
  for directory in directories:
    size = find_total_size_of_directory(directory, directories)
    if size >= target_file_size and size < best_size:
      best_size = size
  return best_size      

print(f"Task 2: {task2_output(directories, 30000000)}")
