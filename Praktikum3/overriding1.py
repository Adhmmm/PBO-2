class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

animal = Animal()
animal.speak()  # Output: The animal makes a sound

dog = Dog()
dog.speak()  # Output: The dog barks

cat = Cat()
cat.speak()  # Output: The cat meows
