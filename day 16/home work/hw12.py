correct_pin = "1234"
user_pin = ""
attempts = 0

while user_pin != correct_pin:
    user_pin = input("შეიყვანეთ PIN კოდი: ")
    attempts += 1
    if user_pin != correct_pin:
        print("არასწორი PIN კოდი")

print("ავტორიზაცია წარმატებით გაიარე {attempts}")
