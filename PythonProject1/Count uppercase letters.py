text = input("Enter a string: ")
count = 0

for char in text:
    if char.isupper():
        count += 1  # Increase count

print("Number of uppercase letters:", count)