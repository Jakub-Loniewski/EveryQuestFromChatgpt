import random

number = random.randint(1,100)

attempt = 0

while True:
    attempt = int(input("Put number betwen 1 and 100"))
    attempt += 1

    if attempt < number:
        print("to little")
    elif attempt > number:
        print("Too much")
    else:
        print(f"Good you guessed {attempt}")
        break