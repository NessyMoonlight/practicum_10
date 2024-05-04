with open('input.txt', 'r') as f:
    t = f.read()
new_t = t.upper()

with open('output.txt', 'w') as s:
    s.write(new_t)
