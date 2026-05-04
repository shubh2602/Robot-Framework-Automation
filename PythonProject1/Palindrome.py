def palindrome(s):
    rev = ""

    for char in s:
        rev = char + rev

    if rev == s:
        print("it is palindrome")
    else:
        print("it is not a palindrome")

palindrome("12321")