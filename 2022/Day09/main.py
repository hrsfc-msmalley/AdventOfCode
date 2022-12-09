# Advent of Code 2022 Day 09
# Rope Bridge

with open('input.txt') as f:
  ropemovesinput = [x.rstrip() for x in f.readlines()]

moves_dict = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

def translate_move(move):
  x = moves_dict[move[0]][0]
  y = moves_dict[move[0]][1]
  repeats = int(move[2:])
  return [x, y, repeats]

moves_dict2 = {(0,0): [(-1,1), (0,1), (1,1),
                       (-1,0), (0,0), (1,0), 
                       (-1,-1), (0,-1), (1,-1)],
               (0,1): [(-1,1), (0,1), (1,1), 
                       (0,0), (0,0), (0,0), 
                       (0,0), (0,0), (0,0)],
              (1,1): [(0,1), (1,1), (1,1), 
                      (0,0), (0,0), (1,1), 
                      (0,0), (0,0), (1,0)],
              (1,0): [(0,0), (0,0), (1,1), 
                      (0,0), (0,0), (1,0), 
                      (0,0), (0,0), (1,-1)],
              (1,-1): [(0,0), (0,0), (1,0), 
                       (0,0), (0,0), (1,-1), 
                       (0,-1), (1,-1), (1,-1)],
              (0,-1): [(0,0), (0,0), (0,0), 
                       (0,0), (0,0), (0,0), 
                       (-1,-1), (0,-1), (1,-1)],
              (-1,-1): [(-1,0), (0,0), (0,0), 
                        (-1,-1), (0,0), (0,0), 
                        (-1,-1), (-1,-1), (0,-1)],
              (-1,0): [(-1,1), (0,0), (0,0), 
                       (-1,0), (0,0), (0,0), 
                       (-1,-1), (0,0), (0,0)],
              (-1,1): [(-1,1), (-1,1), (0,1), 
                       (-1,1), (0,0), (0,0), 
                       (-1,0), (0,0), (0,0)]}

def next_knot_move(head_x, head_y, move_dx, move_dy, tail_x, tail_y):
  dx = head_x - tail_x
  dy = head_y - tail_y
  reference_move = moves_dict2[(0,0)].index((dx, dy))
  tail_moves = moves_dict2[(move_dx, move_dy)][reference_move]
  return tail_moves


def task(movelist, ropelen):
  tail_locations = {(0,0)}
  current_knot_position = []
  previous_knot_position = [0,0]
  next_knot = [0,0]
  for i in range(ropelen):
    current_knot_position.append([0,0])
  for move in movelist:
    translated_move = translate_move(move) # [dx, dy, repeats]
    for _ in range(translated_move[2]):
      for knot in range(ropelen - 1):
        if knot == 0:
          current_move = translated_move[:2]
          next_knot = next_knot_move(current_knot_position[knot][0], current_knot_position[knot][1], current_move[0], current_move[1], current_knot_position[knot+1][0], current_knot_position[knot+1][1])
        else:
          current_move = next_knot
          if next_knot == (0,0):
            break
          else:
            next_knot = next_knot_move(previous_knot_position[0], previous_knot_position[1], current_move[0], current_move[1], current_knot_position[knot+1][0], current_knot_position[knot+1][1])
          
        #print(f"knot {knot}")
        #print(f"current move {current_move}")
        #print(f"next knot{next_knot}")
        if knot == 0:
          current_knot_position[knot][0] += current_move[0]
          current_knot_position[knot][1] += current_move[1]
        
        previous_knot_position[0] = current_knot_position[knot+1][0]
        previous_knot_position[1] = current_knot_position[knot+1][1]

        current_knot_position[knot+1][0] += next_knot[0]
        current_knot_position[knot+1][1] += next_knot[1]
        if knot == (ropelen - 2):
          tail_locations.add((current_knot_position[knot+1][0],current_knot_position[knot+1][1]))
        #print(current_knot_position)
        #print(f"tail {tail_locations}\n")


  return len(tail_locations)



print(f"Task 1 output: {task(ropemovesinput,2)}")
print(f"Task 2 output: {task(ropemovesinput,10)}")
