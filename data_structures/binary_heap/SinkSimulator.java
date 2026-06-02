/*
Task: Implement Sink Simulation

Requirements:
1. Store integers in an ArrayList<Integer>
2. Assume index 0 is unused
3. Implement:
    - void sink(int k)
    - void swap(int i, int j)

Behavior:
- sink(k) repeatedly compares heap[k] with its children.
- If heap[k] is larger than the smaller child, swap them.
- Continue until heap property is restored.

Initial heap:
    [-, 9, 2, 7, 5, 6]

After sink(1):
    [-, 2, 5, 7, 9, 6]

Rules:
- If a node has two children, compare with the smaller child.
- If a node has only left child, compare with left child.
- Stop when heap[k] <= smaller child.
*/

import java.util.ArrayList;

public class SinkSimulator {
    private ArrayList<Integer> heap;

    public SinkSimulator() {
        heap = new ArrayList<>();
        heap.add(null);
    }

    public void sink(int k) {
        while (2*k < heap.size()) {
            int child = 2*k;

            if (child + 1 < heap.size() && heap.get(child) > heap.get(child + 1)) {
                child++;
            }

            if (heap.get(k) <= heap.get(child)) {
                break;
            }

            swap(k, child);
            k = child;
        }
    }

    private void swap(int i, int j) {
        int temp = heap.get(i);
        heap.set(i, heap.get(j));
        heap.set(j, temp);
    }
}
