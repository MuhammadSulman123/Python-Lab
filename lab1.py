

# ........................................ LAB 1.......................................



# .............. TASK_1 ...........:

x = 1
if x > 0:
    print("print a string")


# ............... TASK_2..........:


print("statement1")
print("statement2")
# you can write above two statements int the following way
print("Statement1");print("Statement2")



#............... TASK_3............:



#x = 1
#if x > 0 :
#print("this statement has no indentation")
#print("this statement has no indentation")



#x = 1
#if x > 0 :
# print("this statement has a singal space imdentation")
# print("this statement has a singal space imdentation")



# x = 1
# if x > 0 :
#   print("this statement has a singal tab imdentation")
#   print("this statement has a singal tab imdentation")



# x = 1
# if x > 0 :
#    print("this statement has a space+tab imdentation")
#    print("this statement has a space+tab imdentation")





# ...................TASK_5.............:


a=1452
type(a)
print(a)

b=(-4587)
type(b)
print(b)

c=0
type(c)
print(c)

g=1.03
type(g)
print(g)

h=-11.23
type(h)
print(h)

i=.34
type(i)
print(i)

j=2.12e-10
type(j)
print(j)

k=5E220
type(k)
print(k)



# ................ Task 6..............


x=complex(1,2)
type(x)
print(x)

z=1+2j
type(z)
print(z)

z=1+2J
type(z)
print(z)


# .................. Task 7.............


x = True
type(x)
print(x)

y = False
type(y)
print(y)


# ................. Task 8..............



str1 = "String" #Strings start and end with double quotes
print(str1)

str2 = "String" #Strings start and end with single quotes
print(str2)

# str3 = "String' #Strings start with double quote and end with single quote
# print(str3)

str1 = 'String' #Strings start with single quote and end with double quote
print(str1)

str2 = "Day's" #Single quote within double quotes
print(str2)

str2 = 'Day"s' #Double quote within single quotes
print(str2)




# ........... Task 9 ............



print("The is a backslash (\\) mark.")
print("This is tab \t key")
print("These are \'single quotes\'")
print("These are \"double quotes\"")
print("This is a new line\nNew line")




# ........... Task 10 ............



string5 = "PYTHON TUTORIAL"

print(string5[0]) #Print first character

print(string5[-15]) #Print first character

print(string5[14]) #Print last character

print(string5[-1]) #Print last character

print(string5[4]) #Print 4th character

print(string5[-11]) #Print 4th character

# print(string1[16]) #Out of index range




# ........... Task 11 ...........




my_list1 = [5, 12, 13, 14] # the list contains all integer values
print(my_list1)

my_list2 = ['red', 'blue', 'black', 'white'] # the list contains all string values
print(my_list2)

my_list3 = ['red', 12, 112.12] # the list contains a string, an integer and a float values
print(my_list3)




my_list=[]
print(my_list)



# .......... Task 12 ...........



color_list=["RED", "Blue", "Green", "Black"] # The List have four elements indices start at 0 and end at 3

color_list[0] # Return the First Element

print(color_list[0],color_list[3]) # Print First and Last Elements

color_list[-1] # Return Last Element

# print(color_list[4]) # Creates Error as the indices is out of range




# .......... Task 13...........



color_list=["RED", "Blue", "Green", "Black"] # The List have four elements indices start at 0 and end at 3

print(color_list[0:2]) # Cut first two items

print(color_list[1:2]) # Cut second item

print(color_list[1:-2]) # Cut second item

print(color_list[:3]) # Cut first three items

print(color_list[:]) # Creates copy of original list