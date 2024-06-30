**Linked List:**
- In computer science, a linked list is a linear collection of data elementswhose order is not given by the physical placement in memory, isnread, each element point to the next.
- It is a data structure consisting of a collection of nodes which together represent a sequence.
- In its most basic form, each node contains:
    - data, and
    - a reference (or link)
    to the next node in the sequence.

This structure allows for efficient insertion or removal of elements from any position in the sequence during iteration.

**Drawbacks:**
- Access time is linear
- Random access is not feasible
- Arrays have a better [cache locality] (https://en.wikipedia.org/wiki/Locality_of_reference) compared to linked lists

Linked lists are among the simplest and most common data structures. They can be used to implement several other common abstract data types, including:
- lists,
- stacks,
- queues,
- associative arrays,
- subexpressions,
although these data structures can directly be implemented without using linked list basis

Time Complexity:
- Search    -   O(n)
- Insert    -   O(1)
- Delete    -   O(1)