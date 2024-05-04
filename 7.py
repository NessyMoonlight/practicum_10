with open('input7.txt', 'r') as f:
    lines = f.readlines()
    lines_filtered = [line for line in lines if '100' not in line or\
                      ('100' in line and '1000' in line)]

with open('output.txt', 'w') as f:
    f.writelines(lines_filtered)
