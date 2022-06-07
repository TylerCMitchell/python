# 1
def number_of_food_groups():
    return 5


print(number_of_food_groups())

"""
1.Prediction: 5
Result: 5
"""

# 2


def number_of_military_branches():
    return 5


print(number_of_days_in_a_week_silicon_or_triangle_sides() +
      number_of_military_branches())

"""
2.Prediction: Nothing will happen, or an error as 'number_of_days_in_a_week_silicon_or_triangle_sides()' is not defined.
Result: As predicted
"""

# 3


def number_of_books_on_hold():
    return 5
    return 10


print(number_of_books_on_hold())

"""
3.Prediction: 15
Result: It returned 5. The value '5' is the first to be returned and therefore, the only one recognized. 
"""

# 4


def number_of_fingers():
    return 5
    print(10)


print(number_of_fingers())

"""
4.Prediction: 10, 5
Result: 5 was returned. 'print(10)' is not printing a defined variable, or it is out of order.  
"""

# 5


def number_of_great_lakes():
    print(5)


x = number_of_great_lakes()
print(x)

"""
5.Prediction: 5
Result: 5. 'x' is defined as the new value title for 'number_of_great_lakes().
"""

# 6


def add(b, c):
    print(b+c)


print(add(1, 2) + add(2, 3))

"""
6.Prediction: 8
Result: An error
"""

# 7


def concatenate(b, c):
    return str(b)+str(c)
    print(concatenate(2, 5))


"""
7.Prediction: 7
Result: 7. since it is concatenating the two strings, they add together.
"""

# 8


def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7


print(number_of_oceans_or_fingers_or_continents())

"""
8.Prediction: 100
Result: 100. 100 is not less than '10', so it returns the original value and skips the rest of the loop.
"""

# 9


def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) +
      number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))

"""
9.Prediction: 7, 14, 21
Result: As predicted. The final return is skipped. 
"""

# 10


def addition(b, c):
    return b+c
    return 10


print(addition(3, 5))

"""
10.Prediction: 8
Result: As predicted. The final return is not recognized. 
"""

# 11
b = 500
print(b)


def foobar():
    b = 300
    print(b)


print(b)
foobar()
print(b)

"""
11.Prediction: 500, 500, 300, 500
Result: As predicted. The second 'b' is defined within a def and only applies to when that fuction('fubar()') is called.
"""

# 12
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
foobar()
print(b)

"""
12.Prediction: Same as previous.
Result: Same as previous. 'return b' still only applies to the 'foobar()' function.
"""

# 13
b = 500
print(b)


def foobar():
    b = 300
    print(b)
    return b


print(b)
b = foobar()
print(b)

"""
13.Prediction: 500, 500, 300, 300
Result: As predicted. Since 'b' is defined as 'foobar()' (which is value 300), the final result is '300' as well.
"""

# 14


def foo():
    print(1)
    bar()
    print(2)


def bar():
    print(3)


foo()

"""
14.Prediction: 1, 3, 2
Result: As predicted. 'foo()' is changed to '2' and therefore prints '2' at the end of the function and after 3. 
"""

# 15


def foo():
    print(1)
    x = bar()
    print(x)
    return 10


def bar():
    print(3)
    return 5


y = foo()
print(y)

"""
15.Prediction: 1, 3, 5, 10
Result: As predicted. The function skips over 10 until it is returned as 'y' which had been changed from 'foo()'.
"""
