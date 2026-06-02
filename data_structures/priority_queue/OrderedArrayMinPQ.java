/*
Task: Implement Ordered Array MinPQ

Implement:
    public class OrderedArrayMinPQ<T extends Comparable<T>>
    implements MinPQ<T>

Functionalities:
- Store items in an ArrayList
- Keep the ArrayList sorted in ascending order
- add() should insert the new item into the correct position
- getMin() should return the first item
- delMin() should remove and return the first item

Return rules:
- If the queue is empty:
    getMin() returns null
    delMin() returns null

Example:
Input:
    add(5)
    add(2)
    add(8)
    add(1)

Internal array:
    [1, 2, 5, 8]

getMin() -> 1
delMin() -> 1
size() -> 3
*/

import java.util.ArrayList;

public class OrderedArrayMinPQ<T extends Comparable<T>> implements MinPQ<T> {
    private ArrayList<T> items;

    public OrderedArrayMinPQ() {
        items = new ArrayList<>();
    }

    public void add(T item) {
        int pos = 0;

        while (pos < items.size() && items.get(pos).compareTo(item) <= 0) {
            pos++;
        }

        items.add(pos, item);
    }

    public T getMin() {
        if (items.isEmpty()) {
            return null;
        }

        return items.get(0);
    }

    public T delMin() {
        if (items.isEmpty()) {
            return null;
        }

        T item = items.get(0);
        items.remove(0);
        return item;
    }

    public boolean isEmpty() {
        return items.isEmpty();
    }

    public int size() {
        return items.size();
    }
}
