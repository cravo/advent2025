idRanges = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
"1698522-1698528","446443-446449","38593856-38593862","565653-565659",
"824824821-824824827","2121212118-2121212124"]

total = 0

def find_invalid_ids(start, end):
    for idNum in range(start, end + 1):
        idStr = str(idNum)
        length = len(idStr)
        isValid = True

        for i in range(1, length // 2 + 1):
            pattern = idStr[:i]
            if (pattern * (length // i)) == idStr and length % i == 0:
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