class MyClass:
    def my_method(self, arg1):
        print("Method dengan satu argumen:", arg1)

    def my_method(self, arg1, arg2):
        print("Method dengan dua argumen:", arg1, arg2)

obj = MyClass()
obj.my_method("Hello")  # Error, karena hanya method dengan dua argumen yang didefinisikan
obj.my_method("Hello", "World")  # OK
