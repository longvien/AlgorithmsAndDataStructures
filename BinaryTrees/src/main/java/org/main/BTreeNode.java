package org.main;

public class BTreeNode<T> {
    public T value;
    public BTreeNode<T> left = null;
    public BTreeNode<T> right = null;

    public BTreeNode(T value) {
        this.value = value;
    }
}
