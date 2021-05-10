# my_dict = {'a':50, 'b':58, 'c':56, 'd':40, 'e':100, 'f':20,"g":678,"y":788}
# a = []
# for i in my_dict:
#     a.append(my_dict[i])
# print(a)
# i = 0
# b = a[0]
# while i < len(a):
#     if a[i] > b:
#         b = a[i]
#     i = i + 1
#     a.remove(b)
#     j = 0
#     c = a[0]
#     while j < len(a):
#         if a[j] > c:
#             c = a[j]
#         j = j + 1
#         a.remove(c)
#         k = 0 
#         d = a[0]
#         while k < len(a):
#             if a[k] > d:
#                 d = a[k]
#             k = k + 1
#         print(b,c,d)

# my_dict = {'a':50, 'b':58, 'c':56, 'd':40, 'e':100, 'f':20,"g":678,"y":788}
# a = []
# for i in my_dict:
#     a.append(my_dict[i])
# print(a)
# i = 0
# b = []
# while i < len(a):
#     c = max(a)
#     a.remove(c)
#     b.append(c)
#     i = i + 1
# print(b)


# my_dict = {'a':500, 'b':58, 'c':56, 'd':40, 'e':100, 'f':20,'g':68}
# a = []
# for i in my_dict:
#     a.append(my_dict[i])
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a) - 1:
#         if a[j] > a[j + 1]:
#             a[j],a[j + 1] = a[j + 1],a[j]
#         j = j + 1
#     i = i + 1
# k = a[-3:]
# print(k)



my_dict = {'a':500, 'b':58, 'c':56, 'd':40, 'e':100, 'f':20,'g':68}
my_list = []
my_list_key = []
for i in range(3):
    max_1 = 0
    for value in my_dict:
        if max_1 < my_dict[value]:
            max_1 = my_dict[value]
            key = value
    my_list.append(max_1)
    my_list_key.append(key)
    my_dict.pop(key)
print(my_list)
print(my_list_key)






# n a completely new, empty dictionary.

# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_values = sorted(dict1.values()) # Sort the values
# sorted_dict = {}

# for i in sorted_values:
#     for k in dict1.keys():
#         if dict1[k] == i:
#             sorted_dict[k] = dict1[k]
#             break

# print(sorted_dict)

# a = {"a":21,"b":3}
# for i in a:
    
#     print(a[i])

    