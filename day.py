'''print("this is my frist code in python language")
a=10
b=20
print(a+b)'''



'''a=10

v=10.3

b="Hello"

print(type(b))'''


#taking input from user

'''num= int(input("Enter first number"))

num2= int(input("Enter second Number"))


add= num+num2

print(add)'''



'''#taking information from user 

user_name= input("enter you name")

user_middlename=input ("enter you middle name")

user_surname=input ("enter your surname")

user_Mobileno = ("enter you Mobile number")'''




'''# taking input from user addition 

num=int(input("Enter first number "))

num2=int(input("Enter second number "))

add=num + num2
 
print(add)'''



'''#taking input from user Substraction

num=int(input("Enter first number "))

num2=int(input("Enter second number "))

add=num - num2
 
print(add)'''



'''#taking input from user multiplication

num=int(input("Enter first number "))

num2=int(input("Enter second number "))

add=num * num2
 
print(add)'''



'''#taking input from user division

num=int(input("Enter first number "))

num2=int(input("Enter second number "))

add=num / num2
 
print(add)'''


'''#taking the input from user for Greater than Value
A=int(input("Enter the first choice "))

B=int(input("Enter Second choice "))


print("===Greater than ===",A>B)'''

'''#taking the input from user for Smaller than Value

A=int(input("Enter the first choice "))

B=int(input("Enter Second choice "))


print("====Smaller than ====",A<B)'''


'''#taking the input from user for Greater than of equal too Value

A=int(input("Enter the first choice "))

B=int(input("Enter Second choice "))


print("====Greater than equal to ====",A>=B)
'''

'''#taking the input from user for smaller than of equal too Value

A=int(input("Enter the first choice "))

B=int(input("Enter Second choice "))


print("====smaller than equal to ====",A<=B)'''

'''#taking the input from user for not equal too Value

A=int(input("Enter the first choice "))

B=int(input("Enter Second choice "))


print("====not  equal to ====",A!=B)'''



'''#taking the input from user for equal too Value

A=int(input("Enter the first choice "))

B=int(input("Enter Second choice "))


print("==== equal to ====",A==B)'''





'''#identity operator  IS

Ab=2020

bc=2020

print("This is Logic of IS ",Ab is bc) '''


'''#identity operator  IS NOT

Ab=2022

bc=2020

print("This is Logic of IS NOT ",Ab is not  bc)'''


'''#list 
lst=[1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1,]

#print("this is list" 1st)
print(lst[2])'''

'''lst=[1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1,]

lst[2] =1000
print(lst)'''

'''lst=[1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1,]

#print("this is list" 1st)
print(lst[2])
'''
'''#TUPLE 
lst=[1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1,]

tuple = (2:3=4)
 print(lst=(2:5))'''



'''tpl =(1,2,3,4,5,6,7,8,9,10,10,9,8,7,6,5,4,3,2,1)

#print(tpl)

#print("after slicing on tuple", tpl[2:9])

tpl[3]="Good Afternoon" # tuple is immutable data type thats why we can update values like this as we do in lists 

print(tpl)'''






# list built in methods


#1 Append - adds an element to the end of the list

'''my_list = [1, 2, 3]
my_list.append(4)
print(my_list) ''' #output : [1,2,3,4,]


#2 Extend -  Extends the list by adding elements from another iterable.

'''my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)'''  # Output: [1, 2, 3, 4, 5]


#3 Insert - Inserts an element at a specified position

'''my_list = [1, 2, 4]
my_list.insert(2, 3)  # Insert 3 at index 2
print(my_list)'''  # Output: [1, 2, 3, 4]


#4 remove - Removes the first occurrence of a specified value.

'''my_list = [2222, 23232, 45645, 23456, 40987]
my_list.remove(2222)
print(my_list)'''  # Output: [23232, 45645, 23456, 40987]

#5  POP - Removes and returns an element at a given index (default is the last element).

my_list = [1, 2, 3, 4]
popped_item = my_list.pop(2)  # Remove element at index 2
print(my_list)  # Output: [1, 2, 4]
print(popped_item)  # Output: 3
