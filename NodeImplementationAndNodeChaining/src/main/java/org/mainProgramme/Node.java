package org.mainProgramme;

public class Node {
    public int Value;
    public Node Next;

    public Node(int Value) {
        this.Value = Value;
        this.Next = null; // defaultly set to null
    }

    public int getValue() {
        return this.Value;
    }

    @Override
    public String toString() {
        return String.valueOf(Value);
    }

}
