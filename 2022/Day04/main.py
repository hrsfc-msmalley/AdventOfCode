# Advent of Code Day 4
import re

# Import the file
with open('input.txt') as f:
  sections = [line.rstrip() for line in f]

# Parse section pairs, and convert to sets
def pair_parse(section_pair):
  x = re.findall("[0-9]+", section_pair)
  #print(x)
  pair1start = int(x[0])
  pair1end = int(x[1])
  pair2start = int(x[2])
  pair2end = int(x[3])
  set1 = set([x for x in range(pair1start, pair1end + 1)])
  set2 = set([x for x in range(pair2start, pair2end + 1)])
  return (set1, set2)

# Check if either pair is a subset of the other
# A.issubset(B)
def is_set_subset(set_pair):
  set1 = set_pair[0]
  set2 = set_pair[1]
  return (set1.issubset(set2) or set2.issubset(set1))

# Check if any elements of one set exists in the other
# A.issubset(B)
def is_set_overlap(set_pair):
  set1 = set_pair[0]
  set2 = set_pair[1]
  return not (set1.isdisjoint(set2))

# Count number of subsets
def count_subsets(input_data, function):
  count = 0
  for section in input_data:
    if function(pair_parse(section)):
      count += 1
  return count

print(f"Task 1 count: {count_subsets(sections, is_set_subset)}")
print(f"Task 2 count: {count_subsets(sections, is_set_overlap)}")

