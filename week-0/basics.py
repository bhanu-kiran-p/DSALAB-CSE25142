'''
# ASSIGNING MULTIPLE VARIABLES TO MUTLIPLE VALUES
a, b, c = "hi", 147, True
print(f"a is {a}")
print(f"b is {b}")
print(f"c is c")


# TYPE CONVERSIONS IN PYTHON
#1. implicit type conversions
a = 123
b = 1.23
c = a+b
print(type(c))


name = "bhanu"
roll = 25142                          # in this case implicit conversion do not work
name_roll = name + roll
print(type(name_roll))


#EXPLICIT TYPE CONVERSION
a = "123"
b = 5
c = int(a) + b
print(type(c))


print("hello", "Bhanu", "from", "India", sep = ",")


#TAKING INPUTS
num = input('Enter a number: ')
print(f"the number is {num}")
print(type(num))

num = int(input('Enter a number: '))
print(f"the number is {num}")
print(type(num))


# NESTED IF STATEMENTS
num = 5
if num>=0:
    if num==0:
        print('numbers is 0')
    else:
        print('positive')
else:
    print('negative')


nums = [1, 2, 3, 4]
for num in nums:
    print(num)
print('end')
print("---------------")
for num in nums:
    if num==3:
        break
    else:
        print(num)
print("end")
print("---------------")
for num in nums:
    if num==3:
        continue
    else:
        print(num)
print("end")


n = 10
if n>10:
    pass
print('end')

n = 10
if n>10:          
    # write the code later     #this throws an indentation error
print('end')
'''

import random

list1 = ['a', 'b', 'c', 'd']
print(list1)
print(random.choice(list1))

random.shuffle(list1)
print(list1)

print(random.randrange(10, 20))
print(random.random())

          
