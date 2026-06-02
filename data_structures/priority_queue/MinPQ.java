/*
Task: Define MinPQ Interface

Write a Java interface:
    public interface MinPQ<T extends Comparable<T>>

The interface should define these methods:
- void add(T item)
- T getMin()
- T delMin()
- boolean isEmpty()
- int size()

Return rules:
- getMin() returns the smallest item without removing it.
- delMin() returns and removes the smallest item.
- isEmpty() returns true if the priority queue has no items.
- size() returns the number of items.

Example usage:
    MinPQ<Integer> pq;
*/

public interface MinPQ<T extends Comparable<T>> {
    void add(T item);
    T getMin();
    T delMin();
    boolean isEmpty();
    int size();
}