Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #homework#
>>> 
>>> Item_name = 'Computer' #A string
>>> Item_qty = 10 #An Integer
>>> Item_value = 1000.23 #A floating point
>>> print(Item_name)
Computer
>>> print(Item_value)
1000.23
>>> print(Item_qty)
10
>>> a = 12
>>> 12 = a
SyntaxError: can't assign to literal
>>> x = y = z = 1
>>> print(x)
1
>>> print(y)
1
>>> print(z)
1
>>> x,y,z = 1,2,'abcd'
>>> print(x)
1
>>> print(y)
2
>>> print(z)
abcd
>>> x = 100
>>> print(x)
100
>>> x = 'python'
>>> print(x)
python
>>> x = 10
>>> y - 20
-18
>>> y = 20
>>> print(x)
10
>>> print(y)
20
>>> x,y = y,x
>>> print(x)
20
>>> print(y)
10
>>> var1 = 'python'
>>> def func1():
	var1 = 'PHP'
	print('In side func1() var1 = ', var1)

	
>>> def func1():
	print('In side func2() var1= '. var1)

	
>>> func1()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    func1()
  File "<pyshell#37>", line 2, in func1
    print('In side func2() var1= '. var1)
AttributeError: 'str' object has no attribute 'var1'
>>> def func2():
	print('In side func2() var1= '. var1)

	
>>> func1()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    func1()
  File "<pyshell#37>", line 2, in func1
    print('In side func2() var1= '. var1)
AttributeError: 'str' object has no attribute 'var1'
>>> def func2():
	print('In side func2() var1= ', var1)

	
>>> func1()
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    func1()
  File "<pyshell#37>", line 2, in func1
    print('In side func2() var1= '. var1)
AttributeError: 'str' object has no attribute 'var1'
>>> func2()
In side func2() var1=  python
>>> def func1():
	global var1
	var1 = 'PHP'
	print('in Side func1() var1 = ', var1)

	
>>> def func2():
	print('In side func2() var1 = '. var1)

	
>>> func1
<function func1 at 0x10b8a22f0>
>>> func1()
in Side func1() var1 =  PHP
>>> func2()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    func2()
  File "<pyshell#53>", line 2, in func2
    print('In side func2() var1 = '. var1)
AttributeError: 'str' object has no attribute 'var1'
>>> def func2():
	print('In side func2() var1 = ', var1)

	
>>> func2()
In side func2() var1 =  PHP
>>> 
>>> 
>>> #end of python variable
>>> 
