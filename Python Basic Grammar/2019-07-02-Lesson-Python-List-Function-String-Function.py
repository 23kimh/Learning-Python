Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [1, 'c', True]
>>> type(1)
<class 'int'>
>>> type(2)
<class 'int'>
>>> type('c')
<class 'str'>
>>> type(True)
<class 'bool'>
>>> #list inside a list
>>> list1 = [1, 'cit', True]
>>> list2 = [3,4, 'py']
>>> list2 = [3, 2, 'py']
>>> list3 = [list1, list2]
>>> list3
[[1, 'cit', True], [3, 2, 'py']]
>>> list3(0)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    list3(0)
TypeError: 'list' object is not callable
>>> list3[0]
[1, 'cit', True]
>>> list3[0][1]
'cit'
>>> test1 = ['orange', 'apple', 'cherry', 'mango']
>>> test2 = ['rose', 'lavender', 'flower']
>>> test = [test1, test2]
>>> test[1]
['rose', 'lavender', 'flower']
>>> test[1][1]
'lavender'
>>> test[0][3]
'mango'
>>> 
>>> test3 = ['soccer', 'basketball', 'baseball', 'swimming']
>>> test4 = ['dog', 'penguin', 'bird']
>>> testA = [test1, test2]
>>> testB = [test3, test4]
>>> test = testA, testB]
SyntaxError: invalid syntax
>>> test = [testA, testB]
>>> #LIST DEPTH OF 3
>>> test
[[['orange', 'apple', 'cherry', 'mango'], ['rose', 'lavender', 'flower']], [['soccer', 'basketball', 'baseball', 'swimming'], ['dog', 'penguin', 'bird']]]
>>> 
>>> #Q
>>> cafe = ['starbucks', 'mollys', 'emiya', 'fomafams']
>>> mmin = ['americano', 'cappucino', 'cafelatte', 'americano']
>>> main = ['americano', 'cappucino', 'cafelatte', 'americano']
>>> price = ['3700', '4500', '3200', '4100']
>>> location = ['A street', 'B street', 'C street', 'D street']
>>> #table- chart
>>> cafetable = [cafe, main, price, location]
>>> cafetable
[['starbucks', 'mollys', 'emiya', 'fomafams'], ['americano', 'cappucino', 'cafelatte', 'americano'], ['3700', '4500', '3200', '4100'], ['A street', 'B street', 'C street', 'D street']]
>>> cafetable[0]
['starbucks', 'mollys', 'emiya', 'fomafams']
>>> for i in cafetable
SyntaxError: invalid syntax
>>> for i in cafetable:
	print(i)

	
['starbucks', 'mollys', 'emiya', 'fomafams']
['americano', 'cappucino', 'cafelatte', 'americano']
['3700', '4500', '3200', '4100']
['A street', 'B street', 'C street', 'D street']
>>> cafetable[2]
['3700', '4500', '3200', '4100']
>>> #column not row
>>> for i in cafetable
SyntaxError: invalid syntax
>>> for i in range(0,4):
	print(cafetable[1][i])

	
americano
cappucino
cafelatte
americano
>>> for i in range(0,4):
	print(cafetable[i][1])

	
mollys
cappucino
4500
B street
>>> 
>>> A = [1,4,5]
>>> B = [2,3,6]
>>> C = []
>>> for x in A:
	for y in B
	
SyntaxError: invalid syntax
>>> for x in A:
	for y in B:
		C.append(x*y)

		
>>> for z in C:
	print(z)

2
3
6
8
12
24
10
15
30
>>> # for x in A <- x replaced [1,4,5]
>>> # x = 1, x = 2, x = 3
>>> # and when x = 1, y is [2,3,6] adn so on and so forth
>>> 
>>> #dictionary
>>> #something:somthing are partner
>>> emotion = { 'happy': 'nice', 'angry', 'mean'}
SyntaxError: invalid syntax
>>> emotion = { 'happy': 'nice', 'angry': 'mean'}
>>> emotion
{'happy': 'nice', 'angry': 'mean'}
>>> #{}
>>> #key is happy and angry
>>> emotion{'happy'}
SyntaxError: invalid syntax
>>> emotion['happy']
'nice'
>>> #the result
>>> emotion['angry']
'mean'
>>> emotion['happy'] = 'good'
>>> amotion
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    amotion
NameError: name 'amotion' is not defined
>>> emotion
{'happy': 'good', 'angry': 'mean'}
>>> #replaced
>>> #2 pairs to 3 pairs... add
>>> emotion['tired'] = 'sleepy'
>>> emotion
{'happy': 'good', 'angry': 'mean', 'tired': 'sleepy'}
>>> emotion.pop('angry')
'mean'
>>> emotion
{'happy': 'good', 'tired': 'sleepy'}
>>> # pop- remove from the dictionary
>>> americano = {'starlucks':'3700', 'mollys':'4700', 'emiya':'2800','fomafams':'4100'}
>>> americano
{'starlucks': '3700', 'mollys': '4700', 'emiya': '2800', 'fomafams': '4100'}
>>> ameicano['anzelinus'] = '4900'
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    ameicano['anzelinus'] = '4900'
NameError: name 'ameicano' is not defined
>>> americano['anzelinus'] = '4900'
>>> americano['coffeejean'] = '4800'
>>> americano.pop('emiya')
'2800'
>>> americano.pop('fomafams'_
	      
SyntaxError: invalid syntax
>>> americano.pop('fomafams')
'4100'
>>> americano
{'starlucks': '3700', 'mollys': '4700', 'anzelinus': '4900', 'coffeejean': '4800'}
>>> for x in americano:
	print(x)

	
starlucks
mollys
anzelinus
coffeejean
>>> #just does around the first anyway
>>> for x in americano.values(): #be specific
	print(x)

	
3700
4700
4900
4800
>>> for x in americano:
	print(americano[x])

	
3700
4700
4900
4800
>>> for x,y in americano.items():
	print(x,y)

	
starlucks 3700
mollys 4700
anzelinus 4900
coffeejean 4800
>>> 
>>> sum = 0
>>> for x in americano.values():
	sum = sum + int(x)

	
>>> sum
18100
>>> 
>>> 
>>> #string
>>> ex = 'peter parker'
>>> ex[6:12]
'parker'
>>> #alwasy add one more!
>>> es[6:]
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    es[6:]
NameError: name 'es' is not defined
>>> ex[6:]
'parker'
>>> ex[3:5]
'er'
>>> string = 'cit acedemy'
>>> string[2:7]
't ace'
>>> 
>>> ex.split('e')
['p', 't', 'r park', 'r']
>>> #took out all es and now a lisr
>>> #list
>>> string = 'cit academy'
>>> string.split('a')
['cit ', 'c', 'demy']
>>> #count
>>> ex.count('e')
3
>>> string.count('a')
2
>>> #couting characters
>>> len(ex)
12
>>> len(string)
11
>>> ex.upper()
'PETER PARKER'
>>> ex
'peter parker'
>>> ex.replace('e', 'E')
'pEtEr parkEr'
>>> ex
'peter parker'
>>> ex = ex.upper()
>>> ex
'PETER PARKER'
>>> #to change officially
>>> 
