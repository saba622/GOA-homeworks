words = ["ვაშლი", "მსხალი", "ბანანი", "საზამთრო", "ატამი", "კივი", "ანანასი"]

# სიას შემოვაბრუნებთ slicing-ით
reversed_words = words[::-1]

# ცვლადი რომელიც ითვლის ინდექსს
index = 0

# გავდივართ შებრუნებულ სიაზე
for word in reversed_words:
    if index % 2 == 0:  # თუ ინდექსი ლუწია
        print(word)
    index += 1