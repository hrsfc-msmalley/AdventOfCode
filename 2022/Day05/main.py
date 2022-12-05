# Advent of Code Day 5
# Identify final stack arrangements given initial stacks and movements
import re

# Import the file
with open('input.txt') as f:
  inputfile = [line.rstrip() for line in f]

# Initialise stacks
def initialise_stacks(inputdata):
  # Get number of stacks and create blank list of stacks
  for line in inputdata:
    if line == "":
      break
    else:
      match = re.findall("[0-9]+", line)
  number_of_stacks = int(match[-1])
  stacks = [[] for i in range(number_of_stacks)]
  # Populate stacks
  matches = []
  for line in inputdata:
    if line == "":
      break
    else:
      matches.append(re.finditer("[A-Z]+", line))
  for match in reversed(matches):
    for item in match:
      stack = int((item.start() + 3) / 4) - 1
      stacks[stack].append(item.group())
  return stacks


# Get move instructions
def move_instructions(inputdata):
  matches = []
  moves = []
  for line in inputdata:
    matches.append(re.findall("[0-9]+", line))
    if line == "":
      matches = []

  for match in matches:
    move = [match[0], match[1], match[2]]
    moves.append(move)
  
  return moves

# Moving things about stacks
def move1(stacks, repeats, source, destination):
  for i in range(repeats):
    item = stacks[source - 1].pop()
    stacks[destination - 1].append(item)
  return stacks

def move2(stacks, repeats, source, destination):
  moving_items = []
  for i in range(repeats):
    moving_items.append(stacks[source - 1].pop())

  for item in reversed(moving_items):    
    stacks[destination - 1].append(item)
    
  return stacks
  
def stack_moves(stacks, instructions, move):
  for instruction in instructions:
    repeats = int(instruction[0])
    source = int(instruction[1])
    destination = int(instruction[2])
    stacks = move(stacks, repeats, source, destination)
  return stacks

def get_required_output(stacks):
  output = ""
  for stack in stacks:
    letter = stack.pop()
    output += letter
  return output
  
stacks = initialise_stacks(inputfile)
instructions = move_instructions(inputfile)
final_stacks = stack_moves(stacks, instructions, move2)
output = get_required_output(final_stacks)
print(output)


