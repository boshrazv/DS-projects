class Node:
    def __init__(self, data):
        # ایجاد یک گره جدید با داده مشخص
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # در ابتدا درخت خالی است
        self.root = None

    def insert(self, data):
        # اضافه کردن یک گره جدید به درخت
        if self.root is None:
            self.root = Node(data)  # اگر درخت خالی باشد، ریشه را مقداردهی می‌کند
        else:
            current = self.root
            while True:
                if data < current.data:  # اگر داده جدید کمتر از داده گره فعلی است، به سمت چپ می‌رود
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                elif data > current.data:  # اگر داده جدید بیشتر از داده گره فعلی است، به سمت راست می‌رود
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right

    def search(self, data):
        # جستجوی یک مقدار در درخت
        current = self.root
        while current:
            if current.data == data:
                return True  # اگر داده پیدا شد
            elif data < current.data:
                current = current.left  # به سمت چپ می‌رود
            else:
                current = current.right  # به سمت راست می‌رود
        return False  # اگر داده پیدا نشد

    def inorder(self, node):
        # پیمایش inorder درخت (چپ، ریشه، راست)
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        # پیمایش preorder درخت (ریشه، چپ، راست)
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        # پیمایش postorder درخت (چپ، راست، ریشه)
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def delete(self, data):
        # حذف گره از درخت
        self.root = self._delete_recursive(self.root, data)

    def _delete_recursive(self, root, data):
        # تابع بازگشتی برای حذف گره
        if root is None:
            return root

        if data < root.data:
            root.left = self._delete_recursive(root.left, data)  # به سمت چپ می‌رود
        elif data > root.data:
            root.right = self._delete_recursive(root.right, data)  # به سمت راست می‌رود
        else:
            # گره پیدا شد
            if root.left is None:
                return root.right  # اگر گره فقط فرزند راست دارد
            elif root.right is None:
                return root.left  # اگر گره فقط فرزند چپ دارد
            else:
                # گره دارای دو فرزند است
                min_larger_node = self._get_min(root.right)
                root.data = min_larger_node.data  # جایگزین کردن داده گره حذف‌شده با کمترین داده از سمت راست
                root.right = self._delete_recursive(root.right, root.data)
        return root

    def _get_min(self, node):
        # پیدا کردن کمترین گره در درخت
        current = node
        while current.left:
            current = current.left
        return current

    def display(self):
        # نمایش درخت به ترتیب inorder
        if self.root is None:
            print("درخت خالی است.")
        else:
            print("پیمایش Inorder درخت:")
            self.inorder(self.root)
            print()

# برنامه اصلی برای تعامل با کاربر
if __name__ == "__main__":
    tree = BinaryTree()

    # گرفتن داده‌های اولیه از کاربر
    num_nodes = int(input("چند گره می‌خواهید به درخت اضافه کنید؟ "))

    for i in range(num_nodes):
        data = int(input(f"داده گره {i + 1} را وارد کنید: "))
        tree.insert(data)


    while True:
        print("\nمنو:")
        print("1. اضافه کردن یک گره به درخت")
        print("2. جستجوی یک گره در درخت")
        print("3. نمایش درخت به ترتیب Inorder")
        print("4. نمایش درخت به ترتیب Preorder")
        print("5. نمایش درخت به ترتیب Postorder")
        print("6. حذف یک گره از درخت")
        print("7. خروج از برنامه")

        choice = input("یک گزینه را انتخاب کنید: ")

        if choice == "1":
            data = int(input("داده گره جدید را وارد کنید: "))
            tree.insert(data)
        elif choice == "2":
            key = int(input("مقدار گره مورد نظر را برای جستجو وارد کنید: "))
            if tree.search(key):
                print(f"گره با مقدار {key} پیدا شد.")
            else:
                print(f"گره با مقدار {key} پیدا نشد.")
        elif choice == "3":
            tree.display()  # نمایش Inorder
        elif choice == "4":
            print("پیمایش Preorder درخت:")
            tree.preorder(tree.root)
            print()
        elif choice == "5":
            print("پیمایش Postorder درخت:")
            tree.postorder(tree.root)
            print()
        elif choice == "6":
            key = int(input("مقدار گره مورد نظر را برای حذف وارد کنید: "))
            tree.delete(key)
        elif choice == "7":
            print("خروج از برنامه.")
            break
        else:
            print("انتخاب نامعتبر است. لطفاً دوباره تلاش کنید.")