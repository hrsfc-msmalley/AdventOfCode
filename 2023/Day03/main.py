#AoC Day3 Solution
#file_name = 'trial.txt' #Trial 1 expected 4361, Trial 2 expected 467835
file_name = 'input.txt' 

with open(file_name, 'r') as f:
    input_lines = f.readlines()

def strip_newline(input):
  output = []
  for line in input:
    output.append(line.rstrip())
  return output

input_lines = strip_newline(input_lines)


# Loop through and create an array that stores (bool isDigit,  bool adjacentSymbol, bool gear) for each coordinate
def find_neighbours(input_lines):
  number_of_rows = len(input_lines)
  number_of_columns = len(input_lines[0])
  neighbours = []
  gear_dict = {}
  gear_no = 0
  for i in range(number_of_rows):
    row = []
    for j in range(number_of_columns):
      isDigit = False
      adjacentSymbol = False
      gear_key = ""
      if input_lines[i][j].isdigit():
        isDigit = True
      for p in [-1, 0, 1]:
        for q in [-1, 0, 1]:
          if (i + p) >= 0 and (j + q) >= 0 and (i + p) < number_of_rows and (j + q) < number_of_columns:
            if input_lines[i + p][j + q] == '*':
              gear_key = str(i+p)+','+str(j+q)
              if gear_key not in gear_dict:
                gear_dict[gear_key] = gear_no
                gear_no += 1
            if input_lines[i + p][j + q].isdigit():
              continue
            elif input_lines[i + p][j + q] != '.':
              adjacentSymbol = True
            
      row.append((isDigit, adjacentSymbol, gear_key))
    neighbours.append(row)
  return neighbours, gear_dict

def list_to_integer(digits):
  result = 0
  for digit in digits:
    result = result * 10 + int(digit)
  return result

def find_valid_numbers(input_lines, neighbours, gear_dict):
  number_of_rows = len(input_lines)
  number_of_columns = len(input_lines[0])
  valid_numbers = []
  digits = []
  gear_vals = {}
  gear_no = -1
  valid = False
  gear = False
  for i in range(number_of_rows):
    if digits != [] and valid:
      valid_numbers.append(list_to_integer(digits))
      if gear:
        if gear_no in gear_vals:
          operations = gear_vals[gear_no][2]
          if operations == 1:
            print(digits)
            print(gear_vals[gear_no][0])
          number = gear_vals[gear_no][1]
          gear_vals[gear_no][0] = number * list_to_integer(digits)
          
          gear_vals[gear_no][2] = operations + 1
        else:
          gear_vals[gear_no] = [0,list_to_integer(digits),0]
    digits = []
    valid = False
    gear = False
    key = ""
    gear_no = -1
    for j in range(number_of_columns):
      #isDigit
      if neighbours[i][j][0]:
        digits.append(input_lines[i][j])
        #neighboursSymbol
        if neighbours[i][j][1]:
          valid = True
          key = neighbours[i][j][2]
          if key in gear_dict:
            gear = True
            gear_no = gear_dict[key]

      #neighboursDigit
      elif not neighbours[i][j][0] and valid:
        valid = False
        valid_numbers.append(list_to_integer(digits))
        number = 0
        if gear:
          if gear_no in gear_vals:
            operations = gear_vals[gear_no][2]
            # if operations == 1:
            #   print(digits)
            #   print(gear_vals[gear_no][0])
            number = gear_vals[gear_no][1]
            gear_vals[gear_no][0] = number * list_to_integer(digits)

            gear_vals[gear_no][2] = operations + 1
          else:
            gear_vals[gear_no] = [0,list_to_integer(digits),0]
        digits = []
        gear = False
      else:
        valid = False
        gear = False
        key = ""
        digits = []
        gear_no = -1

  return valid_numbers, gear_vals


def tasks(input_lines):
  task1_sum = 0
  task2_sum = 0
  neighbours, gear_dict = find_neighbours(input_lines)
  #print(neighbours)
  #print(gear_dict)
  valid_numbers, gear_vals = find_valid_numbers(input_lines, neighbours, gear_dict)
  #print(gear_vals)
  for num in valid_numbers:
    task1_sum += num

  for gear in gear_vals:
    task2_sum += gear_vals[gear][0]
    #if gear_vals[gear][2] > 1:
      #print(gear)
      #print(gear_vals[gear])
  #print(gear_dict)


  return task1_sum, task2_sum

ans1, ans2 = tasks(input_lines)

print(f"Task 1: {ans1}")
print(f"Task 2: {ans2}")
