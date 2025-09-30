import random

randomNum: int = random.randint(1, 20)
count: int = 0

while True:
    try:
        userNum: int = int(input("Guess Number between 1 to 20: "))
    except ValueError:
        print("Please enter a valid number")
        continue

    count += 1
    if randomNum == userNum:
        print("✅ Horray! You Guess it correctly in ", count, " tries")
        break
    else:
        if randomNum > userNum:
            print("Try Bigger Number")
        else:
            print("Try Lower Number")
        continue
