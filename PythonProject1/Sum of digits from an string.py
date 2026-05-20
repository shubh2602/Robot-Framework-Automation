def Sum_of_digits_from_and_string(s):
     total = 0
     for char in s:
          if char.isdigit():
              total += int(char) 
     return total

print(Sum_of_digits_from_and_string("abc123def"))

