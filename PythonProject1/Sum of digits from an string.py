def Sum_of_digits_from_and_string(str):
     total = 0
     for char in str:
          if char.isdigit():
              total += int(char) 
     return total

print(Sum_of_digits_from_and_string("abc123def"))

