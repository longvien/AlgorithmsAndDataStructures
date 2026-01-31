package org.mainProgramme.Node;

public class SinglyNode<T> {
    public T value;
    public SinglyNode<T> next;

    public SinglyNode(T Value) {
        this.value = Value;
        this.next = null; // defaultly set to null
    }

    public T getValue() {
        return this.value;
    }

    @Override
    public String toString() {
        return String.valueOf(value);
    }

}
