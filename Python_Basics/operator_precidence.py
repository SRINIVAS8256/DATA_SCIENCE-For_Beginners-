#python follows PEMDAS  (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction). The order of operations in Python is:
#1  Parentheses () – Highest precedence, operations inside parentheses are evaluated first.
#2 Exponents ** – Power calculations (e.g., 2 ** 3 → 8).
#3 Multiplication *, Division /, Floor Division //, Modulus % – Evaluated from left to right.
#4 Addition +, Subtraction - – Evaluated from left to right.
result = 10 + 2 * 3  # Multiplication happens first: 10 + (2 * 3) = 16
print(result)

result = (10 + 2) * 3  # Parentheses first: (10 + 2) * 3 = 36
print(result)

result = 2 ** 3 ** 2  # Right-to-left exponentiation: 2 ** (3 ** 2) = 2 ** 9 = 512
print(result)