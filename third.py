# numbers = (1, 2, 3, 4)
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])


# numbers = [1,2,3,4]
# numbers[0] = 12
# print(numbers)
#
# numbers = (1,2,3,4)
# # numbers[0] = 1000 # error
# print(numbers)


sports = {
    'amirali':'football',
    'danial':'football',
    'mahan':'ordou'
}

# print(f"mahan Likes {sports['mahan']}")

name = input("enter a name: ")
sport = input("enter the sport's name: ")
sports[name] = sport
print(sports)


name = input("enter the name for delete: ")
del sports[name]
print(sports)

# TODO
"""
برنامه ای بنویسید که نام و غذای مورد علاقه سه فرد را از ورودی دریافت نماید و دیکشنری ذخیره کند
سپس نام یک فرد را از ورودی بگیرد و غذای مورد علاقه اش را نمایش دهد
فرض کنیم یکی از افراد پشمیان شده باشد و بخواهد غذای مورد علاقه اش را تغییر دهد
باید اسم را از ورودی بگیرد و غذای جدید را هم از ورودی بگیرید و مانند اضافه کردن به دیکشنری عمل کنید
"""