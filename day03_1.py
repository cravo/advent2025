batteries = ["987654321111111",
"811111111111119",
"234234234234278",
"818181911112111"
]

if __name__ == "__main__":

    with open("day03.txt", "r") as file:
        batteries = [line.strip() for line in file.readlines()]

    sum = 0
    for battery in batteries:
        max_number = 0
        for i in range(len(battery) - 1):
            for j in range(i + 1, len(battery)):
                two_digit_number = int(battery[i] + battery[j])
                if two_digit_number > max_number:
                    max_number = two_digit_number
        print(max_number)
        sum += max_number

    print(f"Sum of max two-digit numbers: {sum}")