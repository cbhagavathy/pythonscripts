class Cat:
	pass

a_cat = Cat()

a_cat.age = 3

print (a_cat.age)
print (a_cat)


class Animal:
	def __init__(self, name):
		self.name = name

	def make_sound(self):
		print ("Urrrr")

dog = Animal("Tommy")


print (dog.name)

#Inheritance
class Dog(Animal):
	def make_sound(self):
		print ("Bow bow !!!")	

dog = Dog("Jony")

print (dog.name)
dog.make_sound()


#Multiple Inheritance
class Animal:
	def says(self):
		return "I speak!"

class Horse(Animal):
	def says(self):
		return "Neigh!"

class Donkey(Animal):
	def says(self):
		return "Hee-haw!"

class Mule(Donkey, Horse):
	pass

class Hinny(Horse, Donkey):
	pass


mule = Mule()
hinny = Hinny()

print (mule.says())
print (hinny.says())


#properties for attribute access
class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name

	def get_name(self):
		print('inside the getter')
		return self.hidden_name

	def set_name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name

	name = property(get_name, set_name)


don = Duck('Donald')

print(don.get_name())
don.set_name('chidhambaram')
print(don.get_name())

print (' ')
print(don.name)

print (' ')
don.name ='test'


class Duck:
	def __init__(self, input_name):
		self.hidden_name = input_name

	@property
	def name(self):
		print('inside the getter')
		return self.hidden_name

	@name.setter
	def name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name

fowl = Duck('chidhu')

fowl.name


class Circle():
	def __init__(self, radius):
		self.radius = radius

	@property
	def diameter(self):
		return 2 * self.radius


c = Circle(5)

print (c.diameter)

#Name mangling for Privacy

class Duck():
	def __init__(self, input_name):
		self.__name = input_name

	@property
	def name(self):
		print ('inside the getter')
		return self.__name

	@name.setter
	def name(self, input_name):
		print ('inside the setter')
		self.__name = input_name


fowl = Duck('chidhu')

print (fowl.name)
fowl.name = 'malar'
print (fowl.name)


print (fowl._Duck__name)



class A():
	count = 0
	def __init__(self):
		A.count += 1
	def exclaim(self):
		print ("I am A!")

	@classmethod
	def kids(cls):
		print ('A has', cls.count, 'little objects')

a1 = A()
a2 = A()
a3 = A()

A.kids()



class CoyoteWeapon():
	@staticmethod
	def commercial():
		print("This CoyoteWeapon has been brought to you by Acme!")


CoyoteWeapon.commercial()


class Word():
	def __init__(self, text):
		self.text = text

	def equals(self, word2):	
		return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('Ha')


print (first.equals(second))


class Words():
        def __init__(self, text):
                self.text = text

	#def __eq__(self, word2):
		#return self.text.lower() == word2.text.lower()

first = Words('ha')
second = Words('HA')
third = Words('Ha')


print ( first == second )


from collections import namedtuple
Duck = namedtuple("Duck", "bill tail")

duck = Duck("Wide Orange", "long")

print (duck)

print (duck.bill)
print (duck.tail)


from dataclasses import dataclass

@dataclass
class AnimalClass:
	name: str
	habitat: str
	teeth: int = 0

snowman = AnimalClass('yeti', 'Himalayas', 45)


print(snowman)
