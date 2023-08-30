# def isOdd(number):
#     if number % 2 != 0:
#         return f"{number} is odd"

# n = int(input("Enter a number: "))
# print(isOdd(n))


# def area(width, length):
#     return f"area is {width * length}"

# print(area(4,2))
# print(area(4,8))


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number


print(fizzbuzz(15))
print(fizzbuzz(5))
print(fizzbuzz(3))
print(fizzbuzz(30))


# TODO

"""
تابعی بنویسید که یک عدد بگیرد و
اگر رقم یکان عدد یک بود
به عدد st 
را بچسباند
1st
101st

اگر رقم یکان آن دو بود
2nd
102nd
"""
