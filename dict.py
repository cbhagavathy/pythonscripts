
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}

for key in signals.keys():
	print (key)

for value in signals.values():
	print (value)

print ( list (signals.values()) )

print ( list (signals.items()))

print ( len(signals))

colors = { 'G':'Green', 'B':'Blue', 'R':'Red', 'W':'White' }

print (colors)

colors['Y']='Yellow'
print (colors)

#Get an item by key
print ( colors ['G'] )

print ( 'Y' in colors )

print (colors.get('G'))


#Print all keys
print ( colors.keys() )

#Print all values
print ( colors.values() )

print ( list (colors.keys()))
print ( list (colors.values()))

#get length
print (len (colors))

part1 = { 'a':'apple', 'b':'ball' }
part2 = { 'c':'cat', 'd':'dog' }

print ( {**part1, **part2} )

part = {**part1, **part2}

del part['d']

print ( part )


a_set = { number for number in range (1,100) if number % 2 == 0}

print (a_set)
