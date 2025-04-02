correct_password = "1234"
user_input = " "

while user_input != correct_password:
    user_input = input("შეიყვანეთ პაროლი: ")
    if user_input != correct_password:
        print("არასწორი პაროლი: ")

print("პაროლი სწორია: ")