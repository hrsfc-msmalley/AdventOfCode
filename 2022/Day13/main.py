# Advent of Code 2022 Day 13
# Signal Descrambling

from functools import cmp_to_key

with open('input.txt') as f:
  input_signals = [x.rstrip() for x in f.readlines()]

def get_pairs_from_input(input_file):
  output = []
  for i in range(len(input_file)):
    if i % 3 == 0:
      output.append([eval(input_file[i]), eval(input_file[i+1])])
  return output

def pair_checker(left, right): # returns true if correct, false if switch required
  if type(left) == int and type(right) == int:
    return (left>right) - (left<right)
  elif type(left) == int and type(right) == list:
    return pair_checker([left], right)
  elif type(left) == list and type(right) == int:
    return pair_checker(left, [right])
  elif type(left) == list and type(right) == list:
    for z in map(pair_checker, left, right):
      if z: return z
    return pair_checker(len(left), len(right))
  else:
    return "Broken"

correct = []
pairs = get_pairs_from_input(input_signals)
for i in range(len(pairs)):
  if pair_checker(pairs[i][0], pairs[i][1]) == -1:
    correct.append(i+1)

sum_of_indices = sum(correct)
print(f"Task 1: {sum_of_indices}")

# How many packets smaller than [[2]]
count2 = 1
for i in range(len(pairs)):
  if pair_checker(pairs[i][0], [[2]]) == -1:
    count2 +=1
  if pair_checker(pairs[i][1], [[2]]) == -1:
    count2 +=1

# How many packets smaller than [[6]]
count6 = 2
for i in range(len(pairs)):
  if pair_checker(pairs[i][0], [[6]]) == -1:
    count6 +=1
  if pair_checker(pairs[i][1], [[6]]) == -1:
    count6 +=1

# loc [[2]] * loc[[6]]
decoder_key = count2 * count6
print(f"Task 2: {decoder_key}")
