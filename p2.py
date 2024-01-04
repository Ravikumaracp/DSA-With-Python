stack=[]
def push_element():
    if len(stack)==n:
        print('stack is full!')
    else:
        element=int(input('enter the element'))
        stack.append(element)
        print(stack)
def pop_element():
    if not stack:
        print('stack is empty')
    else:
        stack.pop()
        print(stack)
n=int(input("enter limit of stack"))
while True:
    print("select the stack operation 1.push 2.pop 3.quit")
    choice=int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print('invalid input1')