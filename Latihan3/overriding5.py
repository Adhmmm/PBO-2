class Dog:
    def sound(self):
        print("Guk guk!")

class Cat:
    def sound(self):
        print("Meoww")

def make_sound(animal):
    animal.sound

# membuat objek dari class Dof dan Cat
dog = Dog()
cat = Cat()

# memanggil method make_sound pada objek tersebut
dog.sound()
cat.sound()