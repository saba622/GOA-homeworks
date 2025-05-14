full_name = "saba samshvili"

result = ""

uppercase_chars = [char for char in full_name if char.isupper()]

for char in full_name:
    if char.isupper():
        if uppercase_chars.count(char) >= 4:
            result += char.lower()


print(result)