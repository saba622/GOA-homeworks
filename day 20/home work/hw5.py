vowels = "aeiouAEIOU"

vowel_count = 0
consonant_count = 0

sentence = input("შეიყვანეთ წინადადება: ")

for char in sentence:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(vowel_count)
print(consonant_count)