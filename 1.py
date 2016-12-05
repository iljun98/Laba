n=int(input())
A=input()
k=int(input())
def magic(n,A,k):
    c=len(A)-1
    tmp=0
    fin=[]
    for elem in A:
        if elem.isdigit():
            tmp+=int(elem)*n**c
        else:
            tmp+=(ord(elem)-55)*n**c
        c-=1
    while tmp>=1:
        fin.append(tmp%k)
        tmp=tmp//k
    fin.reverse()
    for i in range(len(fin)):
        if fin[i]>9:
            fin[i]=chr(fin[i]+55)
        else:
            fin[i]=str(fin[i])
    print(''.join(fin))
magic(n,A,k)