vegetables = ["ბროკოლი", "სტაფილო", "ყაბაყი", "კომბოსტო"]

user_choice = int(input("შეიყვანეთ რიცხვი 0-დან 3-მდე: "))

if 0 <= user_choice < len(vegetables):
    print("აირჩიეთ:", vegetables[user_choice])
else:
    print("არასწორი არჩევანი! გთხოვთ შეიყვანოთ რიცხვი 0-დან 3-მდე.")