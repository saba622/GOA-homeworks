colors = ["წითელი", "მწვანე", "ლურჯი", "ყვითელი", "იასამნისფერი"]

index = int(input("შეიყვანეთ ინდექსი: "))

if 0 <= index <= 4:
    print(colors[index])
else:
    print("მცდარი ინდექსი!")