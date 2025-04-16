positive_sum = 0

while True:
    number = int(input("შეიყვანეთ რიცხვი: "))

    if number < 0:
        break

    if number > 0:
        positive_sum += number

print(positive_sum)