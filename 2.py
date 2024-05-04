with open('input2.txt', 'r') as f:
    lines = f.readlines()

filtered_lines = [line for line in lines if line.upper().startswith('A')]

with open('output.txt', 'w') as f:
    for line in filtered_lines:
        f.write(line)