def do_nothing():
	pass

def print_hello():
	print ("Hello")

def print_hello2(name='World'):
	print ("Hello" + " " + name)

def agree():
	return True

do_nothing()
print_hello()


if agree():
	print ("True")
else:
	print ("False")

print_hello2('Chidhambaram')

print_hello2();


def buggy(arg, result=[]):
	result.append(arg)
	print(result)


data=[]
buggy("a", data)
print(data)
buggy("b", data)
print(data)


def works(arg):
	result = []
	result.append(arg)
	return result


data1=works('a')
print (data1)

data1=works('b')
print (data1)


def nonbuggy(arg, result=None):
	if result is None:
		result = []
	result.append(arg)
	print(result)



data3=None
nonbuggy('a', data3)


def print_args(*args):
	print (args)


print_args()

print_args(10,20, "test")

def print_keywords(**kwargs):
	print("Keyword arguments : ", kwargs)


print_keywords()

print_keywords(fname="chidhambaram", lname="bhagavathy")

def print_data(data, *, start=0, end=100):
	for value in (data[start:end]):
		print (value)

data = ['a', 'b', 'c', 'd', 'e', 'f']

print_data(data)
print  ( " ")
print_data(data, end=3)
print  ( " ")
print_data(data, start=2)


#inner functions
def outer(a, b):
	def inner(c, d):
		return c + d
	return inner (a, b)

print (outer (4, 1))



#Closures
def knights(saying):
	def inner2():
		return "We are the knights who say : '%s'" % saying
	return inner2


a = knights("Duck")
b = knights("Hasan")

print (type(a))

print (a())

print (b())


#lambda
def edit_story(words, func):
	for word in words:
		print (func(word))


def enliven(word):
	return word.capitalize() + '!'


colors = ['green', 'blue', 'yellow', 'red']
edit_story(colors, enliven)

print (" ")

edit_story(colors, lambda word: word.capitalize() + '!')


#locals and globals
animal = "fruitbat"
def change_local():
	animal = "wombat"
	print ('locals : ', locals())

print (animal)

print (change_local())

print ('globals : ', globals())

#decorators
def document_it(func):
	def new_function(*args, **kwargs):
		print ("Running function : ", func.__name__)
		print ("Positional arguments : ", args)
		print ("Keyword arguments : ", kwargs)
		result = func(*args, *kwargs)
		print ("Result : ", result)
		return result
	return new_function


def add_ints(a, b):
	return a+b

add_ints(5,3)

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)

def amazing():
	'''This is the function
		definition
		of amazing'''
	print ('This function is named : ', amazing.__name__)
	print ('And its docstring is : ', amazing.__doc__)


amazing()

short_list = [1,2,3]
position = 5

try:
	print (short_list[position])
except Exception as error:
	print ('Error captured :', error)
