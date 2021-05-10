dict1 = {'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
count = 0
for i in dict1:
    if dict1[i]:
        count = count + len(dict1[i])
print(count)


# a = [[[2,3,5]]]
# b = a[0][0][1]
# print(b)