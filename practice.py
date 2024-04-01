from math import floor

a = "Hello"
b = "Saleh"
message = f'{a}, {b.upper()}. Welcome to the world!'
# print(help(str.find))

num1 = 3.56  # float(input("Enter the first number: "))
num2 = 2  # int(input("Enter the second number: "))
result = num1 + num2
# print(floor(result))

courses = ['Math', 'English', 'History']
courses2 = ['Python', 'Java']
courses.extend(courses2)
courses.remove('Math')
popped = courses.pop()
courses.sort(reverse=True)
sorted_courses = sorted(courses, reverse=True)
# print(courses)

# print(help(set))

x = 'This is global x'


def outer_test_scope():
    x = 'This is outer x'

    def inner_test_scop():
        nonlocal x
        x = 'This is inner x'
        print(x)

    inner_test_scop()
    print(x)


# list/string slicing
my_url = "https://mdsaleh.com"
# print(my_url[8:my_url.rfind('.com')])

# list comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_numbers = [n * n for n in numbers if n % 2 == 0]
# print(my_numbers)

my_list_1 = [(l, n) for l in 'abcd' for n in range(4)]
# print(my_list_1)

# dictionary comprehension
name_list = ['Saleh', 'Vijay', 'Dip']
age_list = ['18', '25', '30']
# print(zip(name_list, age_list))

my_dict_1 = {}
for name, age in zip(name_list, age_list):
    my_dict_1[name] = age

my_dict_2 = {name: age for name, age in zip(name_list, age_list)}
print(my_dict_1)
print(my_dict_2)

numbers_1 = [1, 2, 3, 4, 1, 2]
my_set_1 = {n for n in numbers_1}
print(my_set_1)

my_tuple_1 = (n for n in numbers_1)
# lambda to print the tuple
# for n in my_tuple_1:
#     print(n)
list(map(lambda n: print(n*n), my_tuple_1))


def isAnagram( s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    ls = list(s)
    ls.sort()
    lt = list(t)
    lt.sort()
    print(ls)
    print(lt)
    return ls == lt

s = 'abc'
t = 'bca'
print(isAnagram(s, t))
