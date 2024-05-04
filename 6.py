try:
    with open('input6.txt', 'r') as f:
        data = f.readlines()

    n = data[0]
    if int(n) == len(data) - 1:
        result = "YES"
    else:
        result = "NO"

except (ValueError, IndexError):
    result = "ERROR"

with open('output.txt', 'w') as f:
    f.write(result)