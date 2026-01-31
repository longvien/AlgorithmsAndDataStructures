package org.mainProgramme;

import org.mainProgramme.Node.SinglyNode;
import org.mainProgramme.Node.DoublyNode;

public class Main {
    public static void main(String[] args) {
        SinglyNode<Integer> singlyNode1 = new SinglyNode<>(1);
        SinglyNode<Integer> singlyNode2 = new SinglyNode<>(2);
        SinglyNode<Integer> singlyNode3 = new SinglyNode<>(3);

        singlyNode1.next = singlyNode2;
        singlyNode2.next = singlyNode3;

        while (singlyNode1 != null) {
            System.out.println(singlyNode1.getValue());
            singlyNode1 = singlyNode1.next;
        }

        DoublyNode<Float> doublyNode1 = new DoublyNode<>(1.0f);
        DoublyNode<Float> doublyNode2 = new DoublyNode<>(2.0f);
        DoublyNode<Float> doublyNode3 = new DoublyNode<>(3.0f);

        doublyNode1.next = doublyNode2;
        doublyNode2.previous = doublyNode1;

        doublyNode2.next = doublyNode3;
        doublyNode3.previous = doublyNode2; //
    }


}