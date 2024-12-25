class Node:
    def __init__(self, data):
        """ابتدا نود جدید با داده‌ای که وارد می‌شود، ساخته می‌شود."""
        self.data = data
        self.next = None  # نود بعدی به‌صورت پیش‌فرض None است

class Stack:
    def __init__(self):
        """پشته را ایجاد می‌کنیم که در ابتدا خالی است."""
        self.top = None  # بالای پشته به‌صورت اولیه خالی است

    def is_empty(self):
        """بررسی می‌کند که آیا پشته خالی است یا خیر."""
        return self.top is None

    def push(self, data):
        """داده جدید را به بالای پشته اضافه می‌کند."""
        new_node = Node(data)  # نود جدید ایجاد می‌شود
        new_node.next = self.top  # نود جدید به نود قبلی اشاره می‌کند
        self.top = new_node  # بالای پشته به نود جدید تغییر می‌کند

    def pop(self):
        """نود بالای پشته را حذف کرده و داده آن را برمی‌گرداند."""
        if self.is_empty():
            print("پشته خالی است!")
            return None
        popped_node = self.top
        self.top = self.top.next  # بالای پشته به نود بعدی تغییر می‌کند
        return popped_node.data

    def peek(self):
        """داده نود بالای پشته را بدون حذف آن برمی‌گرداند."""
        if self.is_empty():
            print("پشته خالی است!")
            return None
        return self.top.data

    def display(self):
        """نمایش داده‌های پشته."""
        if self.is_empty():
            print("پشته خالی است!")
            return
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ایجاد پشته
stack = Stack()

# گرفتن تعداد عناصر از کاربر
try:
    num_elements = int(input("چند عنصر می‌خواهید به پشته اضافه کنید؟ "))
    if num_elements <= 0:
        raise ValueError("تعداد باید مثبت باشد.")
except ValueError as e:
    print(f"خطا: {e}")
    num_elements = 0

# گرفتن داده‌ها از کاربر و اضافه کردن به پشته
for i in range(num_elements):
    data = input(f"لطفاً داده {i + 1} را وارد کنید: ")
    try:
        data = int(data)
    except ValueError:
        print(f"داده {data} عدد نیست. به‌عنوان رشته ذخیره می‌شود.")
    stack.push(data)

# نمایش محتویات پشته پس از وارد کردن داده‌ها
print("\nلیست شما این است:")
stack.display()

# منوی عملیات پشته
while True:
    print("\nمنوی پشته:")
    print("1. اضافه کردن عنصر به پشته (Push)")
    print("2. حذف بالاترین عنصر از پشته (Pop)")
    print("3. مشاهده بالای پشته (Peek)")
    print("4. نمایش محتویات پشته (Display)")
    print("5. پایان دادن به برنامه")
    
    choice = input("لطفاً یک گزینه وارد کنید (1-5): ")

    if choice == "1":
        data = input("لطفاً داده‌ای که می‌خواهید اضافه کنید را وارد کنید: ")
        try:
            data = int(data)
        except ValueError:
            print("لطفاً عدد معتبر وارد کنید.")
            continue
        stack.push(data)
        print(f"{data} به پشته اضافه شد.")
        stack.display()

    elif choice == "2":
        popped = stack.pop()
        if popped is not None:
            print(f"{popped} از پشته حذف شد.")
        stack.display()

    elif choice == "3":
        peeked = stack.peek()
        if peeked is not None:
            print(f"داده بالای پشته: {peeked}")

    elif choice == "4":
        print("محتویات پشته:")
        stack.display()

    elif choice == "5":
        print("برنامه خاتمه یافت.")
        break

    else:
        print("گزینه نامعتبر است. لطفاً یک عدد بین 1 تا 5 وارد کنید.")