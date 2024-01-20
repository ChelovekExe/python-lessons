f=open('D:\ДОКУМЕНТЫ\Янчугов_Сергей\Git\python-lessons\Perepis.txt','r')
L=[]
for i in f:
    i=i.strip('\n')
    L.append(i)

print(L)

k=0
for i in L:
    L1=i.split('  ')
    print(L1[0])
    L2=L1[3].split('.')
    if int(L2[2])<1978:
        k+=1
print(k)

print()

a=int(input('a'))
b=int(input('b'))
for i in L:
    L1=i.split('  ')
    L2=L1[3].split('.')
    if a<int(L2[2])<b:
        print(L1)