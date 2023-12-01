#AoC Day1 Solution
#file_name = 'trial.txt' #Trial 1 expected 142
#file_name = 'trial2.txt' #Trial 2 expected 281
file_name = 'input.txt' 
task = 2

with open(file_name, 'r') as f:
    input_lines = f.readlines()

#THIS DOES NOT WORK
def extract_digits(input_string):
  digit_mapping = {
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9',
    "zero":'0'
  }

  digits = ""
  for i in range(len(input_string)):
    if input_string[i].isdigit():
      digits += input_string[i]
    else:
      for key in digit_mapping:
        word_len = len(key)
        word_end = i + word_len
        word = input_string[i:word_end]
        if key == word:
          digits += digit_mapping[word]
        
  return digits


def get_first_and_last_digit(input_string, test):
  if test == 1:
    digits = [char for char in input_string if char.isdigit()]
  elif test == 2:
    digits = extract_digits(input_string)
  else:
    print("No validtest specified")
    return 0
  #print(parsed_string)
  first_digit = digits[0]
  last_digit = digits[-1]
  return first_digit + last_digit


#Identify first and last characters in each line
total = 0
for line in input_lines:
  line_value = int(get_first_and_last_digit(line,task))
  total += line_value
print(f"Task {task} {total}")
