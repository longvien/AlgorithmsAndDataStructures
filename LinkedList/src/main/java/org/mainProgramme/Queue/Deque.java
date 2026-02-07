package org.mainProgramme.Queue;

import org.mainProgramme.LinkedList.DoublyLinkedList;
import org.mainProgramme.Node.DoublyNode;

import java.util.Iterator;

public class Deque<T> implements Iterable<T>{
    DoublyLinkedList<T> store = new DoublyLinkedList<>(); // Uses a DoublyLinkedList as it's data stores.

    // Enqueue Head
    public void EnqueueHead(T value){
        store.addHead(value);
    }

    // Enqueue Tail
    public void EnqueueTail(T value) {
        store.addTail(value);
    }

    // Deque Head and return head.value
    public T DequeueHead() {
        if (store.head != null) {
            T value = store.head.value;
            store.removeHead();
            return value;
        }
        else {
            throw new IllegalStateException("Deque is empty!");
        }
    }

    // Deque Tail and return tail.value
    public T DequeueTail() {
        if (store.tail != null) {
            T value = store.tail.value;
            store.removeTail();
            return value;
        }
        else {
            throw new IllegalStateException("Deque is empty!");
        }

    }

    // return head without dequeing it
    public T peekHead() {
        if (store.head != null) {
            return store.head.value;
        }
        else {
            throw new IllegalStateException("Deque is empty");
        }
    }

    // return tail without dequeing it
    public T peekTail(){
        if (store.tail != null) {
            return store.tail.value;
        }
        else {
            throw new IllegalStateException("Deque is empty");
        }
    }

    // iterator() for foreach loop
    public Iterator<T> iterator(){
        return new Iterator<>() {
            DoublyNode<T> current = store.head;
            @Override
            public boolean hasNext() { return current != null; }
            @Override
            public T next() {
                T value =  current.value;
                current = current.next;
                return value;
            }
        };
    }
}
