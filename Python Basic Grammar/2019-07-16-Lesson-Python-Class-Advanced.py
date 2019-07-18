Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ### extension of class###
>>> # parent class/ and child class exist
>>> #parent class transfer the functions and loops directly to children class.
>>> #class
>>> #class Childclass(Parentclass);
>>> #...
>>> # .. memebrs..
>>> class factory:
	brand = 'CIT'
	dat = '20190716
	
SyntaxError: EOL while scanning string literal
>>> class factory:
	brand = 'CIT'
	date = '20190716'
	def start_up(self):
		print('vroom')

		
>>> #original
>>> class py(factory):
	tire = 'thon'

	
>>> class cl(factory):
	tire = ple'
	
SyntaxError: EOL while scanning string literal
>>> 
>>> class cl(factory):
	tire = 'ple'

	
>>> carpy = py()
>>> #create instance of py class
>>> carcl = cl()
>>> carpy.brand
'CIT'
>>> car.day
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    car.day
NameError: name 'car' is not defined
>>> carpy.day
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    carpy.day
AttributeError: 'py' object has no attribute 'day'
>>> carpy.date
'20190716'
>>> carpy.tire
'thon'
>>> carcl.brand
'CIT'
>>> carcl.date
'20190716'
>>> carcl.tire
'ple'
>>> 
>>> 
>>> # Q1
>>> class cake:
	ingredients = [['bread', 5000, 'B'], ['cream', 1500, 'C']]

	
>>> # Q2
>>> class choco(cake):
	chocolate = 2000
	def cost(self):
		return self.chocolate + self.ingredient[0][1] + slef.ingredient[1][1]

	
>>> chocolate = choco()
>>> chococake.chocolate
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    chococake.chocolate
NameError: name 'chococake' is not defined
>>> chococake = choco()
>>> chococake.chocolate
2000
>>> chococake.ingredient[0][1]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    chococake.ingredient[0][1]
AttributeError: 'choco' object has no attribute 'ingredient'
>>> chococake.ingredients[0][1]
5000
>>> chococake.ingredients[1][1]
1500
>>> chocockae.costs()
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    chocockae.costs()
NameError: name 'chocockae' is not defined
>>> chococake.costs()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    chococake.costs()
AttributeError: 'choco' object has no attribute 'costs'
>>> chococake.cost()
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    chococake.cost()
  File "<pyshell#46>", line 4, in cost
    return self.chocolate + self.ingredient[0][1] + slef.ingredient[1][1]
AttributeError: 'choco' object has no attribute 'ingredient'
>>> 
>>> 
>>> #redefine
>>> #override
>>> class factory
SyntaxError: invalid syntax
>>> class factory:
	tire = 'ko'
	brand = 'cit'
	day = '20190716'
	def start_up(self):
		print(self.tire, 'start!')

		
>>> class py(factory):
	tire = 'thon;
	
SyntaxError: EOL while scanning string literal
>>> class py(factory):
	tire = 'thon'
	de start_up(slef):
		
SyntaxError: invalid syntax
>>> class py(factory):
	tire = 'thon'
	def start_up(self):
		print(super().tire, 'wing!')

		
>>> car = py()
>>> car.start_up()
ko wing!
>>> # ko start!
>>> #ko wing
>>> #thon wing
>>> 
>>> #Q1
>>> class company:
	brnad = 'py'
	ceo = 'van'
	def intro(self):
		print(self.brand, self.ceo)

		
>>> class snack(company):
	taste = 'spicy'
	print = 1500

	
>>> class drink(company):
	taste = 'sweet'
	price = 2000

	
>>> #Q2
>>> class company:
	brnad = 'py'
	ceo = 'van'
	year = 1990
	def intro(self):
		print(self.brand, self.ceo)

		
>>> #Q3
>>> class snack(company):
	taste = 'spicy'
	print = 1500

	
>>> class drink(company):
	taste = 'sweet'
	price = 2000

	
>>> #Q4
>>> snakc_instance = snack()
>>> snack_instance = snack()
>>> #Q5
>>> drink_instance()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    drink_instance()
NameError: name 'drink_instance' is not defined
>>> drink_instance() = drink()
SyntaxError: can't assign to function call
>>> drink_instance = drink()
>>> #Q5
>>> #Q6
>>> snack.instance.intro()
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    snack.instance.intro()
AttributeError: type object 'snack' has no attribute 'instance'
>>> snack_instance.intro()
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    snack_instance.intro()
  File "<pyshell#100>", line 6, in intro
    print(self.brand, self.ceo)
AttributeError: 'snack' object has no attribute 'brand'
>>> class company:
	brand = 'py'
	ceo = 'van'
	year = 1990
	def intro(self):
		print(self.brand, self.ceo)

		
>>> class snack(company):
	taste = 'spicy'
	print = 1500

	
>>> class drink(company):
	taste = 'sweet'
	price = 2000

	
>>> drink_instance = drink()
>>> snack_instance = snack()
>>> snack_instance.intro()
py van
>>> snack_instance.ceo = 'kan'
>>> snack_instance.intro()
py kan
>>> #to change
>>> 
>>> #/\
>>> 
>>> class drink(company):
	taste = 'sweet'
	price = 2000
	def build(self):
		print('in', self.year, 'years')

		
>>> drink_instance = drink()
>>> drink_instance.build()
in 1990 years
>>> 
>>> # __init__
>>> class factory:
	brand = 'cit'
	def __init__(self):
		print('brand', self.brand)

		
>>> car = factory()
brand cit
>>> class factory:
	brand = 'cit'
	def __init__(self, brand):
		self.brand = brand
		print('brand', self.brand)

		
>>> car = factory('hailey')
brand hailey
>>> class factory:
	def __init__(self, brand, day, fuel):
		self.brand = brand
		self.day = day
		self.fuel = fuel
		print('brand: ', self.brand, self.day, 'fuel:', self.fuel)

		
>>> car = factory('hailey', '20190202', 'Buffet')
brand:  hailey 20190202 fuel: Buffet
>>> #Q4
>>> class jyp:
	def __init__(slef, girlgroup, boygroup)
	
SyntaxError: invalid syntax
>>> class jyp:
	def __init__(self, girlgroup, boygroup, girlgroup_song, boygroup_song):
		print(girlgroup. ': ', girlgroup_song)
		
SyntaxError: invalid syntax
>>> class jyp:
	def __init__(self, girlgroup, boygroup, girlgroup_song, boygroup_song):
		self.girlgroup = girlgroup
		self.boygroup = boygroup
		self.girlgroup_song = girlgroup_song
		self.boygroup_song = boygroup_song
		print(self.girlgroup, ': ', self.girlgroup_song)
		print(self.boygroup, ':', self.boygroup_song)

		
>>> 
