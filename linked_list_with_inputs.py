class Node:
    def __init__(self, data):
        # مقداردهی اولیه یک گره
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # ایجاد یک لیست پیوندی خالی
        self.head = None

    def add_to_front(self, data):
        # افزودن گره‌ای به ابتدای لیست
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        # حذف گره‌ای با مقدار مشخص از لیست
        current = self.head
        prev = None

        # بررسی اینکه گره اول لیست همان گره موردنظر است
        if current and current.data == key:
            self.head = current.next
            print(f"گره با مقدار {key} حذف شد.")
            return

        # جستجوی گره در لیست
        while current and current.data != key:
            prev = current
            current = current.next

        # اگر گره پیدا نشود
        if not current:
            print(f"گره با مقدار {key} پیدا نشد.")
            return

        # حذف گره
        prev.next = current.next
        print(f"گره با مقدار {key} حذف شد.")

    def display(self):
        # نمایش تمام گره‌های لیست
        current = self.head
        if not current:
            print("لیست خالی است.")
            return

        print("لیست پیوندی:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        # جستجوی یک مقدار در لیست
        current = self.head
        while current:
            if current.data == key:
                print(f"گره با مقدار {key} پیدا شد.")
                return
            current = current.next
        print(f"گره با مقدار {key} پیدا نشد.")

# برنامه اصلی برای تعامل با کاربر
if __name__ == "__main__":
    ll = LinkedList()

    # گرفتن مقادیر اولیه از کاربر
    initial_values = input("مقادیر اولیه لیست را وارد کنید (با کاما جدا کنید): ").split(",")
    for value in initial_values:
        ll.add_to_front(value.strip())

    while True:
        print("\nمنو:")
        print("1. افزودن یک گره به ابتدای لیست")
        print("2. حذف یک گره از لیست")
        print("3. نمایش لیست پیوندی")
        print("4. جستجو برای یک گره در لیست")
        print("5. خروج")

        choice = input("لطفاً یک گزینه انتخاب کنید: ")

        if choice == "1":
            data = input("لطفاً مقدار گره را وارد کنید: ")
            ll.add_to_front(data)
        elif choice == "2":
            key = input("لطفاً مقدار گره‌ای که می‌خواهید حذف کنید را وارد کنید: ")
            ll.delete_node(key)
        elif choice == "3":
            ll.display()
        elif choice == "4":
            key = input("لطفاً مقدار گره‌ای که می‌خواهید جستجو کنید را وارد کنید: ")
            ll.search(key)
        elif choice == "5":
            print("خروج از برنامه.")
            break
        else:
            print("گزینه نامعتبر است. لطفاً دوباره تلاش کنید.")