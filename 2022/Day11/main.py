# Advent of Code 2022 Day 11
# Lost of Monkeys

import math
from copy import deepcopy


# Initialise inputs
def times5(x):
  return x * 5


def squared(x):
  return x * x


def times7(x):
  return x * 7


def add1(x):
  return x + 1


def add3(x):
  return x + 3


def add5(x):
  return x + 5


def add8(x):
  return x + 8


def add2(x):
  return x + 2


monkeys = {
  0: {
    "starting_items": [92, 73, 86, 83, 65, 51, 55, 93],
    "operation": lambda num: times5(num),
    "divtest": 11,
    "true": 3,
    "false": 4,
    "count": 0
  },
  1: {
    "starting_items": [99, 67, 62, 61, 59, 98],
    "operation": lambda num: squared(num),
    "divtest": 2,
    "true": 6,
    "false": 7,
    "count": 0
  },
  2: {
    "starting_items": [81, 89, 56, 61, 99],
    "operation": lambda num: times7(num),
    "divtest": 5,
    "true": 1,
    "false": 5,
    "count": 0
  },
  3: {
    "starting_items": [97, 74, 68],
    "operation": lambda num: add1(num),
    "divtest": 17,
    "true": 2,
    "false": 5,
    "count": 0
  },
  4: {
    "starting_items": [78, 73],
    "operation": lambda num: add3(num),
    "divtest": 19,
    "true": 2,
    "false": 3,
    "count": 0
  },
  5: {
    "starting_items": [50],
    "operation": lambda num: add5(num),
    "divtest": 7,
    "true": 1,
    "false": 6,
    "count": 0
  },
  6: {
    "starting_items": [95, 88, 53, 75],
    "operation": lambda num: add8(num),
    "divtest": 3,
    "true": 0,
    "false": 7,
    "count": 0
  },
  7: {
    "starting_items": [50, 77, 98, 85, 94, 56, 89],
    "operation": lambda num: add2(num),
    "divtest": 13,
    "true": 4,
    "false": 0,
    "count": 0
  },
}

divs = []
for i in monkeys:
  divs.append(monkeys[i]["divtest"])

common_divisor = math.prod(divs)


def monkey_business(input_monkeys, rounds):
  monkeys = deepcopy(input_monkeys)
  for j in range(rounds):
    # if j % 100 == 0:
    #   print(j)
    for i in range(len(monkeys)):
      for item in monkeys[i]["starting_items"]:
        # print()
        # print(item)
        worry = monkeys[i]["operation"](item)
        # print(worry)
        if rounds == 20:
          worry = worry // 3
        else:
          worry = worry % common_divisor
        # print(worry)
        if worry % monkeys[i]["divtest"] == 0:
          true_loc = monkeys[i]["true"]
          monkeys[true_loc]["starting_items"].append(worry)
        else:
          false_loc = monkeys[i]["false"]
          monkeys[false_loc]["starting_items"].append(worry)
        monkeys[i]["count"] += 1
      monkeys[i]["starting_items"] = []
      # print(monkeys[i]["starting_items"])
  return monkeys


new_monkeys1 = monkey_business(monkeys, 20)
scores1 = []
for i in new_monkeys1:
  scores1.append(new_monkeys1[i]["count"])

scores1.sort(reverse=True)
print(f"Task 1: {scores1[0]*scores1[1]}")

new_monkeys2 = monkey_business(monkeys, 10000)
scores2 = []
for i in new_monkeys2:
  scores2.append(new_monkeys2[i]["count"])

scores2.sort(reverse=True)
print(f"Task 2: {scores2[0]*scores2[1]}")
