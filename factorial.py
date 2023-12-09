"""
    Question 2: Write a Python program to find the factorial of a number.
"""


nb = int(input("Entrer number : "))

factor = nb

if (factor == 0):
    factor = 1
else:
    for i in range(1, nb):
        factor = factor * i
    
print(factor)