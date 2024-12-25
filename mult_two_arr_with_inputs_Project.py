import numpy as np

def multiply_arrays(array1, array2):
    # بررسی طول آرایه ها
    if len(array1) != len(array2):
        print("خطا: طول آرایه ها برابر نیست")
        return

    # ضرب عنصر به عنصر آرایه ها
    result = np.multiply(array1, array2)

    # نمایش آرایه ها و نتیجه
    print("First array:", "[" + ", ".join(map(str, array1)) + "]")
    print("Second array:", "[" + ", ".join(map(str, array2)) + "]")
    print("Result:", "[" + ", ".join(map(str, result)) + "]")

# گرفتن آرایه ها از کاربر
try:
    array1 = list(map(int, input("Enter the first array (comma-separated): ").split(',')))
    array2 = list(map(int, input("Enter the second array (comma-separated): ").split(',')))

    # فراخوانی تابع
    multiply_arrays(array1, array2)
except ValueError:
    print("خطا: لطفاً فقط اعداد صحیح وارد کنید.")