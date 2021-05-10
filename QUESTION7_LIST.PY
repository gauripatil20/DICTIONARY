LIST1 = [{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
a=[]
for i in LIST1:
    for j in i:
        b=i[j]
        if b not in a:
            a.append(i[j])
print(a)




# value=set(val for dic in LIST1 for val in dic.values())
# print(value)


