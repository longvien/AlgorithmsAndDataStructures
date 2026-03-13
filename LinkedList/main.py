from LinkedList.SortedLinkedList import sortedLinkedList
from LinkedList.DoublyLinkedList import DoublyLinkedList

def main():
    mySTL = sortedLinkedList()
    mySTL.add(2)
    mySTL.add(1)
    mySTL.add(3)
    mySTL.add(5)
    mySTL.add(4)
    mySTL.add(5)
    mySTL.display()
    myDLL = DoublyLinkedList()
    myDLL.addHead(4)
    myDLL.addHead(3)
    myDLL.addHead(2)
    myDLL.addHead(1)
    myDLL.addTail(5)
    myDLL.remove(2)
    myDLL.returnValueHeadToTail()
main()
