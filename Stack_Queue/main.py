from queue import Queue
from stack import Stack
def main():
    myQueue = Queue()
    myQueue.enqueue(5)
    myQueue.enqueue(4)
    myQueue.enqueue(3)
    myQueue.enqueue(2)
    myQueue.enqueue(1)
    for i in range(5):
        myQueue.dequeue()
    print(myQueue.peek())
    myStack = Stack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    myStack.push(5)
    for i in range(1):
        myStack.pop()
    print(myStack.peek())

if __name__ == "__main__":
    main()  #execute when file is run directly, not when imported ad a module