
def sum_elements(limit):
    acum = 0
    for i in range(limit):
        if good(i):
            acum = acum + i
    return acum


def good(i):
    if i == 0:
        return False
    by_3 = (i % 3) == 0
    by_5 = (i % 5) == 0
    return by_3 or by_5


def even_elements_mult(i,b):
    if i ==0:
        return False
    for num in range (i,b):
        for i in range (1,num):
            if num % i == 0:
                result = i*b
        return result


# Task2:
# for all numbers below 10 (excluding 0)
# result of multiplication of all even numbers is 384=2*4*6*8
# calculate the multiplication result of all even numbers below 100000


# Task 3:
# how to change sum_elements with list comprehension and map function