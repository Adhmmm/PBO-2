class Animal:
    def make_sound(self):
        return 'The animal makes a sound'

class Dog:
    def make_sound(self):
        return 'The dog barks'

class Cat:
    def make_sound(self):
        return 'The cat meows'

class Chihuahua:
    def make_sound(self):
        return 'The chihuahua yaps'

class Siamese:
    def make_sound(self):
        return 'The siamese purrs'
    
obj_animal = Animal()
obj_dog = Dog()
obj_cat = Cat()
obj_chihuahua = Chihuahua()
obj_siamese = Siamese()

for obj in [obj_animal, obj_dog, obj_cat, obj_chihuahua, obj_siamese]:
    print(obj.make_sound())

    def animal_sound(animal):
        animal.make_sound()

# Instantiate objects of each class
animal= Animal()
dog = Dog()
cat = Cat()
chihuahua = Chihuahua()
siamese = Siamese()

# Call the animal sound function for each object
animal_sound(animal)        # Output: The animal makes a sound
animal_sound(animal)        # Output: The dog barks
animal_sound(animal)        # Output: The cat meows
animal_sound(animal)        # Output: The chihuahua yaps
animal_sound(animal)        # Output: The siamese purrs
