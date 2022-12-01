# Advent of Code 2022 - Day 1
# Finding the elf with the most calories

# Import the File
with open('input.txt') as f:
  lines = [line.rstrip() for line in f]

totals = [0]

i = 0
for line in lines:
  if line != "":
    totals[i] += int(line)
  else:
    totals.append(0)
    i += 1

totals.sort(reverse=True)

print(totals[0])
print(totals[0]+totals[1]+totals[2])
