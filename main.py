print(2**3)
print(4 // 2)
print(2 // 4)
print(7 // 3)

print(10 % 5)

print(round(4.5))
print(round(0.99))

print(abs(-3))
print(abs(9.8))
print(abs(-0.99))

some_value = 5
some_value -= 2
print(some_value)

value = 6
value = value + 8
print(value)

value = 7
number = value * 9
print(number)

long_string = '''
ant
elephant
lion
WWW
O O
---
'''
print(long_string)

first_name = 'Moulya'
last_name = 'K A'
full_name = first_name + last_name
print(full_name)

first_name = 'Moulya '
last_name = 'K A'
full_name = first_name + last_name
print(full_name)

first_name = 'Moulya'
last_name = 'K A'
full_name = first_name + ' ' + last_name
print(full_name)

print('hello' + ' world')

print(str(100))
print(type(str(100)))
print(type(int(str(100))))

a = str(6)
b = int(a)
c = type(b)
print(c)

weather1 = "It's kind of sunny"
print(weather1)

weather2 = "It\'s \"kind of\" sunny"
print(weather2)

weather3 = "It\\s \"kind of\" sunny"
print(weather3)

weather4 = " \t It\'s\"kind of\" sunny"
print(weather4)

weather5 = " \t It\'s\" kind of\" sunny \n hope u have a good day!"
print(weather5)

name = 'Johnny'
age = 55
print('hi' + name + '.You are ' + str(age) + ' years old')

print(f'hi {name}.You are {age} years old')

print('hi {}.You are {} years old'.format('John', 25))

print('hi {0}.You are {1} years old'.format(name, age))

selfish = 'me me me'
print(selfish[4])

selfish = '012345678'
print(selfish[1:5])
print(selfish[0:7:3])
print(selfish[2:])
print(selfish[:6])
print(selfish[::1])
print(selfish[-1])
print(selfish[::-1])

selfish = '01234567'
selfish = selfish + '8'
print(selfish)

print(len('hellllooooo'))

greet = 'hellooo'
print(greet[1:len(greet)])

quote = 'to be or not to be'
print(quote.upper())

quote = "to be or not to be"
print(quote.capitalize())

quote = 'to be or not to be'
print(quote.find('or'))

quote = 'to be or not to be'
print(quote.replace('to', 'the'))

quote = 'to be or not to be'
print(quote.replace('be', 'me'))
print(quote)

#birth_year =input ('what year were you born?')
#age =(2023 -int( birth_year))
#print (f'your age is: {age}')

#username = input('what is your name?')
#password = input('what is your password?')
#password_length = len(password)
#hidden_password = '*' * password_length
#print(f'{username},your password,{hidden_password},is {password_length} letters long')

#list = [1,'a',0.5,True]
#print(list)

amazon_cart = ['notebooks', 'sunglasses']
print(amazon_cart[1])

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'
print(amazon_cart)

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'
print(amazon_cart[0:3])
print(amazon_cart)

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'
new_cart = (amazon_cart[0:3])
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'
new_cart = (amazon_cart[:])
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

matrix = [[1, 5, 1], [3, 4, 5], [5, 4, 6]]
print(matrix[2][0])

basket = [1, 2, 3, 4, 5, 6]
basket.append(100)
new_list = basket
print(basket)
print(new_list)

basket.insert(5, 20)
print(basket)

basket.extend([80])
print(basket)

basket.pop()
print(basket)

basket.pop()
basket.pop()
print(basket)

basket.pop(1)
print(basket)

basket.remove(3)
print(basket)

box = [1, 2, 3, 4]
new = box.remove(4)
print(new)

box = [1, 2, 3, 4]
new = box.pop(2)
print(new)

newlist = basket.clear()
print(basket)

container = ['a', 'b', 'c', 'd', 'f', 'e', 'd']
print(container.index('b'))

print(container.index('d', 0, 4))

print('f' in container)

print(container.count('d'))

print(container.sort())

container.sort()
print(container)

print(sorted(container))

new_container = container[:]
new_container.sort()
print(new_container)
print(container)

container.reverse()
print(container)

print(list(range(1, 100)))

print(list(range(100)))

sentence = ' '.join(['hi', 'my', 'name', 'is', 'moulya'])
print(sentence)

a, b, c = 1, 2, 3
print(a)
print(b)
print(c)

a, b, c, *other = [1, 2, 3, 4, 5, 6, 7]
print(other)

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7]
print(other)

weapons = None
print(weapons)

dictionary = {'a': 1, 'b': 2}
print(dictionary['b'])

my_list = [{
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}, {
    'a': [4, 5, 6],
    'b': 'hello',
    'x': False
}]
print(my_list[0]['a'][2])

dictionary = {'123': [1, 2, 3], '123': 'hello'}
print(dictionary['123'])

user = {'basket': [1, 2, 3], 'greet': 'hello'}
print(user.get('age'))

print(user.get('age', 50))

user2 = dict(name='John')
print(user2)

print('basket' in user)

print('greet' in user.keys())

print('hello' in user.values())

print(user.items())

print(user.clear())

user.clear()
print(user)

user3 = {'a': [4, 5, 6], 'b': 'hello', 'x': False}
print(user3.pop('b'))
print(user3)

print(user3.popitem())

print(user3.update({'age': 50}))
print(user3)

my_tupule = (1, 2, 3, 4, 5)
print(my_tupule[1])

print(5 in my_tupule)

print(my_tupule.count(4))

print(my_tupule.index(3))

print(len(my_tupule))

new_tupule = my_tupule[1:2]
print(new_tupule)

my_set = {1, 2, 3, 4, 5, 6, 6}
print(my_set)

print(1 in my_set)
print(len(my_set))
print(list(my_set))

my_list = [1, 2, 3, 4, 5, 5, 5]
print(set(my_list))

my_set.add(100)
my_set.add(2)
print(my_set)

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set)

my_set2 = {1, 2, 3, 4, 5, 6}
your_set = {4, 5, 6, 7, 8, 9}

#print(my_set2.difference(your_set))
#print(my_set2.discard(5))
#print(my_set2)
#print(my_set2.difference_update(your_set))
#print(my_set2)
#print(my_set2.intersection(your_set))
#print(my_set2 & (your_set))
#print(my_set2.isdisjoint(your_set))
#print(my_set2.union(your_set))
print(my_set2 | your_set)
print(my_set2.issubset(your_set))
print(your_set.issuperset(my_set))

is_old = True
is_licenced = True

if is_old:
  print('you are old enough to drive!')

elif is_licenced:
  print('you can drive now!')
else:
  print('you are not of age')

is_old1 = False
is_licenced1 = False

if is_old1 and is_licenced1:
  print('you are old enough to drive and you have a licence!')

else:
  print('you are not of age')


is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message'
print(can_message)

is_friend = True
is_User = False
if is_friend or is_User :       #can use and also
  print('best friends forever')

is_magician = False
is_expert = False

if is_expert and is_magician :
  print('you are a master magician')

elif is_magician and not is_expert :
  print('atleast you are getting there')

elif not is_magician : 
  print('you need magic powers')

#for item in 'Zero to mastery':
 # print(item)

#for item in (1,2,3,4,5):
 # for x in ['a','b','c']:
   # print(item,x)

#user = {
 # 'name':'Ram',
 # 'age': 50,
 # 'can_swim':False
#}

#for item in user :
 # print(item)

#for item in user.items():
#  print(item)

#for item in user.values():
 # print(item)

#for item in user.keys():
 # print(item)

#for key,value in user.items():
  #print(key,value)

#my_list = [1,2,3,4,5,6,7,8,9,10]
#counter = 0
#for item in my_list:
 # counter = counter +item
#print(counter)

#print(range(100))

#for number in range (0,100): 
  # print(number)


#for _ in range(0,10,2):
 #  print(_)

#for _ in range(2):
 # print(list(range(10)))

#for i,character in enumerate([1,2,3]) :
   # print(i,character)

#for i,character in enumerate(list(range(100))):
  #print(i,character)
  #if character == 50:
   # print(f'index of 50 is :{i}')


#i = 0 
#while i < 50 :
   # print(i)
    #i=i+1

#else :
   # print('done with all work')

#my_list = [1,2,3]
#for item in my_list:
  #print(item)

#i = 0
#while i < len(my_list) :
 # print(my_list[i])
 # i = i+1

#while True :
 # input('say something:')
 # break

#while True :
 # response = input('say something')
 # if(response == 'bye'):
    #break

#my_list = [1,2,3]
#for item in my_list:
 # continue
  #print(item)

#i=0
#while i<len(my_list):
 # i +=1
  #continue
  #print(my_list[i])

#my_list = [1,2,3]
#for item in my_list:
 # pass

#i = 0 
#while i < len(my_list) :
 # print(my_list)
 # i+=1
 # pass

# picture = [
 # [0,0,0,1,0,0,0],
 # [0,0,1,1,1,0,0],
  #[0,1,1,1,1,1,0],
 # [1,1,1,1,1,1,1],
  #[0,0,0,1,0,0,0],
 # [0,0,0,1,0,0,0]

#]
# for row in picture:
#  for pixel in row:
#    if (pixel == 1):
#      print('*', end ='')

#    else:
#      print(' ', end ='')
#  print('')

"""some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for value in some_list:
   if some_list.count(value) > 1:
    if value not in duplicates:
        duplicates.append(value)
print(duplicates)

def say_hello():
   print('helloo')
say_hello()

print(say_hello)

def say_hi (name,emoji):
  print( f'hello{name} {emoji}')
say_hi(' Andrei' ,'😊')
say_hi(' dan','😂')

say_hi(emoji='😍',name = ' moulya')

def say_bye(name='Ram',emoji='😁'):
  print(f'bye {name} {emoji}')
say_bye()"""

"""import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)"""

"""x = int(input("enter a value of x: "))
match x:
  case 0:
    print("x is zero")
  case 4:
    print("x is 4")
  case _:
    print(x)"""

"""def calculateGmean(a,b):
  print((a*b)/(a+b))

def isgreater(a,b):
  if a > b:
    print("a is greater")
  else:
    print("b is greater")

isgreater(2,3)
calculateGmean(2,3)"""

"""def greet(**name):
  print("hello",name["fname"],name["lname"])

greet( fname = "john",lname = "khan")"""
#write a program that an integer as  input 'n' and counts the #number of digits in the binary representation of 'n' using #recursion.
"""n = int(input("enter a number: "))
def count_digits(n):
  if n == 0:
    return 0
  else:
    return 1 + count_digits(n//2)
print(count_digits(n))"""

#write a program to find gcd by subtraction method

"""def gcd_subtraction(a, b):
  while a != b:
      if a > b:
          a = a - b
      else:
          b = b - a
  return a

result = gcd_subtraction(4, 6)
print(result)"""

"""l =[1,8,4,5,6,7,9,2]
print(l)
l.append(3)
print(l)
l.sort()
print(l)"""

name = "moulya"
age = 18
print(f"my name is {{name}} and my age is{{age}}")


"""def square(n):
#docstring should be placed below the function name otherwise it doesn't work
  '''
  this function returns the square of a number'''
  print(n**2)
square(5)
print(square.__doc__)"""


#import this #gives the zen of python by tim peters

"""def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n -1)
print(factorial(3))"""

#fibonacci sequence


"""def fib(n):
  if n == 0 or n == 1:
    return n
  else:
    return fib(n-1) + fib(n-2)
print(fib(5))"""

"""for i in range(5):
  print(i)
  if i == 3:
    break

else:
   print("no i ")"""

"""a =int(input("enter a number: "))
for i in range(1,11):
  print(f"{a} * {i} = {a*i}")"""

#exceptional handling
"""try:
  a = int(input("enter a number: "))
  b = int(input("enter a number: "))
  print(a/b)
except ZeroDivisionError:
  print("division by zero is not allowed")
except ValueError:
  print("invalid input")"""


#finally keyword
"""def func():
  try:
    l = [1,2,3,4]
    i = int(input("enter a index: "))
    print(l[i])
    return 1
  except:
    print("some error occured")
    return 0

  finally:
    print("i am always executed")

x = func()
print(x)"""
"""a = int(input("enter a number between 4 and 8: "))

if (a<4 or a>8):
  raise ValueError("Value should be between 4 and 8")"""

a = [1,23,4,5,6,765,54]
for index, i in enumerate(a):
  print(i)
  if (index == 3):
    print("you r awesome")


  
  



  

  














    