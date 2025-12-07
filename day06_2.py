problems = [
"123 328  51 64 ",
" 45 64  387 23 ",
"  6 98  215 314",
"*   +   *   +  "
]



if __name__ == "__main__":

    with open("day06.txt", "r") as file:
        problems = file.readlines()

    total = 0
    num_cols = len(problems[0])
    num_rows = len(problems)

    for col in range(num_cols):
        if col < num_cols - 1:
            operation = problems[-1][col]
            if operation != ' ':
                numbers = []
                
                while col < num_cols:
                    digits = []
                    for row in range(num_rows - 1):
                        char = problems[row][col]
                        if char.isdigit():
                            digits.append(char)
                    if not digits:
                        break
                    else:
                        numbers.append(int(''.join(digits)))
                        col += 1

                print(numbers, operation)
                if operation == '+':
                    result = sum(numbers)
                elif operation == '*':
                    result = 1
                    for val in numbers:
                        result *= val
                total += result
    print(total)