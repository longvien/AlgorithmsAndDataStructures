package org.mainProgramme;

import org.mainProgramme.Node.DoublyNode;

public class DoublyLinkedList<T> {
    public DoublyNode<T> head = null;
    public DoublyNode<T> tail = null;
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
    // remove a node
    public void remove(T value){
        DoublyNode<T> node = head;

        if (contains(value)) {
            while (node != null) {
                if (node.value.equals(value)) {
                    if (head == node && tail == node) {
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
                }
                node = node.next;
            }
        }
        else {
            System.out.println("Node doesn't exist!");
        }
    }


    public void returnValueHeadToTail() {
        DoublyNode<T> current = head;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }

    public void returnValueTailToHead() {
        DoublyNode<T> current = tail;
        while (current != null) {
            System.out.println(current.value);
            current = current.previous;
        }
    }

    // find value and return node that holds value
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
    // return true / false if the value is in the list
    public boolean contains(T value) {
        return find(value) != null;
    }
}
