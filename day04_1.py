map = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@."
]

if __name__ == "__main__":

    with open("day04.txt", "r") as file:
        map = [line.strip() for line in file.readlines()]

    total = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "@":
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(map) and 0 <= nj < len(map[ni]):
                            if map[ni][nj] == "@":
                                count += 1
                if count < 4:
                    total += 1

    print(total)