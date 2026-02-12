package org.main;

public class Main {
    public static void main(String[] args) {
    BTreeNode<String> root = new BTreeNode<>("root");
    BTreeNode<String> left = new BTreeNode<>("left");
    BTreeNode<String> right = new BTreeNode<>("right");

    root.left = left;
    root.right = right;
    System.out.println(root.left.value);
    }
}