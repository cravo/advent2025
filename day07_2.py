data =[
".......S.......",
"...............",
".......^.......",
"...............",
"......^.^......",
"...............",
".....^.^.^.....",
"...............",
"....^.^...^....",
"...............",
"...^.^...^.^...",
"...............",
"..^...^.....^..",
"...............",
".^.^.^.^.^...^.",
"...............",
]

def set_char(row, col, char):
    global data
    data[row] = data[row][:col] + char + data[row][col+1:]

def count_splits(row, col, memo=None):
    if memo is None:
        memo = {}
    
    if row >= len(data):
        return 0
    if col < 0 or col >= len(data[0]):
        return 0
    
    if (row, col) in memo:
        return memo[(row, col)]
    
    count = 0
    if data[row][col] == '^':
        left_count = count_splits(row + 1, col - 1, memo)
        right_count = count_splits(row + 1, col + 1, memo)
        count = 1 + left_count + right_count
    else:
        count = count_splits(row + 1, col, memo)
    
    memo[(row, col)] = count
    return count

if __name__ == "__main__":

    with open("day07.txt", "r") as file:
        data = file.readlines()
        
    col = data[0].index('S')

    rows = len(data)
    cols = len(data[0])

    splits = 1 + count_splits(1, col)
                
    print(splits)
    