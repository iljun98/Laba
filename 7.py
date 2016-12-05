n=int(input())
stack1=[i for i in range(n,0,-1)]
stack2=[]
stack3=[]
def hanoi(n):
    if n==1:
        if not stack3 or stack1[-1] < stack3[-1]:stack3.append(stack1.pop())
        print(stack1,stack2,stack3)
    else:
        if not stack2 or stack1[-1] < stack2[-1]:stack2.append(stack1.pop())
        print(stack1, stack2, stack3)
        hanoi(n-1)
        if not stack1 or stack2[-1] < stack1[-1]:stack1.append(stack2.pop())
        print(stack1, stack2, stack3)
        hanoi(n-1)
hanoi(n)