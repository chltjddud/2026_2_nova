text = "racecar"

is_palindrome = True
left = 0
right = len(text) - 1

while left < right:
    if text[left] != text[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(is_palindrome)
