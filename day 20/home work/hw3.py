correct_pin = "1234"

attempts = 3

while attempts > 0:
    entered_pin = input("შეიყვანეთ PIN კოდი: ")

    if entered_pin == correct_pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(attempts)
        else:
            print("Access Denied")