n=int(input())
stack1=[i for i in range(1,n+1)]
stack2=[]
stack3=[]
def hanoi3_1(k):
    if k==1:
        stack1.append(stack3.pop())
        print(stack1,stack2,stack3)
    else:
        hanoi3_1(k-1)
        hanoi1_2(k-1)
        hanoi3_1(1)
        hanoi2_1(k-1)
def hanoi1_3(n):
    if n==1:
        stack3.append(stack1.pop())
        print(stack1,stack2,stack3)
    else:
        hanoi1_2(n-1)
        hanoi1_3(1)
        hanoi2_1(n-1)
        hanoi1_3(n-1)
def hanoi2_1(g):
    if g==1:
        stack1.append(stack2.pop())
        print(stack1,stack2,stack3)
    else:
        hanoi2_1(g-1)
        hanoi1_3(g-1)
        hanoi2_1(1)
        hanoi3_1(g-1)
def hanoi1_2(q):
    if q==1:
        stack2.append(stack1.pop())
        print(stack1,stack2,stack3)
    else:
        hanoi1_3(q-1)
        hanoi1_2(1)
        hanoi3_1(q-1)
        hanoi1_2(q-1)
hanoi1_3(n)

print(stack1,stack2,stack3)
