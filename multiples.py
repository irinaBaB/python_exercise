import array as arr

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


def even_elements_mult(i):
    if i == 0:
        return False
    for num in i:
        if num % 2 == 0 and num > 0:
            print (num)
        result = num * num
    return result


# Task2:
# for all numbers below 10 (excluding 0)
# result of multiplication of all even numbers is 384=2*4*6*8
# calculate the multiplication result of all even numbers below 100000


# Task 3:
# how to change sum_elements with list comprehension and map function