queue=[]
def enqueue():
    if len(queue)==n:
        print('stack is over flow')
    else:
        element=int(input('enter the element:'))
        queue.append(element)
        print(element,' is added into a queue')
def dequeue():
    if not queue:
        print('queue is empty')
    else:
        e=queue.pop(0)
        print('removed element id ',e)
def display():
    print(queue)
n=int(input('enter queue limit:'))
while True:
    print("select the operation 1.enqueue 2.dequeue 3.show 4.quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print('invalid input!')