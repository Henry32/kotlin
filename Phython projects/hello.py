a = 9
print("Hello, world!", 9)
print(a)
if a != 9:
    print("deo bang")
else:
    print("bang me no roi")
def my_function(b):
    print("my function")
    a = b
    return a
print(my_function(4))
b = ('a', 1, 'python', (1, 2))
print(b[2])
i=7
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1

print("test ---{}".format(i))
a = 'hello'

print(list(a))

print(set(a) )

print(tuple(a))

def f(m):
    m.append(3)
x = [1, 2]
print(f(x))
if x == [1, 2]:
    print('true', x == [1, 2])
else:
        print('false', x == [1, 2])
#def bar():
#    x = (1, 2)
#    f(x)
#    print(x == (1, 2))

#print(bar())

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))

my = {'a', 'b', 'c', 'd'}
for i in my:
    print("list element {}".format(i))

first_names = {'Adam', 'Charlie', 'Beth'}

for i in first_names:
    print("shit === {}".format(i))

#name = input("What is your name?\n")
#print("my name is {}".format(name))

print(dir(__builtins__))
help(set)
A = [1,2]
B = [3,4]
a = set(A)
b = set(B)
import math
print(math.sqrt(16))
#help(eval)

s = """w'o"w"""
print(repr(s))
print(str(s))
print(eval(repr(s)) == s)

b = frozenset('asdfagsa')
print(b)
def isEven(a):
    if a%2 == 0:
        return True
#this next line should be even with the if
        #return False
print(isEven(7))
import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(datetime.datetime(2000, 1, 1, 0, 0, 0))
millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)
today = datetime.date.today()
noon = datetime.time(12, 0, 0)
print('Time since the millenium at midnight: ',
datetime.datetime(today.year, today.month, today.day))
print('Time since the millenium at noon: ', datetime.datetime.combine(today, noon))
