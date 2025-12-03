
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
        print(f"Processing battery: {battery}")
        max_number = 0
        need = 12
        n = len(battery)
        if n >= need:
            pos = 0
            picked = []
            for remaining in range(need, 0, -1):
                # we must pick one from indices pos..(n-remaining)
                end = n - remaining
                best_digit = None
                best_idx = None
                for idx in range(pos, end + 1):
                    d = battery[idx]
                    if best_digit is None or d > best_digit:
                        best_digit = d
                        best_idx = idx
                    if best_digit == "9":  # can't do better than 9
                        break
                picked.append(best_digit)
                pos = best_idx + 1
            max_number = int("".join(picked))
        else:
            max_number = 0

        print(max_number)
        sum += max_number

    print(f"Sum of max numbers: {sum}")