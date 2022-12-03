import string

# Import the File
with open('input.txt') as f:
  sack = [line.rstrip() for line in f]

# Create letter values dictionary
letter_values = {}
# Import letters
valid_letters = string.ascii_lowercase + string.ascii_uppercase 
# Populate the dictionary by looping through letters and adding the value
i = 1
for letter in valid_letters:
  letter_values[letter] = i
  i += 1

#print(lettervalues)

# Identify duplicate letter for each half of sack
total1 = 0
for items in sack:
  length = len(items)
  half_length = int(length / 2)
  set_left = set(items[0:half_length])
  set_right = set(items[half_length:length])
  misplaced_item = set_right.intersection(set_left)
  #print(misplaced_item)
  item_value = letter_values[list(misplaced_item)[0]]
  #print(item_value)
  total1 += item_value

print(f"Task 1 total = {total1}")

# Identify duplicate letter for each 3 sacks
total2 = 0
i = 0
for items in sack:
  if i % 3 == 0:
    set1 = set(items)
  elif i % 3 == 1:
    set2 = set(items)
  else:
    set3 = set(items)
    misplaced_item = set1.intersection(set2).intersection(set3)
    item_value = letter_values[list(misplaced_item)[0]]
    total2 += item_value
  i += 1
  
print(f"Task 2 total = {total2}")
