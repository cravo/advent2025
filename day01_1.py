dialValue = 50

def adjust_dial(value):
    global dialValue
    dialValue += value
    while dialValue < 0:
        dialValue += 100

    while dialValue >= 100:
        dialValue -= 100

    return dialValue

rotations = []
                 
if __name__ == "__main__":
    numberOfTimesDialIsZero = 0

    with open("day01.txt", "r") as file:
        rotations = [line.strip() for line in file.readlines()]

    dialValue = 50

    for rotation in rotations:
        direction = rotation[0]
        amount = int(rotation[1:])

        print(f"Current dial value: {dialValue}, rotating {direction}{amount}")

        if direction == "L":
            adjust_dial(-amount)
        elif direction == "R":
            adjust_dial(amount)

        if dialValue == 0:
            numberOfTimesDialIsZero += 1
            print(f"Dial hit zero! Count: {numberOfTimesDialIsZero}")

    print(f"Dial hit zero a total of {numberOfTimesDialIsZero} times.")
    print(f"Final dial value: {dialValue}")

