# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3} 
# dic1={}
# dic1.update(dic)
# print(dic1)

dic_values = {"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
dic1 = []
num = dict()
for key, val in dic_values.items():
    if val not in dic1:
        dic1.append(val)
        num[key]= val
print("The dictionary after values removal : " + str(num))
