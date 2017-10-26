count = 0
total = 0
current = 0

while current != 'done':
     try:
         current = raw_input("enter number")
         total = total + float(current)
         count = count + 1
     except:
         if current != 'done':
             print 'invalid input'
print 'Total',total
print 'Count', count
print 'Average', total/count


str1 = 'hello'
str2 = 'bob'
bob = str1 +' '+ str2
print bob
print str1, str2
str3 = '123'
print str3 + str(1)
print str3 + '1'
print int(str3) + 1
print str3,1

#looping through loops

fruit = 'banana'
print len(fruit)
print fruit[0]
print fruit[len(fruit)-1]

#for and while for loop
for index in range(0, len(fruit)):
    print index, fruit[index],
    print ''

index = 0
while index < len(fruit):
    print index, fruit[index],
    index = index + 1
    
fruit = 'banana'
for letter in fruit:
    print letter,

word = 'banana'
count = 0
for letter in word :
    if letter == 'a' :
       count = count + 1
print 'a times:',count

word = 'banana'
count = 0
for letter in word :
    if letter == 'n' :
       count = count + 1
print 'n times:',count

number = [10,5,2,3,10,11,10]
count = 0
for number in number:
    if number == 10 :
       count = count + 1
print '10 times:',countwords


#counting letter in words:

word = raw_input("Enter word: ")
the_letter = raw_input ("Enter letter: ")
count = 0
for letter in word:
    if letter == the_letter:
       count = count + 1
print count


s = 'star wars movies'
print s[0:4] # is reading from 0 including 0, and all below 4
print s[6:7] # goes from 6 up to below 7
print s[6:20] #goes from 6(incl) up to below 20

>>> s = 'Monty Python'
>>> print s[:2] #from the beginning up to below 2
Mo
>>> print s[8:] #from 8 up to the end
thon
>>> print s[:] #all string
Monty Python
>>> print s[::-1] #print all in the string but backwords

fruit = 'banana'
if 'a' in fruit :
print 'found it!'

print 'n' in fruit
print 'm' in fruit
print 'nan' in fruit
print 'app' in fruit

#############################

word = raw_input("Enter word: ")
the_letter = raw_input ("Enter letter: ")
count = 0
for letter in word:
    if letter == the_letter:
       count = count + 1
print count

if word < 'banana':
    print 'your word', + word + ', comes before banana'
elif word > 'banana':
    print 'your word', + word + ', comes after banana'
else:
    print 'All right bananas'

#####################################

greet = 'Hello Bob'
zap = greet.lower()
print zap
print greet
print greet.upper()
print 'Hi There'.lower()

print type (greet)
print dir (greet)
print greet.replace('e','o')

#####################################

balance = '_______123456_____'
print balance.strip('_')
print balance.lstrip('_')
print balance.rstrip('_')

######################################

fruit = 'banana'
pos = fruit.find('na')
print pos
2
z = fruit.find('z')
print z

######################################

greet = 'Hello Bob'
nnn = greet.upper()
print nnn

www = greet.lower()
print www

################################

value = 'all over the tableou'
print value.replace('o','k')

##############################

line = 'Please have a nice day’
line.startswith('Please')
line.startswith('p')


data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
atpos = data.find('@')
print atpos
sppos = data.find(' ',atpos)
print sppos
host = data[atpos+1 : sppos]
print host
name = data(data.find(' ')+ 1:atpos)
print name.replace('.', ' ').capitalize().replace('m','M')

#####################################




























