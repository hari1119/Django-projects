from datetime import datetime, timedelta
from functools import reduce
import math, json, random, csv, sys

ele = [2, 5, 6, 2, 8]
# Bubble sort
n = len(ele)

for i in range(n):
    for j in range(0, n-i-1):
        if ele[j] > ele[j+1]:
            # Swap elements if they are in the wrong order
            ele[j], ele[j+1] = ele[j+1], ele[j]
# Print the sorted list
print(ele)

# class Animal:
#     pass

# class Dog:
#     pass

# my_dog = Dog()
# if isinstance(my_dog, Animal):
#     print("my_dog is an instance of Animal or its subclass")
# y = [1, 2, 3]
# if isinstance(y, ( tuple)):
#     print("y is a list or tuple")

# user = int(input('Enter any number to print start: ')) 

# for i in range(1, user+1):
#     for j in range(1, i+1):
#         print('*', end=' ')
#     print()       

# for i in range(1, user+1):
#     for j in range(user-i):
#         print(' ', end=' ')
#     for k in range(2*i-1):
#         print('*', end=' ')
#     print()     

# import make_call


# sys.setrecursionlimit(20)
# i = 0
# def he():
#     global i
#     i+=1
#     print('test', i )
#     he()
# he()    
# exit()    
# while True:
#     user = int(input('Enter number greater then 50:'))
#     if user < 50:
#         print('wrong number')
#         continue
#     elif user == 50:        
#         print('good')
#         pass
#     else:
#         print('you are correct')
#         break

# print(random.random()*30)
# print(random.randint(10,50))
# print(random.choice(['vj','thala', 'sk']))


# lst = ['car','mob', 'bike','laptop', 'ship']
# for i,d in enumerate(lst):
#     print(i,d,'okay', sep='--')
    
# data = {
#     'name':'praba',
#     'age':27,
#     'email':False,
#     'nsum':None,
#     'money':3.3,
# }

# print(data)  
# with open('sample.json', "w") as json_write:
#     json.dump(data, json_write, indent=4)
#     json_write.close()

# json_data = json.dumps(data, indent=2)
# print(json_data)    

# with open('sample.json', 'r') as json_read:
#     rd_json=json.load(json_read)
#     json_read.close()
#     print(rd_json)
# dict_data = json.loads(json_data)
# print(dict_data)

# ls = [2,3,1,6,8,10,12]

# m = list(map(lambda x:x*x, ls))
# print(m)
# f = list(filter(lambda x: x>7, ls))
# print(f)
# r = reduce(lambda x,y:x+y, ls)
# print(r)

# temp = ls[0]
# ls[0] = ls[len(ls)-1] 
# ls[len(ls)-1]=temp

# ls[0], ls[-1] = ls[-1], ls[0]

# print(ls)



# file_name = 'example.csv'

# # Open the CSV file in write mode
# with open(file_name, 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)

#     # Write the header row
#     csv_writer.writerow(['Column1', 'Column2', 'Latitude', 'Longitude', 'IP Address', 'Username'])

#     # Generate 1000 dynamic data rows
#     for i in range(1, 1001):
#         current_datetime = datetime.utcnow()
#         desired_date = current_datetime - timedelta(days=i)  # Adjust as needed

#         latitude = random.uniform(-90, 90)
#         longitude = random.uniform(-180, 180)
#         ip4_address = f'192.168.1.{random.randint(1, 255)}'
#         user_name = f'User{i}'

#         # Write the data row
#         csv_writer.writerow([i, desired_date, latitude, longitude, ip4_address, user_name])

# print(f'{file_name} has been created successfully.')
















# def generate_numbers_and_sum(a, b):
#     result = a + b
#     yield result

#     for i in range(5):
#         yield i

#     # return "Done"

# gen = generate_numbers_and_sum(3, 5)
# print(next(gen),'-----')

# for value in gen:
#     print(value)
    
# numbers=[1,2,3,4,5,6,7,8,9,10]

# n_map = list(map(lambda x: x if x%2==0 else 0, numbers))
# print(n_map)

# n_filter = list(filter(lambda x: x%2==0, numbers))
# print(n_filter)

# result = reduce(lambda x, y: x+y , n_filter,2)
# print(result)


