package org.mainProgramme;

public class Node<T> {
    public T Value;
    public Node<T> Next;

    public Node(T Value) {
        this.Value = Value;
        this.Next = null; // defaultly set to null
    }

    public T getValue() {
        return this.Value;
    }

    @Override
    public String toString() {
        return String.valueOf(Value);
    }

}
