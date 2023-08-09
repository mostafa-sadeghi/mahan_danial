# for i in range(5):
#     print("hello")

# print("blalallal")


# for i in range(3):
#     print(i)

# for i in range(1,5):
#     print(i)
# for i in range(4,5):
#     print(i)


# for number in range(1, 11, 2):
#     print(number)

# عددهای زوج


# for i in range(10, 0, -1):
#     print(i)

# for i in range(10, -1, -1):
#     print(i)


# TODO
"""
برنامه ای بنویسید که با کمک حلقه فور چهار اسم از ورودی دریافت نماید و در لیستی ذخیره نماید

تمرین 2:
برنامه ای بنویسید که با کمک حلقه فور، پنج عدد از ورودی دریافت نماید و با هم جمع کند

تمرین 3
برنامه ای بنویسید که پنج عدد از ورودی دریافت نماید و جمع اعداد زوج موجود را محاشبه نماید
عدد زوج عددی است که باقیمانده تقسیم آن بر دو مساوی صفر است
باقیمانده را با کمک % می توان محاسبه نمود
"""


# names = []
# for i in range(4):
#     new_name = input("enter a name: ")
#     names.append(new_name)

# print(names)


# total = 0
# for i in range(5):
#     new_number = int(input("enter a number: "))
#     total += new_number # total = total + new_number

# print("total is:",total)

total = 0
for i in range(5):
    new_number = int(input("enter a number: "))
    if new_number % 2 == 0:
        total += new_number # total = total + new_number

print("total is:",total)