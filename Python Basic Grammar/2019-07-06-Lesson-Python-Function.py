Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #say
>>> def say(name):
	print(name, 'is entered')

	
>>> say('name'_
    
SyntaxError: invalid syntax
>>> say('name')
name is entered
>>> 
>>> for i in range(1,10):
	print('*' * i)

	
*
**
***
****
*****
******
*******
********
*********
>>> def star(count):
	print('*' *count)

	
>>> for i in range(1,10):
	star(i)

	
*
**
***
****
*****
******
*******
********
*********
>>> def star(count):
	print('*' *count)
	return 0

>>> #return
>>> list = [8,2,3,0,8]
>>> def list(count):
	print(list + count)

	
>>> for i in(list)
SyntaxError: invalid syntax
>>> for i in(list):
	list(i)

	
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for i in(list):
TypeError: 'function' object is not iterable
>>> sum = 0
>>> for i in list:
	sum +=i
print(sum)
SyntaxError: invalid syntax
>>> for i in list:
	sum +=i

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    for i in list:
TypeError: 'function' object is not iterable
>>> #functions
>>> def addition(list):
	sum = 0
	for l in list
	
SyntaxError: invalid syntax
>>> def addition(list):
	sum = 0
	for l in list:
		sum +=l

		
>>> def addition(list):
	sum = 0
	for l in list:
		sum +=l
		return sum
	#call function

	
>>> additiondef addition(list):
	sum = 0
	for l in list:
		sum +=l
	return sum
	#call function
SyntaxError: invalid syntax
>>> def addition(list):
	sum = 0
	for l in list:
		sum +=l
	return sum
	#call function
