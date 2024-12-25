import numpy as np

def multiply_arrays(array1, array2):
    # بررسی طول آرایه ها
    if len(array1) != len(array2):
        print("خطا: طول آرایه ها برابر نیست")
        return

    # ضرب عنصر به عنصر آرایه ها
    result = np.multiply(array1, array2)

    # نمایش آرایه ها
    #'[' + ... + ']'
    #", ".join(str(x) for x in result)
    #استفاده از دو مورد بالا برای تبدیل آرایه به رشته و گذاشتن آنها در کروشه و جداسازی توسط کاما
    print("First array:", array1)
    print("Second array:", array2)
    print("Result:", "[" + ", ".join(str(x) for x in result) + "]")

# آرایه های ورودی
array1 = [1, 2, 3, 4, 5]
array2 = [6, 7, 8, 9, 10]

# فراخوانی تابع
multiply_arrays(array1, array2)