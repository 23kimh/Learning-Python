Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> bookname = 'hello java'
>>> number = '2ONB1A'
>>> bookname.replace('java', 'python')
'hello python'
>>> len(bookname)
10
>>> bookname.upper()
'HELLO JAVA'
>>> bookname.count('A') + number.count('A')
1
>>> bookname.count('a') + number.count('a')
2
>>> 
>>> #escape
>>> print('line\nbreak')
line
break
>>> #split lines/ line break
>>> #another one
>>> print('tab\tspace')
tab	space
>>> #'t' = tab
>>> name = ['bell', 'sona', 'rick', 'tony', 'jade']
>>> score = [52, 96, 32, 73, 85]
>>> name[1[ = name[1].replace('s', 'k')
	
SyntaxError: invalid syntax
>>> name[1] = name[1].replace('s', 'k')
>>> name
['bell', 'kona', 'rick', 'tony', 'jade']
>>> for i in range (len(name)):
	if 'o' in name[i]:
		name[i] = name[1].replace('o', 'ecoto')

		
>>> name
['bell', 'kecotona', 'rick', 'kececototecotona', 'jade']
>>> name
['bell', 'kecotona', 'rick', 'kececototecotona', 'jade']
>>> name = ['bell', 'kona', 'rick', 'tony', 'jade']
>>> for i in range (len(name)):
	if 'o' in name[i]:
		name[i] = name[i].replace('o', 'ecoto')

		
>>> name
['bell', 'kecotona', 'rick', 'tecotony', 'jade']
>>> #if i in len(name) [name[1], mane[2] etc then replace ecoto
>>> print
<built-in function print>
>>> 9name
['bell', 'kecotona', 'rick', 'tecotony', 'jade']
>>> print(name)
['bell', 'kecotona', 'rick', 'tecotony', 'jade']
>>> for i in range (len(name)):
	splited_name = []
	if 'co' in name[i]:
		splited_name = name[i].split('co')
	for 'j' in range(len(splited_name)):
		name.append(splited_name[i])
		
SyntaxError: can't assign to literal
>>> for i in range (len(name)):
	splited_name = []
	if 'co' in name[i]:
		splited_name = name[i].split('co')
	for i in range(len(splited_name)):
		name.append(splited_name[i])

		
>>> name
['bell', 'kecotona', 'rick', 'tecotony', 'jade', 'ke', 'tona', 'te', 'tony']
>>> #splited_name = ['ke', 'tona']
>>> #spliting everytime there is co
>>> for i in range (len(name)):
	del(name[i]):
		
SyntaxError: invalid syntax
>>> for n in name:
	if 'co' in n:
		name.remove(n)

		
>>> name
['bell', 'rick', 'jade', 'ke', 'tona', 'te', 'tony']
>>> avg = sum(score)/len(score)
>>> avg
67.6
>>> spiderman = 'Peter' + ' ' + 'Parker'
>>> spiderma
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    spiderma
NameError: name 'spiderma' is not defined
>>> spiderman
'Peter Parker'
>>> A1 = 'abc'
>>> A2 = 'ABC'
>>> B1 = [A1 + A2]
>>> B1
['abcABC']
>>> B1 = A1 + A2
>>> B1
'abcABC'
>>> C1 = B1[2:5] + 'LE'
>>> C1
'cABLE'
>>> C1.upper()
'CABLE'
>>> C1
'cABLE'
>>> C1.C1.upper()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    C1.C1.upper()
AttributeError: 'str' object has no attribute 'C1'
>>> C1=C1.upper()
>>> C1 + 'CAR'
'CABLECAR'
>>> ghhhghgghhghffhfhfhfhhfjdh
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    ghhhghgghhghffhfhfhfhhfjdh
NameError: name 'ghhhghgghhghffhfhfhfhhfjdh' is not defined
>>> 'trgsc'
'trgsc'
>>> print('How do I hack')
How do I hack
>>> #function = input output system
>>> def bodymass(weight, height):
	#find bmi
	bmi = weight / (height**2)
	return bmi

>>> bodymass(58, 1.69)
20.307412205454995
>>> name = 'welcome'
>>> def name(welcome)
SyntaxError: invalid syntax
>>> def welcome():
	print('Hello!')

	
>>> welcome
<function welcome at 0x105857b70>
>>> welcome()
Hello!
>>> def goodbye():
	print('Goodbye!')

	
>>> goodbye()
Goodbye!
>>> def welcome(name)
SyntaxError: invalid syntax
>>> def welcome(name):
	print('Hello', name)

	
>>> welcome(name)
Hello welcome
>>> def welcome(name):
	print('Hello', name)

	
>>> welcome('hailey')
Hello hailey
>>> #return
>>> def welcome(name):
	print('Hello', name)
	return 'bye.'

>>> print(welcome('hailey'))
Hello hailey
bye.
>>> 
>>> 
>>> workbook
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    workbook
NameError: name 'workbook' is not defined
>>> #workbook
>>> 
>>> 
>>> 
>>> #workbook
>>> 
>>> print('Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are)
      
SyntaxError: EOL while scanning string literal
>>> print('Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are')
Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are
>>> print('Twinkle, twinkle, little star,\n How I wonder what you are! \n\tUp above the world so high, \nLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are')
Twinkle, twinkle, little star,
 How I wonder what you are! 
	Up above the world so high, 
Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
>>> print('Twinkle, twinkle, little star,\n How I wonder what you are! \n\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are')
Twinkle, twinkle, little star,
 How I wonder what you are! 
	Up above the world so high, 
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
>>> print('Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are')
Twinkle, twinkle, little star,
	 How I wonder what you are! 
		Up above the world so high, 
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
>>> def circleArea
SyntaxError: invalid syntax
>>> def circleArea:
	
SyntaxError: invalid syntax
>>> import math
>>> math.pi
3.141592653589793
>>> def circleArea(radius):
	print(radius**2 * math.pi)

	
>>> circleArea(1.1)
3.8013271108436504
>>> def name(first, last):
	print(last, first)

	
>>> first('Hailey')
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    first('Hailey')
NameError: name 'first' is not defined
>>> name(Hailey, Kim)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    name(Hailey, Kim)
NameError: name 'Hailey' is not defined
>>> name('Hailey', 'Kim')
Kim Hailey
>>> def extension():
	filename = input()     #from a user
	loc = filename.index('.')
	output = filename[loc+1:]
	return output

>>> extension()
test.txt
'txt'
>>> extention()
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    extention()
NameError: name 'extention' is not defined
>>> extension()
abc.java
'java'
>>> #####slicing
>>> spiderman = 'peter parker
SyntaxError: EOL while scanning string literal
>>> spiderman = 'peter parker'
>>> spiderman[6:12]
'parker'
>>> spiderman[6:]
'parker'
>>> #to the end
>>> 
>>> color_list = ["Red","Green","White" ,"Black"]
>>> color_list[0]
'Red'
>>> color_list[3]
'Black'
>>> for x in range(len(color_list))
SyntaxError: invalid syntax
>>> for x in range(len(color_list)):
	if x == 0:
		print(color_list[x])
	if x == (len(color_list) - 1):
		print(color_list[x])

		
Red
Black
>>> 
