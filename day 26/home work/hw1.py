basket = ["ვაშლი", "მსხალი", "ბანანი", "ფორთოხალი", "ატამი"]

favorite_fruit = input("შეიყვანეთ თქვენი საყვარელი ხილი: ")

fruit_in_basket = False

for fruit in basket:
    if fruit == favorite_fruit:
        fruit_in_basket = True
        break

if fruit_in_basket:
    print("Good choice")
else:
    print("Fruit not in basket")