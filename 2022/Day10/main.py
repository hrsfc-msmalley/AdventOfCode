# Advent of Code Day 10
# CRT Clock

# Import inputs
with open('input.txt') as f:
  instructions_input = [x.rstrip() for x in f.readlines()]

# Initialise variables
x = 1
cycle = 1
cycles_of_interest = [20, 60, 100, 140, 180, 220]
cycles_of_interest2 = [40, 80, 120, 160, 200, 240]

def list_x_state_at_every_clock(instructions, x_initial):
  x = x_initial
  clock = 0
  xs = {1: x_initial}
  for instruction in instructions:
    #print(f"clock {clock}, inst {instruction}")
    if instruction == "noop":
      clock += 1
      if not xs.get(clock, False):
        xs[clock] = x
        
    else:
      x_val = int(instruction[4:])
      
      clock += 1
      if not xs.get(clock, False):
        xs[clock] = x        
      
      clock += 1
      xs[clock] = x
      
      x += x_val
      xs[clock+1] = x

    #print(xs)
  return xs

def sumproduct_specified_values(dict, values):
  sum = 0
  for value in values:
    sum += (dict[value] * value)
  return sum

list_x = list_x_state_at_every_clock(instructions_input, x)
print(f"Task 1: {sumproduct_specified_values(list_x, cycles_of_interest)}")

def draw_image(dict_x_cycles, values):
  previous_value = 0
  for value in values:
    print("")
    for i in range(previous_value + 1, value + 1):
      sprite_locations = [dict_x_cycles[i], dict_x_cycles[i]+1, dict_x_cycles[i]+2]
      if i%40 in sprite_locations:
        print("#", end = '')
      else:
        print(" ", end = '') # REPLACE '.' WITH ' ' TO MAKE IT READABLE
    previous_value = value

print("\nTask 2:")
draw_image(list_x, cycles_of_interest2)
