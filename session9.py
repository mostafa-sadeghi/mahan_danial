# def isOdd(number):
#     if number % 2 != 0:
#         return f"{number} is odd"

# n = int(input("Enter a number: "))
# print(isOdd(n))


# def area(width, length):
#     return f"area is {width * length}"

# print(area(4,2))
# print(area(4,8))


# def fizzbuzz(number):
#     if number % 3 == 0 and number % 5 == 0:
#         return "fizzbuzz"
#     elif number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     else:
#         return number


# print(fizzbuzz(15))
# print(fizzbuzz(5))
# print(fizzbuzz(3))
# print(fizzbuzz(30))


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


# def my_function(number):
#     # if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
#     if number % 100 in (11, 12, 13):
#         return str(number) + "th"
#     elif number % 10 == 1:
#         return str(number) + "st"
#     elif number % 10 == 2:
#         return str(number) + "nd"
#     elif number % 10 == 3:
#         return str(number) + "rd"
#     else:
#         return str(number) + "th"


# print(my_function(101))
# print(my_function(102))
# print(my_function(11))
# print(my_function(12))


# print(ord('p'))
# print(ord('y'))

# print(chr(10001))
# print(chr(101))
# print(chr(1000001))

"""تابعی بنویسید که یک عبارت را از ورودی دریافت نماید و معادل یونیکد هر یک از 
حروف آن را نمایش دهد"""

# def to_unicode(text):
#     # for t in text:
#     #     print(ord(t))
#     for i in range(len(text)):
#         print(ord(text[i]))

# to_unicode("python")

# TODO
"""
[18,101,300,24,76,88,92]
chr()
تابعی بنویسید که لیست بالا را بگیرد و معادل کاراکتر ی هر یک از اعداد موجود در لیست را نمایش دهد
با حلقه فور
"""
print(chr(18))
