/*
Task: Implement Unordered Array MinPQ

Implement:
    public class ArrayMinPQ<T extends Comparable<T>>
    implements MinPQ<T>

Functionalities:
- Store items in an ArrayList
- add() should simply append item
- getMin() should scan the whole array
- delMin() should:
    1. find the smallest item
    2. remove it
    3. return it

Return rules:
- If the queue is empty:
    getMin() returns null
    delMin() returns null

Example:
Input:
    add(5)
    add(2)
    add(8)

getMin() -> 2
delMin() -> 2
size() -> 2
*/

import java.util.ArrayList;

public class ArrayMinPQ<T extends Comparable<T>> implements MinPQ<T> {
    private ArrayList<T> items;

    public ArrayMinPQ() {
        items = new ArrayList<>();
    }

    public void add(T item) {
        // append item
        items.add(item);
    }

    public T getMin() {
        // if empty, return null
        // scan all items and find smallest
        if (items.isEmpty()) {
            return null;
        }

        return items.get(getMinIndex());
    }

    public T delMin() {
        // if empty, return null
        // find index of smallest item
        // remove it and return it
        if (items.isEmpty()) {
            return null;
        }

        int minIndex = getMinIndex();
        T item = items.get(minIndex);
        items.remove(minIndex);
        return item;
    }

    public boolean isEmpty() {
        // return whether items is empty
        return items.isEmpty();
    }

    public int size() {
        // return number of items
        return items.size();
    }

    private int getMinIndex() {
        int minNumIndex = 0;

        for (int i = 0; i < items.size(); i++) {
            if (items.get(i).compareTo(items.get(minNumIndex)) < 0) {
                minNumIndex = i;
            }
        }

        return minNumIndex;
    }
}
