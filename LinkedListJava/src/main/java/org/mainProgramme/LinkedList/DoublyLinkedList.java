package org.mainProgramme.LinkedList;

import org.mainProgramme.Node.DoublyNode;

import java.util.Iterator;

public class DoublyLinkedList<T> implements Iterable<T>{
    public DoublyNode<T> head = null;
    public DoublyNode<T> tail = null;

    public Iterable<T> reverse() {
        return new Iterable<> () { //1st Anonymous class implements Iterable<T>
            @Override
            public Iterator<T> iterator() {
                return new Iterator<>() { //2nd Anonymous class implements Iterator<>
                    DoublyNode<T> current = tail;
                    @Override
                    public boolean hasNext() {
                        return current != null;
                    }
                    @Override
                    public T next() {
                        T value = current.value;
                        current = current.previous;
                        return value;
                    }
                };
            }
        };
    }

    // foreach calls iterator() automatically behind
    public Iterator<T> iterator() {
        return new Iterator<> () { // Anonymous class created
            DoublyNode<T> current = head;
            @Override
            public boolean hasNext() {
                return current != null;
            }
            @Override
            public T next() {
                T value = current.value;
                current = current.next;
                return value;
            }
        };
    }

    // add node to head
    public void addHead(T value) {
        DoublyNode<T> newNode = new DoublyNode<>(value);
        if (head != null) {
            head.previous = newNode;  // lastNode.previous = newNode;
            newNode.next = head; // newNode.next = lastNode;
            head = newNode; // head = newNode;
        }
        else if (head == null && tail == null) {
            head = newNode;
            tail = newNode;
        }
    }

    // add node to tail
    public void addTail(T value) {
        DoublyNode<T> newNode = new DoublyNode<>(value);

        if(tail != null) {
            tail.next = newNode;
            newNode.previous = tail;
            tail = newNode;
        }
        else if (tail == null && head == null) {
            head = newNode;
            tail = newNode;
        }
    }

    // remove a node base on it's value
    public void remove(T value){
        DoublyNode<T> node = head; // assign head to node
        // if value exist in linked list(use contains()):
        if (contains(value)) {
            while (node != null) {
                if (node.value.equals(value)) {
                    if (head == tail) {
                        head = null;
                        tail = null;
                    }
                    else if (node.previous == null){
                        node.next.previous = null;
                        head = node.next;
                        node.next = null;
                    }
                    else if (node.next == null){
                        node.previous.next = null;
                        tail = node.previous;
                        node.previous = null;
                    }
                    else {
                        node.previous.next = node.next;
                        node.next.previous = node.previous;
                        node.next = null;
                        node.previous = null;
                    }
                    break;
                }
                node = node.next;
            }
        }
        else {
            throw new IllegalStateException("Node doesn't exist!");
        }
    }
    // remove head node
    public void removeHead() {
        if (head.next != null) {
            head.next.previous = null;
            head = head.next;
        }
        else {
            head = null;
            tail = null;
        }
    }
    // remove tail node
    public void removeTail() {
        if (tail.previous != null) {
            tail.previous.next = null;
            tail = tail.previous;
        }
        else {
            tail = null;
            head = null;
        }
    }
    // return value in order from head to tail
    public void returnValueHeadToTail() {
        DoublyNode<T> current = head;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }
    // return value in order from tail to head
    public void returnValueTailToHead() {
        DoublyNode<T> current = tail;
        while (current != null) {
            System.out.println(current.value);
            current = current.previous;
        }
    }

    // find value and return node that holds value, if not found, return null
    public DoublyNode<T> find(T value) {
        DoublyNode<T> counter = head;
        while(counter != null) {
            if (counter.value.equals(value)) {
                return counter;
            }
            counter = counter.next;
        }
    return null;
    }

    // return true / false if the there's a node that contains the value. Use find() method
    public boolean contains(T value) {
        return find(value) != null;
    }
}