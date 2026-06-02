/*
Task: Implement Heap Index Helpers

Write a class that implements these methods:

- int parent(int k)
- int leftChild(int k)
- int rightChild(int k)

Rules:
- parent(k) returns k / 2
- leftChild(k) returns 2 * k
- rightChild(k) returns 2 * k + 1

Example:
parent(6) -> 3
leftChild(3) -> 6
rightChild(3) -> 7
*/

public class HeapIndexHelper {

    public int parent(int k) {
        return k / 2;
    }

    public int leftChild(int k) {
        return 2 * k;
    }

    public int rightChild(int k) {
        return 2 * k + 1;
    }
}
