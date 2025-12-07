problems = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   + "
]

if __name__ == "__main__":

    with open("day06.txt", "r") as file:
        problems = [line.strip() for line in file.readlines()]

    total = 0
    num_cols = len(problems[0].split())

    for col in range(num_cols):
        values = []
        operation = None
        
        for row in range(len(problems)):
            col_data = problems[row].split()
            if col < len(col_data):
                data = col_data[col]
                if data == '*' or data == '+':
                    operation = data
                else:
                    values.append(int(data))
        
        if operation == '+':
            result = sum(values)
        elif operation == '*':
            result = 1
            for val in values:
                result *= val
        
        total += result

    print(total)