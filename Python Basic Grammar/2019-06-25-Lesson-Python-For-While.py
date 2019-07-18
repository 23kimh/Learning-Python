Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #!= - false
>>> #== - true
>>> num = input('enter number')
enter number 5
>>> num = input('enter number')
enter number5
>>> num
'5'
>>> if int(num) % 2 == 0:
	print('even')
else:
	print('odd')

	
odd
>>> #elif = else if
>>> num = int(input('enter num: '))
enter num: -5
>>> if num < 0:
	print('negative number')
elif num == 0:
	print('zero')

	
negative number
>>> #calculator
>>> num = input('enter number')
enter number10
>>> num2 = input
>>> num2 = input('enter number: ')
enter number: 2
>>> num
'10'
>>> choice = input('enter choice: ')
enter choice: 1
>>> if  choice == '1':
	print(int(num) *int(num2))
elif choice == '2':
	print(int(num)/(int(num2))
elif choice == '3'
	      
SyntaxError: invalid syntax
>>> # etc
>>> #for, while, range in...
>>> #for loop
>>> for x in range(1,9,2):
	print(x)

	
1
3
5
7
>>> for x in range(1,99,2)
SyntaxError: invalid syntax
>>> for x in range(1,99,2):
	print(x)

	
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
>>> # squared (**)
>>> 5**2
25
>>> for x in range(1,101);
SyntaxError: invalid syntax
>>> for x in range(1,101):
	print(x**2)

	
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
400
441
484
529
576
625
676
729
784
841
900
961
1024
1089
1156
1225
1296
1369
1444
1521
1600
1681
1764
1849
1936
2025
2116
2209
2304
2401
2500
2601
2704
2809
2916
3025
3136
3249
3364
3481
3600
3721
3844
3969
4096
4225
4356
4489
4624
4761
4900
5041
5184
5329
5476
5625
5776
5929
6084
6241
6400
6561
6724
6889
7056
7225
7396
7569
7744
7921
8100
8281
8464
8649
8836
9025
9216
9409
9604
9801
10000
>>> #while
>>> x = 1
>>> while x<=5:
	print(x)
	x=x+1

	
1
2
3
4
5
>>> while x<=5:
	print(x)
	x=x+2

	
>>> x = 1
>>> while x<=5:
	print(x)
	x=x+2

	
1
3
5
>>> x = 2
>>> while x<=100
SyntaxError: invalid syntax
>>> while x<=100:
	print(x)
	x=x+2

	
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100
>>> while True: #enter infinity loop


c
SyntaxError: expected an indented block
>>> #nested loop
>>> #for >for> code
>>> for x in range(1-10)
SyntaxError: invalid syntax
>>> for x in range(1,10):
	print('\n')
	for y in range(1,10):
		print(x,'*',y,'=',x*y)

		


1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9


2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18


3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27


4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36


5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45


6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54


7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63


8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72


9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
>>> while x<=9
SyntaxError: invalid syntax
>>> ###########
>>> while x<=9:
	print(x)
while y<=9:
	print(y)
	
SyntaxError: invalid syntax
>>> while x<=9:
	print(x)
	while y<=9:
		print(y)
		x = x*y

		
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
9
Traceback (most recent call last):
  File "<pyshell#89>", line 4, in <module>
    print(y)
KeyboardInterrupt
>>> 
>>> 
>>> x = 1
>>> y = 1
>>> while x<=10:
	print('\n')
	while y<10
	
SyntaxError: invalid syntax
>>> while x<=10:
	print('\n')
	while y<10:
		print(x,'*', y, '=',x*y)
		y = y+1
	x = x+1

	


1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9


















>>> while x<=10:
	print('\n')
	while y<10:
		print(x,'*', y, '=',x*y)
		y = y+1
		x = x+1

		
>>> 
>>> while x<=10:
	print('\n')
	while y<10:
		print(x,'*', y, '=',x*y)
		y = y+1
		x = x+1

		
>>> x = 1
>>> y = 1
>>> while x<=10:
	print('\n')
	while y<10:
		print(x,'*', y, '=',x*y)
		y = y+1
		x = x+1

		


1 * 1 = 1
2 * 2 = 4
3 * 3 = 9
4 * 4 = 16
5 * 5 = 25
6 * 6 = 36
7 * 7 = 49
8 * 8 = 64
9 * 9 = 81




































































































































Traceback (most recent call last):
  File "<pyshell#110>", line 2, in <module>
    print('\n')
KeyboardInterrupt
>>> while x<=10:
	print('\n')
	y = 1
	while y<10:
		print(x,'*', y, '=',x*y)
		y = y+1
	x = x+1

	


10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
>>> x = 1
>>> while x<=10:
	print('\n')
	y = 1
	while y<10:
		print(x,'*', y, '=',x*y)
		y = y+1
	x = x+1

	


1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
1 * 6 = 6
1 * 7 = 7
1 * 8 = 8
1 * 9 = 9


2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18


3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 = 15
3 * 6 = 18
3 * 7 = 21
3 * 8 = 24
3 * 9 = 27


4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
4 * 6 = 24
4 * 7 = 28
4 * 8 = 32
4 * 9 = 36


5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45


6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54


7 * 1 = 7
7 * 2 = 14
7 * 3 = 21
7 * 4 = 28
7 * 5 = 35
7 * 6 = 42
7 * 7 = 49
7 * 8 = 56
7 * 9 = 63


8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72


9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81


10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
>>> for x in range(1,9):
	for y in range(x,x+3)
	
SyntaxError: invalid syntax
>>> for x in range(1,9):
	for y in range(x,x+3):
		print(y)

		
1
2
3
2
3
4
3
4
5
4
5
6
5
6
7
6
7
8
7
8
9
8
9
10
>>> #list
>>> [1,2,3]
[1, 2, 3]
>>> list = ['a','b','c','d','e']
>>> list[3]
'd'
>>> #;ist starts out at 0
>>> list1
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list
['a', 'b', 'c', 'd', 'e']
>>> list1 = [1,'c',True]
>>> list[1] = 'cit'
>>> print(list1)
[1, 'c', True]
>>> list1[1] = 'cit'
>>> lise1
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    lise1
NameError: name 'lise1' is not defined
>>> list1
[1, 'cit', True]
>>> list =['abc','dfg','hij',123,456]
>>> list[0] = 'park'
>>> print(list)
['park', 'dfg', 'hij', 123, 456]
>>> arr = 1
>>> for i in range(1,9):
	
KeyboardInterrupt
>>> arr = []
>>> for i in rnage(1,9):
	arr.append(4*i)

	
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    for i in rnage(1,9):
NameError: name 'rnage' is not defined
>>> arr = []
>>> for i in range(1,9)
SyntaxError: invalid syntax
>>> for i in range(1,9):
	arr.append(4*i)

	
>>> print(arr)
[4, 8, 12, 16, 20, 24, 28, 32]
>>> arr[3] = 'cit'
>>> print(arr)
[4, 8, 12, 'cit', 20, 24, 28, 32]
>>> #average
>>> name = ['ted', 'jack', 'james', 'alice']
>>> score [ 92,68,50,86]
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    score [ 92,68,50,86]
NameError: name 'score' is not defined
>>> score [ 92,68,50,86]:
	
SyntaxError: invalid syntax
>>> score = [ 92,68,50,86]
>>> avg = sum(score) / len(score)
>>> avg
74.0
>>> top = score[0]
>>> 
>>> for x in range(4):
	if top < score{x+1}:
		
SyntaxError: invalid syntax
>>> for x in range(3):
	if top < score[x+1]:
		top = score[x+1]
		print('current top score:', top)
		top_index = x +1

		
>>> top_index
KeyboardInterrupt
>>> top = score[0]
>>> top_index = 0
>>> for x in range(3):
	if top < score[x+1]:
		top = score[x+1]
		print('current top score:', top)
		top_index = x +1

		
>>> top index
SyntaxError: invalid syntax
>>> top_index
0
>>> print(the average, avg, is the average, name[top_index], has teh highest score)
SyntaxError: invalid syntax
>>> print('the average', avg, 'is the average', name[top_index], 'has the highest score')
the average 74.0 is the average ted has the highest score
>>> #list's function
>>> #1. insert and append
>>> #2. delete and remove
>>> #3. index and len
>>> list0 = []#empty list
>>> list1 = [1,2,3]
>>> list1,insert(1,10) #list 1replace 1 wih 10
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    list1,insert(1,10) #list 1replace 1 wih 10
NameError: name 'insert' is not defined
>>> list1.insert(1,10) #list 1replace 1 wih 10
>>> print(list1)
[1, 10, 2, 3]
>>> list2 = [1,2,3]
>>> list2.append(10) #replace the last place in list
>>> print(list2)
[1, 2, 3, 10]
>>> # Test 1
>>> for i in range(1,10):
	list0.append(i)

	
>>> print(list0)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list0.insert(0,0)
>>> list0
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>  
