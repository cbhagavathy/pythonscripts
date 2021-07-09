poem='''There was a Young Lady
		very nice lady, good lady
		very kdy'''

print (poem)


data="""'testing the string
is a great stuff to go with
i love this"""

print (data)


palindrome="A man, \nA plan, \nA canal"

print (palindrome)


hi="hi"

print (hi*3)

letters = 'abcdefghijklmnopqrstuvwxyz'


print (letters[:])
print (letters[10:])
print (letters[:10])
print (letters[-3:])
print (letters[18:])
print (letters[18:-3])

alphabets="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"

print (alphabets.split(','))

print (alphabets.split(',')[23])


title="Welcome to Jurassic Park"

print ("+", title.center(50), "+")
print ("+",title.ljust(50),"+")
print ("+",title.rjust(50),"+")


name="chidhambara"
age=38

print ( "My name is %s and age is %d" % (name, age))

print ( "Heading : %s" % (title))
print ( "Heading : %50s" % (title))
print ( "Heading : %-50s" % (title))
print ( "Heading : %.3s" % (title))
print ( "Heading : %12.3s" % (title))
print ( "Heading : %-12.3s" % (title))


number=12345.123

print ( "%d" % number)
print ( "%12d" % number)
print ( "%+12d" % number)

print ( "{}".format(name))
print ( "My name is {}".format(name))
print ( "My name is {} and age is {}".format(name, age))

fname="Chidhambaram"
lname="Bhagavathy"
print ( "My first name is {0} and last name is {1}".format(fname, lname))
print ( "My first name is {1} and last name is {0}".format(fname, lname))


print ( "My first name is {f} and last name is {l}".format(f=fname, l=lname))

name = {'fname':'chidhambaram', 'lname':'bhagavathy'}

print ( "My first name is {0[fname]} and last name is {0[lname]}".format(name))

thing = 'wraith'
place = 'window'

print ('The {:10s} is at the {:10s}'.format(thing, place))
print ('The {:<10s} is at the {:<10s}'.format(thing, place))
print ('The {:^10s} is at the {:^10s}'.format(thing, place))
print ('The {:>10s} is at the {:>10s}'.format(thing, place))
print ('The {:*^10s} is at the {:!^10s}'.format(thing, place))

thing = 'wereduck'
place = 'werepond'

print (f'The {thing} is in the {place}')
print (f'The {thing.capitalize()} is in the {place.rjust(20)}')
print (f'The {thing:>20} is in the {place:.^20}')
print (f'{thing =}, {place =}')
print (f'{thing[-4:] =}, {place.title() =}')
print (f'{thing = :>4.4}')
