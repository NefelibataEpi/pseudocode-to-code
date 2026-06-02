/*
Task: Implement Binary Heap MinPQ

Implement:
    public class BinaryHeapMinPQ<T extends Comparable<T>>
    implements MinPQ<T>

Requirements:
- Store items in an ArrayList<T>
- index 0 is unused
- add(item) uses swim()
- getMin() returns heap[1]
- delMin():
    1. save heap[1]
    2. swap heap[1] with last item
    3. remove last item
    4. sink(1)
    5. return saved min

Private helper methods:
- swim(int k)
- sink(int k)
- swap(int i, int j)

Return rules:
- If empty:
    getMin() returns null
    delMin() returns null

Example:
add(5)
add(2)
add(7)
add(1)

getMin() -> 1
delMin() -> 1
getMin() -> 2
*/

import java.util.ArrayList;

public class BinaryHeapMinPQ<T extends Comparable<T>> implements MinPQ<T> {
    private ArrayList<T> heap;

    public BinaryHeapMinPQ() {
        heap = new ArrayList<>();
        heap.add(null);
    }

    public void add(T item) {
        heap.add(item);
        swim(heap.size() - 1);
    }

    public T getMin() {
        if (isEmpty()) {
            return null;
        }

        return heap.get(1);
    }

    public T delMin() {
        if (isEmpty()) {
            return null;
        }

        T minItem = heap.get(1);
        swap(1, heap.size() - 1);
        heap.remove(heap.size() - 1);
        sink(1);
        return minItem;
    }

    public boolean isEmpty() {
        return heap.size() == 1;
    }

    public int size() {
        return heap.size() - 1;
    }

    private void swim(int k) {
        while (k > 1 && greater(k/2, k)) {
            swap(k, k/2);
            k = k/2;
        }
    }

    private void sink(int k) {
        while (2*k < heap.size()) {
            int child = 2*k;

            if (child + 1 < heap.size() && greater(child, child + 1)) {
                child++;
            }

            if (!greater(k, child)) {
                break;
            }

            swap(k, child);
            k = child;
        }
    }

    private void swap(int i, int j) {
        T temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }

    private boolean greater(int i, int j) {
        return heap.get(i).compareTo(heap.get(j)) > 0;
    }
}