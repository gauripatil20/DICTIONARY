i=1
dict1=[]
while i <=10:
    NUM = input("ENTER THE STUDENT :")
    NUM1 = int(input("ENTER THE MARKS :"))
    i=i+1
    A = (NUM,NUM1)
    dict1.append(A)
dict2={}
dict2.update(dict1)
print(dict2)