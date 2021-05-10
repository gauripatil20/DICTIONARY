# MY_DICT = {"bijender":4,"manish":1,"deepak":60,"param":20,"anjili":30,"roshini":50}
# DICT = {}
# for i in MY_DICT:
#     s = MY_DICT[i]
#     for j in MY_DICT:
#         a = MY_DICT[j]
#         if s < a:
#             DICT[j] = a
# for i in MY_DICT:
#     s = MY_DICT[i]
#     for j in MY_DICT:
#         a = MY_DICT[j]
#         if s > a:
#             DICT[j] = a
# print(DICT)

# MY_DICT = {"bijender":4,"manish":20,"deepak":60,"param":1,"anjili":30,"roshini":50}
# DICT = {}
# for i in MY_DICT:
#     s = MY_DICT[i]
#     for j in MY_DICT:
#         a = MY_DICT[j]
#         if s > a:
#             DICT[j] = a
# for i in MY_DICT:
#     s = MY_DICT[i]
#     for j in MY_DICT:
#         a = MY_DICT[j]
#         if s < a:
#             DICT[j] = a
# print(DICT)

# my_dict = {"bijender":45,"deepak":60,"param":20,"anjili":30,"roshini":50,"roshni":23}
# new_dict = {}
# lenght = len(my_dict)
# print(lenght)
# for i in range(lenght):
#     max_1 = 0
#     for value in my_dict:
#         if max_1 < my_dict[value]:
#             max_1 = my_dict[value]
#             key = value
#     new_dict.update({key:max_1})
#     my_dict.pop(key)
# print(new_dict)