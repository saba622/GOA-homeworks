def manual_max(lst):
    if not lst:
        raise ValueError("სია ცარიელია")
    max_value = lst[0]
    for item in lst[1:]:
        if item > max_value:
            max_value = item
    return max_value

def manual_len(sequence):
    count = 0
    for _ in sequence:
        count += 1
    return count

numbers = [3, 7, 2, 9, 4]

print("manual_max:", manual_max(numbers))
print("manual_len:", manual_len(numbers))