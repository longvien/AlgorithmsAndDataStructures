package org.mainProgramme.Queue;

public class Stack<T> {
    Deque<T> store = new Deque<>();

    // Push item to Top / Bottom
    public void Push(T item) { store.EnqueueHead(item);}

    // Pop Item out (Pop top)
    public T Pop() { return store.DequeueHead(); }

    // Peek Top Item
    public T Peek() { return store.peekHead(); }

}
