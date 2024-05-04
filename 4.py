with open('input4.txt', 'r') as f:
    lines = f.readlines()

long_lines = [line for line in lines if len(line) > 20]

with open('output.txt', 'w') as f:
    for line in long_lines:
        f.write(line)