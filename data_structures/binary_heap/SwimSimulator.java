/*
Task: Implement Swim Simulation

Requirements:

1. Store integers in an ArrayList<Integer>
2. Assume index 0 is unused (put a dummy value at index 0)
3. Implement:
    - void add(int x)
    - void swim(int k)
    - void swap(int i, int j)

Behavior:
- add(x):
    1. append x to the end
    2. call swim()

- swim(k):
    repeatedly swap child with parent
    while parent is greater

Example:

add(5)
heap = [-, 5]

add(2)
heap = [-, 2, 5]

add(7)
heap = [-, 2, 5, 7]

add(1)
heap = [-, 1, 2, 7, 5]
*/

import java.util.ArrayList;

public class SwimSimulator {
    private ArrayList<Integer> heap;

    public SwimSimulator() {
        heap = new ArrayList<>();
        heap.add(null);
    }

    public void add(int x) {
        heap.add(x);
        swim(heap.size() - 1);
    }

    private void swim(int k) {
        while (k > 1 && heap.get(k/2) > heap.get(k)) {
            swap(k, k/2);
            k = k/2;
        }
    }

    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }
}
