# Advent of Code 2022 Day 2
# Rock Paper Scissors Strategy Guide

# Load the input
with open('input.txt') as f:
    lines = f.readlines()

strategy = [x.rstrip() for x in lines]
throw_values = {"A":1,"B":2,"C":3}
outcome_values = {"X":0, "Y":3, "Z":6}

# Calculate winner
# def winner(player, opponent):
#    if (player == "X" and opponent == "A") or (player == "Y" and opponent == "B") or (player == "Z" and opponent == "C"):
#       return 3
#   elif (player == "X" and opponent == "C") or (player == "Y" and opponent == "A") or (player == "Z" and opponent == "B"):
#       return 6
#   else:
#       return 0

# Calculate throw
def throw(opponent, outcome):
    if outcome == "Y":
        return opponent
    elif outcome == "Z":
        if opponent == "A":
            return "B"
        elif opponent == "B":
            return "C"
        else:
            return "A"
    else:
        if opponent == "A":
            return "C"
        elif opponent == "B":
            return "A"
        else:
            return "B"

# Calculate score for 1 round
def round_score(round):
    #return winner(round[2], round[0]) + throw_values[round[2]]
    return throw_values[throw(round[0], round[2])] + outcome_values[round[2]]
    

# Calculate total score
score = 0
for round in strategy:
    score += round_score(round)

# Give output
print(score)
#print(round_score(strategy[0]))
