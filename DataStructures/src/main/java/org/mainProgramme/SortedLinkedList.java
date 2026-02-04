package org.mainProgramme;

import org.mainProgramme.Node.SortedNode;

public class SortedLinkedList<T extends Comparable<T>> {
    public SortedNode<T> head = null;
    public SortedNode<T> tail = null;

    public void add(T value) {
        SortedNode<T> newNode = new SortedNode<>(value);
        SortedNode<T> current = head;
        if (head == null) {
            head = newNode;
            tail = newNode;
        }
        else if (newNode.value.compareTo(head.value) <= 0) {
            newNode.next = head;
            head.previous = newNode;
            head = newNode;
        }
        else if (newNode.value.compareTo(tail.value) >= 0) {
            newNode.previous = tail;
            tail.next = newNode;
            tail = newNode;
        }
        else {
            while (current != null) {
                if (newNode.value.compareTo(current.value) > 0) {
                    current = current.next;
                    if (newNode.value.compareTo(current.value) < 0) {
                        newNode.next = current;
                        newNode.previous = current.previous;
                        current.previous.next = newNode;
                        current.previous = newNode;
                    }
                }
            }
        }
    }

    public void displayValue() {
        SortedNode<T> current = head;
        while (current != null) {
            System.out.println(current.value);
            current = current.next;
        }
    }
}
