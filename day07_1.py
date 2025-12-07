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

if __name__ == "__main__":

    with open("day07.txt", "r") as file:
        data = file.readlines()
        
    col = data[0].index('S')
    set_char(1, col, '|')

    rows = len(data)
    cols = len(data[0])
    splits = 0

    for r in range(1, rows - 1):
        for c in range(cols):
            if(data[r][c] == '|'):
                below = data[r+1][c]
                if below == '.':
                    set_char(r+1, c, '|')
                elif below == '^':
                    splits += 1
                    set_char(r+1, c-1, '|')
                    set_char(r+1, c+1, '|')
                        
    for r in range(0,rows):
        print(data[r])
    print(splits)