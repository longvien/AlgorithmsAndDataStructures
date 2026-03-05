from queue import Queue
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
if __name__ == "__main__":
    main()  #execute when file is run directly, not when imported ad a module