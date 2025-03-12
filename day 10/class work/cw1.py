
height = float(input("შეიყვანეთ თქვენი სიმაღლე (მეტრებში): "))
years = int(input("შეიყვანეთ წლების რაოდენობა: "))

estimated_height = height + (years * 0.5)

print("როდესაც " + str(years) + " წელი გავა, თქვენი სავარაუდო სიმაღლე იქნება: " + str(estimated_height) + " მეტრი.")
