count = 1
while count <= 5:
	print (count)
	count += 1


while True:
	name = input("Enter the name [type q to quit]")
	if name == "q":
		break
	print(name.capitalize())


while True:
	value = input ("Integer, please [q to quit]: ")
	if value == "q":
		break
	number = int(value)
	if number % 2 == 0: 
		continue
	print (number, "squared is", number*number)

length = 10
count = 0
while count < length:
	print (count)
	count += 1

name="Chidhambaram"
for letter in name:
	print (letter)


for x in range(0,3):
	print(x)


for x in range(0,100,3):
	print(x)
