while Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1,2,3]
>>> list1.insert(1,10)
>>> list1
[1, 10, 2, 3]
>>> list2 = [1,2,3]
>>> list2.append(10)
>>> list2
[1, 2, 3, 10]
>>> #append is alwasy at the end
>>> #test 1
>>> list0 = []
>>> for i in range(1,10,1):
	list0.append(i)

	
>>> list0
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list0.insert(0,0)
>>> list0
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> thislist = ['apple','banana', 'cherry']
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist2 = ['banana', 'cherry', 'apple']
>>> thiislist == thislist2
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    thiislist == thislist2
NameError: name 'thiislist' is not defined
>>> thislist[1]
'banana'
>>> #lists are different
>>> #change item value
>>> thislist[1] = 'blackcurrent'
>>> print(thislist1)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(thislist1)
NameError: name 'thislist1' is not defined
>>> print(thislist)
['apple', 'blackcurrent', 'cherry']
>>> #loop through a list
>>> thilist = ['apple', 'banan', 'cherry']
>>> for x in thislist
SyntaxError: invalid syntax
>>> for x in thislist:
	print(x)

	
apple
blackcurrent
cherry
>>> thislist = ['cherry', 'apple', 'banana']
>>> if 'apple' in thislist
SyntaxError: invalid syntax
>>> if 'apple' in thislist:
	print('yes')

	
yes
>>> #list length
>>> thislist
['cherry', 'apple', 'banana']
>>> #use len()
>>> len(thislist)
3
>>> #add item
>>> thislist
['cherry', 'apple', 'banana']
>>> thislist.append('grape')
>>> thislist
['cherry', 'apple', 'banana', 'grape']
>>> len(thislist)
4
>>> #add item- second method
>>> thislist
['cherry', 'apple', 'banana', 'grape']
>>> thislist.insert(2, 'mango')
>>> 
>>> thislist
['cherry', 'apple', 'mango', 'banana', 'grape']
>>> len(thislist)
5
>>> #remvoe item
>>> #1. del()- using the delete function
>>> #2. using .remove()
>>> #del() - location
>>> #remove  - content
>>> list1 = [1,2,3]
>>> del(list[1])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    del(list[1])
TypeError: 'type' object does not support item deletion
>>> del(list1[1])\

	       
>>> print(list1)
[1, 3]
>>> list2.remove(2)
>>> print(list2)
[1, 3, 10]
>>> list0
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del(list0[2])
>>> 
>>> list0
[0, 1, 3, 4, 5, 6, 7, 8, 9]
>>> del(list0[5])
>>> list0
[0, 1, 3, 4, 5, 7, 8, 9]
>>> list0.remove
<built-in method remove of list object at 0x108bbe0c8>
>>> list0.remove(0)
>>> 
>>> list0
[1, 3, 4, 5, 7, 8, 9]
>>> 
>>> 
>>> # list.index(content)
>>> #len(list)
>>> list1 = [1,2,3]
>>> list1.index(3)
2
>>> list2 = [1,2,3]
>>> len(list2)
3
>>> list0
[1, 3, 4, 5, 7, 8, 9]
>>> # q3
>>> list0.index(5)
3
>>> #Q7
>>> list0.index(6)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    list0.index(6)
ValueError: 6 is not in list
>>> len(list0)
7
>>> week = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri']
>>> week.append('Sat')
>>> week
['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat']
>>> week.append('sun')
>>> week
['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'sun']
>>> del(week[1])
>>> week
['Mon', 'Wed', 'Thu', 'Fri', 'Sat', 'sun']
>>> week.insert(1,'Tues')
>>> len(week)
7
>>> week
['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'sun']
>>> 
>>> #infinte loop
>>> score_list = []
>>> while True:
	score = int(input())
	if score == 0
	
SyntaxError: invalid syntax
>>> while True:
	score = int(input())
	if score == 0:
		break
	score_list.append(score)

	
10
20
20
10
0
>>> score_list
[10, 20, 20, 10]
>>> avg = sum(score_list) / len(score_list)
>>> avg
15.0
>>> #why int
>>> temp = input()
7
>>> temp
'7'
>>> type(temp)
<class 'str'>
>>> 
>>> 
>>> hobby_list = []
>>> while True
SyntaxError: invalid syntax
>>> while True:
	hobby = input()
	if hobby == '0':
		break
	hobby_list.append(hobby)

	
soccor
reading
programming
0
>>> hobby_list
['soccor', 'reading', 'programming']
>>> print('your hobby is' hobby_list)
SyntaxError: invalid syntax
>>> print('your hobby is', hobby_list)
your hobby is ['soccor', 'reading', 'programming']
>>> if 'reading' in hobby_list:
	print('recommend <Little Prince>')

	
recommend <Little Prince>
>>> if 'proogramming' in hobby_list:
	print('recommend<python>')

	
>>> 
>>> if 'programming' in hobby_list:
	print('recommend<python>')

	
recommend<python>



