# Advent of Code Day 6
# Communication Packets

# import file
with open('input.txt') as f:
  inputfile = [line.rstrip() for line in f]

# As one line input file
datastream = inputfile[0]

# Find location of first 4 sequential unique characters
def find_start_of_thing(stream, marker_len):
  current_letters = set()
  for i in range(len(stream)):
    if i >= marker_len:
      for j in range(marker_len):
        current_letters.add(stream[i-j])
    #print(current_letters)
    if len(current_letters) == marker_len:
      return i + 1
    current_letters.clear()
  return -1

print(f"Task 1: {find_start_of_thing(datastream,4)}")
print(f"Task 2: {find_start_of_thing(datastream,14)}")     
