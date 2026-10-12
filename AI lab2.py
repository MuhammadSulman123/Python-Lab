# ........................................AI LAB-2....................................

# Example:
# python program to illustrate
# while loop
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")


    # single statement while block;


# python program to illustrate
# single statement while block
# count = 0
# while (count == 0): 
  #  print("Hello Geek")

# for in loop:

# Example:1
# python program to illustrate
# Iterating over a list
print("List iteration")
l = ["geeks", "for","geeks"]
for i in l:
    print(i)


# Example 2
# iterating over a tuple (immutable)
print("\nTuple iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)


# Example 3:
#iterating over a string 
print("\n string iteration")
s = 'Geeks'
for i in s: 
    print(i)


# Iterating by index of sequences:


# python program to illustrate 
# iteratig by index
list = ["Geeks", "for", "geeks"]
for index in range (len(list)):
    print (list[index])

# loop control statements:
# print all letters except 'e' and 's'

for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        continue
    print(f"currentletter ,{letter}")

# break statement:
for letter in 'geeksforgeeks':
    if letter == 'e' or letter == 's':
        break
    print(f"currentletter ,{letter}") 

# functions

def my_function1():
    print("hello from a function") 

my_function1()   


#function parameters:


def my_function2(fname):
    print(fname + "refnes")

my_function2("email")
my_function2("tobias")



# passing a list as a parameter



def my_function3(food):
    for x in food:
        print(x)
fruits = ["apple","cherry","bannaa"]
my_function3(fruits)


# class.....


class myclass: x = 5
p1 = myclass()
print(p1.x)


# inite function

# class person:
#     def __init__(self,name,age):self.name=name
#     self.age=age
#     p1 = person("jhon",36)
# print(p1.name)
# print(p1.age)