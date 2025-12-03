dialValue = 50
numberOfTimesDialIsZero = 0

def adjust_dial(value):
    global dialValue
    for _ in range(abs(value)):
        if value > 0:
            dialValue += 1
        else:
            dialValue -= 1

        if dialValue < 0:
            dialValue += 100
        elif dialValue >= 100:
            dialValue -= 100

        if dialValue == 0:
            global numberOfTimesDialIsZero
            numberOfTimesDialIsZero += 1
            print(f"Dial hit zero! Count: {numberOfTimesDialIsZero}")

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

    print(f"Dial hit zero a total of {numberOfTimesDialIsZero} times.")
    print(f"Final dial value: {dialValue}")