# try:
#     print('1'+1)
# except TypeError as ee:
#     print('error', ee)
# except Exception as e:
#     print('error', e)       
# else:
#     print('s')
# finally:
#     print('finally')

# for i in range(1,9):
# exit()
# tr = 'kakak'
# def myfun(x):
#     global tr
#     tr = 'praba'
#     return x!=0,x
# myfun(0)

# print(tr)

# sort_element =  [0,0,5,4,6,2,1]
# sort_element.sort(reverse=False, key=myfun)
# print(sort_element)

# print(sorted(sort_element, key=lambda x: (x == 0, x)))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print((lambda x: 'good' if x % 2 == 0 else 'bad') (2))
# [print(number) for number in numbers if (lambda x: x % 2 == 0)(number)]

# alph = ["a", "b", "c", "d"]
# lambda_map_data = tuple(map(lambda x:x.upper(),alph))
# print(lambda_map_data)

# sas=lambda x : x+1
# print(sas(2))



# def some_function(x):
#     result = x * 2
#     assert result > 0, "Result should be positive"
#     return result

# print(some_function(1))
# x = "hello"

# #if condition returns True, then nothing happens:
# assert x == "hello"

# #if condition returns False, AssertionError is raised:
# # assert x == "goodbye"
# sample_list = ["red", "blue", "green"]
# sample_list.remove("blue")
# print(sample_list)

# x = [1, 2, 3]
# y = x  # y is assigned to the same object as x
# result = x is y 
# print(result)

# sample_dict =	{
# "user": "test_user",
# "age": "20",
# "mail": 'test@gmail.com'
# }
# del sample_dict["user"]
# print(sample_dict)
# from functools import reduce
# s=[3, 4, 6, 9, 34, 12]
# print(sum(s))

# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# over_75 = list(filter(lambda x:x > 75, scores))
# print(over_75)




# map_data = list(map(str.upper ,alph))
# print(lambda_map_data)
# print(map_data)


# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [1, 2, 3, 4, 5,6]
# results = list(zip(my_strings, my_numbers))
# print(results)

# list_comprehension_if_else = [i if i > 75 else 0 for i in scores]
# list_comprehension_if = [i for i in scores if i > 75]
# mrk = [[1,2,3], [4,5,6], [7,8,9]]
# two_loop= [j if j > 5 else 0 for i in mrk for j in i] 
# print(two_loop)
# print(list_comprehension_if)
# print(list_comprehension_if_else)


# a  = [1, '2', '0']
# print(any(a))

# def myfunc(a):
#     return len(a) <= 5

# x = filter(myfunc, ('apple', 'banana', 'cherry'))
# filtered_list = list(x)
# print(filtered_list)


# print(3**2)
# str1 = 'abcd'
# str1[2] = 'z'
# print(str1)

# print(100/2)
# print(100//2)


# # print("Python" * 5)


# # all(), any(), map(), filter(), reduce(), , issubclass() 


# #---------------------------            
# # Django ORM 
# #---------------------------
# # CREATE
# # create = Album(title = "Divide", artist = "Ed Sheeran", genre = "Pop")
# # create.save()
# #
# # READcopy()
# # Album.objects.all()
# # Album.objects.filter(artist = "The Beatles")
# # Album.objects.exclude(genre = "Rock")
# # Album.objects.get(pk = 3)
# #
# # UPDATE
# # Update = Album.objects.get(pk = 3)
# # Update.genre = "Pop"
# # Update.save()
# #
# # DELETE
# # Album.objects.filter(genre = "Pop").delete()
# #---------------------------
# # DJANGO ORM BUILT-IN
# # data = Album.objects.all()
# # data.query | it show the query of ORM

# #---------------------------
# # Django Relationship 
# #---------------------------
# # Many-to-one  = ForeignKey      - models.ForeignKey(Album, on_delete = models.CASCADE)
# # Many-to-Many = ManyToManyField - models.ManyToManyField(Author)
# # One-to-One   = OneToOneField   - models.OneToOneField(Vehicle, on_delete = models.CASCADE, primary_key = True)
#       # Data integrity options: on_delete --- [ models.CASCADE , models.PROTECT, models.SET_NULL, models.SET_DEFAULT ]
# #---------------------------

# # DATABASE DUMP

# # pg_dump database_name > new_database_name.sql
# # createdb  database_name
# # psql database_name < file_name.sql

