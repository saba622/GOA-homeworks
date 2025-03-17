#2) შექმენით 5 ცვლადი რომლებშიც შეინახავთ წიგნების თავდაპირველ ფასს, შემდეგ შექმენით ცვლადი რომელშიც შეინახავთ ფასდაკლების ოდენობას, შექმენით ახალი ფასის მქონე წიგნების ცვლადები, რომელთა მნიშვნელობა იქნება ძველ მნიშვნელობას გამოკლებული ახალი, საბოლოოდ კი დაბეჭდეთ ახალი წიგნების ფასები (გამოიყენეთ კარგი მიდგომები: რომ ცვლადის მნიშვნელობის მინიჭებისას შეგიძლიათ სხვა ცვლადის გამოყენება, კოდი ახსენით კომენტარების საშვალებით, ცვლადებს დაარქვით აღმწერი სახელები snake_case-ის სტილში)


book_1_price = 30.00
book_2_price = 25.00
book_3_price = 40.00
book_4_price = 20.00
book_5_price = 15.00

discount_percentage = 0.20


book_1_new_price = book_1_price (book_1_price - discount_percentage)
book_2_new_price = book_2_price (book_2_price - discount_percentage)
book_3_new_price = book_3_price (book_3_price - discount_percentage)
book_4_new_price = book_4_price (book_4_price - discount_percentage)
book_5_new_price = book_5_price (book_5_price - discount_percentage)


print("book_1_new_price")
print("book_2_new_price")
print("book_3_new_price")
print("book_4_new_price")
print("book_5_new_price")