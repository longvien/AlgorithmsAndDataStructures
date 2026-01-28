package org.mainProgramme;

public class Main {
    public static void main(String[] args) {
        Node node1 = new Node(10);
        Node node2 = new Node(20);
        Node node3 = new Node(30);

        node1.Next = node2;
        node2.Next = node3;

        while (node1 != null) {
            System.out.println(node1.getValue());
            node1 = node1.Next;
        }

    }
}