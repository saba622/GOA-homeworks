student = {
    "name": "Saba",        # სტუდენტის სახელი
    "hobby": "reading",    # ჰობი
    "height": 175,         # სიმაღლე
    "weight": 76           # წონა
}

name_value = student.get("name")
print("Name:", name_value)

removed_height = student.pop("height")
print("წაშლილი height:", removed_height)

print("განახლებული student:", student)