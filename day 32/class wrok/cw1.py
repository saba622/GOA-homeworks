def square_properties(length=10):
    area = length * length
    perimeter = 4 * length
    return area, perimeter

area1, perimeter1 = square_properties(5)

area2, perimeter2 = square_properties()

square_area1 = area1
square_perimeter1 = perimeter1

square_area2 = area2
square_perimeter2 = perimeter2

print("პირველი კვადრატი:")
print("ფართობი:", square_area1)
print("პერიმეტრი:", square_perimeter1)

print("\nმეორე კვადრატი:")
print("ფართობი:", square_area2)
print("პერიმეტრი:", square_perimeter2)