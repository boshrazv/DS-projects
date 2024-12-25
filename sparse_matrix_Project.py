def sparse_matrix_addition(mat1, mat2):
    # جمع دو ماتریس اسپارس که به صورت دیکشنری نمایش داده شده اند
    result = mat1.copy()  # ایجاد یک کپی از ماتریس اول
    for key, value in mat2.items():  # مرور بر روی کلیدها و مقادیر ماتریس دوم
        result[key] = result.get(key, 0) + value  # جمع مقادیر و ذخیره در نتیجه
    return {k: v for k, v in result.items() if v != 0}  # حذف مقادیر صفر از نتیجه

def sparse_matrix_transpose(mat):
    # ترانهاده یک ماتریس اسپارس که به صورت دیکشنری نمایش داده شده است
    transposed = {}  # دیکشنری جدید برای ترانهاده
    for (row, col), value in mat.items():
        transposed[(col, row)] = value  # جابجایی ردیف و ستون
    return transposed

def sparse_matrix_multiplication(mat1, mat2):
    # ضرب دو ماتریس اسپارس که به صورت دیکشنری نمایش داده شده اند
    from collections import defaultdict

    mat2_t = sparse_matrix_transpose(mat2)  # ترانهاده ماتریس دوم
    result = defaultdict(int)  # استفاده از defaultdict برای مدیریت مقادیر پیش فرض صفر

    for (row1, col1), value1 in mat1.items():
        for (col2, row2), value2 in mat2_t.items():
            if col1 == row2:  # بررسی سازگاری برای ضرب
                result[(row1, col2)] += value1 * value2  # انجام ضرب و جمع مقادیر

    return dict(result)  # تبدیل به دیکشنری معمولی

def print_sparse_matrix(mat, rows, cols):
    # چاپ ماتریس اسپارس به صورت ماتریس متراکم برای نمایش بهتر
    dense = [[0 for _ in range(cols)] for _ in range(rows)]  # ایجاد ماتریس متراکم با صفرها
    for (row, col), value in mat.items():
        dense[row][col] = value  # قرار دادن مقادیر در مکان مناسب
    for row in dense:
        print(" ".join(map(str, row)))  # چاپ هر ردیف به صورت مرتب