number = int(input("შეიყვანეთ მთელი რიცხვი: "))

if number > 0:
    print("რიცხვი დადებითია.")
    
    if number % 2 == 0:
        print("რიცხვი ლუწია.")
    else:
        print("რიცხვი კენტია.")
else:
    print("რიცხვი უარყოფითია ან ნულია.")