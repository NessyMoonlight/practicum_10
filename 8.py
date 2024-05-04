with open('input.txt', 'r') as f:
    steps_data = f.readlines()

steps_month = [0] * 12
days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, steps in enumerate(steps_data):
    month_index = i % 12
    steps_month[month_index] += int(steps)

average = [steps // days_month[i] for i, steps in enumerate(steps_month)]

with open('output.txt', 'w') as f:
    for a in average:
        f.write(str(a) + '\n')