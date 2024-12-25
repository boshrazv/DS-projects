def infix_to_postfix(expression):
    # تعریف اولویت عملگرها
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    # استک برای نگهداری عملگرها
    stack = []

    # لیست برای نگهداری خروجی
    output = []

    # پردازش هر کاراکتر در عبارت
    for char in expression:
        if char.isalnum():  # اگر کاراکتر یک عدد یا حرف است
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())  # انتقال عملگرها به خروجی تا رسیدن به (
            stack.pop()  # حذف پرانتز باز
        else:  # اگر کاراکتر یک عملگر است
            while stack and precedence[stack[-1]] >= precedence[char]:
                output.append(stack.pop())  # انتقال عملگر با اولویت بالاتر یا مساوی به خروجی
            stack.append(char)

    # انتقال باقی عملگرها از استک به خروجی
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# دریافت عبارت میانوندی از کاربر
expression = input("Enter an infix expression: ")
print("Postfix Expression:", infix_to_postfix(expression))