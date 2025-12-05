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

    ingredients = []
    for j in range(i + 1, len(database)):
        ingredients.append(database[j])

    fresh = 0
    for ingredient in ingredients:
        ingredient_num = int(ingredient)
        for r in ranges:
            start, end = map(int, r.split('-'))
            if start <= ingredient_num <= end:
                fresh += 1
                break

    print(fresh)