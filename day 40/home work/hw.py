# მაგალითი 1: გაყოფა სივრცით
text1 = "Hello world from Python"
print(text1.split())  # ['Hello', 'world', 'from', 'Python']

# მაგალითი 2: გაყოფა კომით
text2 = "apple,banana,orange"
print(text2.split(","))  # ['apple', 'banana', 'orange']

# მაგალითი 3: გაყოფა კონკრეტულ სიტყვაზე
text3 = "one and two and three"
print(text3.split(" and "))  # ['one', 'two', 'three']