try:
    with open('input5.txt', 'r') as f:
        numbers = f.readlines()

    num1 = int(numbers[0])
    num2 = int(numbers[1])
    num3 = int(numbers[2])
    result = num1 / num2 + num3

except (ValueError) as v:
    result = "data error"
except (ZeroDivisionError) as z:
    result = "division by 0"

with open('output.txt', 'w') as f:
    f.write(str(result))