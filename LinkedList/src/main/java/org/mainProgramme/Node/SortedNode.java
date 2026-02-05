package org.mainProgramme.Node;

public class SortedNode<T> {
    public T value;
    public SortedNode<T> next;
    public SortedNode<T> previous;

    public SortedNode(T value) {
        this.value = value;
        this.next = null;
        this.previous = null;
    }
}
