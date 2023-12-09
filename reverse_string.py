"""
    
    Question 4: Write a Python program to reverse a string.
    Or simply : print(s[::-1])
"""


s = "Zidane"

new_s = s.lower()
new_word = ""

for i in range(0, len(new_s)):
    index = len(new_s) - i - 1
    new_word += new_s[index]

print(new_word)