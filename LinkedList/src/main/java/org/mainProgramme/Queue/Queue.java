package org.mainProgramme.Queue;

public class Queue<T> {
    Deque<T> store = new Deque<>();

    //Enqueue an item
    public void Enqueue(T value) { store.EnqueueTail(value); }

    //Dequeue an item
    public T Dequeue() { return store.DequeueHead(); }

    //Peek an item(head)
    public T peek() { return store.peekHead(); }

}