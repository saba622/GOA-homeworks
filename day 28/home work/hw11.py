text = "Python programming is fun and powerful"

word = input("შეიყვანეთ საძიებელი სიტყვა: ")

pos = text.find(word)

if pos != -1:
    print(f"სიტყვა '{word}' მდებარეობს პოზიციაზე: {pos}")
else:
    print("word not found")