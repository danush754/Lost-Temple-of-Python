dict1 = {"first_quarter": 10, "second_quarter": 20}
dict2 = {"third_quarter": 30, "fourth_quarter": 40}
first_half = 0
second_half = 0
for quarter in dict1:
    goals = dict1[quarter]
    first_half += goals
for quarter in dict2:
    goals = dict2[quarter]
    second_half += goals
total_score = first_half + second_half
print(total_score)