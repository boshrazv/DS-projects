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
        # افزودن گره ای به ابتدای لیست
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"گره با مقدار {data} به ابتدای لیست اضافه شد.")

    def delete_node(self, key):
        # حذف گره ای با مقدار مشخص از لیست
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
        # نمایش تمام گره ای لیست
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