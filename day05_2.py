database = [
"3-5",
"10-14",
"16-20",
"12-18",
"",
"1",
"5",
"8",
"11",
"17",
"32"  
]

if __name__ == "__main__":

    with open("day05.txt", "r") as file:
        database = [line.strip() for line in file.readlines()]

    ranges = []
    i = 0
    while i < len(database) and database[i] != "":
        ranges.append(database[i])
        i += 1

    fresh = 0
    merged_ranges = []
    
    # Parse and sort ranges by start value
    parsed_ranges = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        parsed_ranges.append([start, end])
    parsed_ranges.sort()
    
    # Merge overlapping ranges
    for start, end in parsed_ranges:
        if not merged_ranges or merged_ranges[-1][1] < start - 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    for start, end in merged_ranges:
        fresh += (end - start) + 1

    print(fresh)