package org.mainProgramme.Node;

public class DoublyNode<T> {
    public T value;
    public DoublyNode<T> previous;
    public DoublyNode<T> next;

    public DoublyNode(T value) {
        this.value = value;
        this.previous = null;
        this.next = null;
    }
}
