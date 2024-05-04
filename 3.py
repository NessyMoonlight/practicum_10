with open('input3.txt', 'r') as f:
    lines = f.readlines()

first_letters = [line[0] for line in lines]
result_word = ''.join(first_letters)

with open('output.txt', 'w') as f:
    f.write(result_word)