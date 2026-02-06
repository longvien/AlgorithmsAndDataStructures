package org.mainProgramme;

import org.mainProgramme.Node.SinglyNode;
import org.mainProgramme.Node.DoublyNode;

public class Main {
    public static void main(String[] args) {
        // Create single nodes
        SinglyNode<Integer> singlyNode1 = new SinglyNode<>(1);
        SinglyNode<Integer> singlyNode2 = new SinglyNode<>(2);
        SinglyNode<Integer> singlyNode3 = new SinglyNode<>(3);
        // [1] -> [2] -> [3]
        // Set next for single nodes
        singlyNode1.next = singlyNode2;
        singlyNode2.next = singlyNode3;

        // Print out all single nodes
        while (singlyNode1 != null) {
            System.out.println(singlyNode1.getValue());
            singlyNode1 = singlyNode1.next;
        }
        // Create a doubly node
        DoublyNode<Float> doublyNode1 = new DoublyNode<>(1.0f);
        DoublyNode<Float> doublyNode2 = new DoublyNode<>(2.0f);
        DoublyNode<Float> doublyNode3 = new DoublyNode<>(3.0f);
        // [1] <-> [2] <-> [3]
        doublyNode1.next = doublyNode2;
        doublyNode2.previous = doublyNode1;

        doublyNode2.next = doublyNode3;
        doublyNode3.previous = doublyNode2;

        // using LinkedList
        DoublyLinkedList<Integer> dll = new DoublyLinkedList<>();
        dll.addHead(100);
        dll.addHead(200);
        dll.addHead(300);
        dll.returnValueHeadToTail();
        dll.addTail(50);
        dll.remove(100);
        dll.returnValueTailToHead();

        // head -> [300] <-> ([200] <-> is removed) [100] <-> [50] <- tail
        System.out.println(dll.contains(100));

        for (int value : dll) {
            System.out.println(value);
        } // foreach runs iterator secretly behind
        for (int value : dll.reverse()) {
            System.out.println(value);
        }


        //SortedList
        System.out.println("SortedList");
        SortedLinkedList<Integer> sll = new SortedLinkedList<>();
        sll.add(6);
        sll.add(6);
        sll.add(5);
        sll.add(2);
        sll.displayValue();
    }
}