#Method overriding


# class person:
#     def Quality(self):
#         return "chill maro yaar"

# class Sita(person):
#     def Quality(self):
#         return "I am the innocent angel "
    

# class Ram(person):
#     def Quality(self):
#         return "I am more pure in my belief"


# p = person()
# print(p.Quality())  
# r = Ram()
# print(r.Quality())

# s = Sita()
# print(s.Quality())


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the addition operator (+)
    def __add__(self, other):                               # we are currently overriding the builtin add function to make it multipy 
        return Vector(self.x * other.x, self.y * other.y)

    # Overloading the string representation method
    def __str__(self):
        return f"({self.x}, {self.y})"

# Creating instances of the Vector class
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Adding two Vector objects using the overloaded addition operator
result = v1 + v2
print(result)  # Output: (8 , 15)


# Addition (+): Implement __add__(self, other)
# Subtraction (-): Implement __sub__(self, other)
# Multiplication (*): Implement __mul__(self, other)
# Division (/): Implement __truediv__(self, other) (for true division) or __floordiv__(self, other) (for floor division)
# Modulus (%): Implement __mod__(self, other)
# Exponentiation (**): Implement __pow__(self, other)
# Comparison operators:
# Equal to (==): Implement __eq__(self, other)
# Not equal to (!=): Implement __ne__(self, other)
# Less than (<): Implement __lt__(self, other)
# Greater than (>): Implement __gt__(self, other)
# Less than or equal to (<=): Implement __le__(self, other)
# Greater than or equal to (>=): Implement __ge__(self, other)
