idRanges = []

total = 0

def find_invalid_ids(start, end):
    for idNum in range(start, end + 1):
        idStr = str(idNum)
        length = len(idStr)
        isValid = True

        for i in range(1, length // 2 + 1):
            half = idStr[:i]
            if half + half == idStr:
                isValid = False
                break

        if not isValid:
            global total
            total += int(idNum)
            print(f"Invalid ID found: {idNum}")

if __name__ == "__main__":
    with open("day02.txt", "r") as file:
        idRanges = file.read().strip().split(",")

    total = 0
    for idRange in idRanges:
        start, end = map(int, idRange.split("-"))
        print(f"Checking range: {start} to {end}")
        find_invalid_ids(start, end)

    print(f"Total of invalid IDs: {total}")