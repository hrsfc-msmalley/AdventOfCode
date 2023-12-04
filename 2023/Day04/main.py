#AoC Day4 Solution
file_name = 'trial.txt' #Trial 1 expected 13, Trial 2 expected 30
file_name = 'input.txt' 

with open(file_name, 'r') as f:
    input_lines = f.readlines()

def strip_newline(input):
  output = []
  for line in input:
    output.append(line.rstrip())
  return output

input_lines = strip_newline(input_lines)

def line_splitter(input_line):
  split_line = input_line.split(":")
  card = split_line[0].split(" ")[-1]
  numbers = split_line[1].split("|")
  winning_numbers = [x for x in numbers[0].split(" ") if x != '']
  selected_numbers = [x for x in numbers[1].split(" ") if x != '']

  return card, winning_numbers, selected_numbers

def calculate_number_of_winners(winning_numbers, selected_numbers):
  total = 0
  for number in selected_numbers:
    if number in winning_numbers:
      total += 1
  return total

def calculate_points(matches):
  total = 0
  if matches == 1:
    total = 1
  elif matches >= 2:
    total = 2 ** (matches - 1)
  else:
    total = 0
  #print(total)
  return total


def tasks(input_lines):
  task1_sum = 0
  task2_sum = 0
  points = [] #task 1
  card_dict = {} #task 2
  number_of_matches = 0
  for line in input_lines:
    card, winning_numbers, selected_numbers = line_splitter(line)
    if str(card) not in card_dict:
      card_dict[str(card)] = 1
      card_quantity = 1
    else:
      card_quantity = card_dict[str(card)]
    number_of_matches = calculate_number_of_winners(winning_numbers, selected_numbers)
    # Task 1
    points.append(calculate_points(number_of_matches))
    # Task 2
    for i in range(number_of_matches):
      new_card_key = str(int(card) + i + 1)
      if new_card_key not in card_dict:
        card_dict[new_card_key] = 1 + (1 * card_quantity)
      else:
        card_dict[new_card_key] = card_dict[new_card_key] + (1 * card_quantity)
      
      


  task1_sum = sum(points)
  card_sum = []
  for key in card_dict:
    card_sum.append(card_dict[key])
  task2_sum = sum(card_sum)

  return task1_sum, task2_sum

ans1, ans2 = tasks(input_lines)

print(f"Task 1: {ans1}")
print(f"Task 2: {ans2}")
