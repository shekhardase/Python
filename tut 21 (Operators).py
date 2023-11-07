""" OPERATORS IN PYTHON:-
1. arithemetic operator
2. assigment operators
3. comparison operators
4. logical operators
5. identity operators
6. membership operators
7. bitwise operators"""

# Arithmetic operators  ( helps in numeric calculations):-

print("5 + 6 is", 5 + 6)
print("5 - 6 is", 5 - 6)
print("5 / 6 is", 5 / 6)
print("5 * 6 is", 5 * 6)
print("5 // 6 is", 5 // 6)  # It is float division operator which gives integer of division
print("5 ** 6 is", 5 ** 6)  # It is exponential operator 5 to power 6   (modulus operator)
print("5 % 6 is", 5 % 6)  # divides then gives remainder     (modulus operator)

# Assigment operator:-
print("assigment operator")
x = 5
print(x)
x += 7  # Here += is assigment operator which adds value 7 in x=5
print(x)
x /= 7  # Similarly /= is also assigment operator which divides
print(x)  # SEARCH MORE ASSIGMENT OPERATORS

# Comparison Operators:-
i = 8
print(i == 5)  # This operator gives true or false value as shown in example

# Logical Operator:-
a = True  # Learn bolean python table
b = False
print(a and b)
print(a or b)
"""(1)Logical AND operator
Logical operator returns True if both the operands are True else it returns False.
   (2)Logical or operator
Logical or operator returns True if either of the operands is True.
   (3)Logical not operator
Logical not operator work with the single boolean value. If the boolean value is True it returns False and vice-versa."""

#Identity Operators :-                ( is , is not)
print(a is not b)
print(a is b)
print(0 != 6)

# Membership Operators:-
List = [3, 4, 5, 8, 9, 12, 46, 89]
print(324 not in List)
print(342 in List)

# Bitwise Operator:-   (ignore not so deeep)
