class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            print("Method dengan satu argumen:", args[0])
        elif len(args) == 2:
            print("Method dengan dua argumen:", args[0], args[1])

obj = MyClass()
obj.my_method("Hello")  # OK
obj.my_method("Hello", "World")  # OK
