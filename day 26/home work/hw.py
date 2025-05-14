start = int(input("შეიყვანეთ დასაწყისი რიცხვი: "))
end = int(input("შეიყვანეთ დასასრული რიცხვი: "))

if end < start:
    print("არასწორი შუალედი.")
else:
    total = 0
    print("რიცხვები შუალედში:")
    for num in range(start, end + 1):
        print(num)
        total += num
    print("რიცხვების ჯამი არის:", total)