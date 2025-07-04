# Lab 05: Singly Linked List in Python

## Classes and Methods

### Node
- `data`: The value stored in the node.
- `next`: Reference to the next node in the list.

### SinglyLinkedList
- `__init__()`: Initializes an empty list.
- `is_empty()`: Checks if the list is empty.
- `prepend(data)`: Inserts a new node at the beginning.
- `append(data)`: Inserts a new node at the end.
- `insert_after(target, data)`: Inserts a new node after the given node.
- `delete(target)`: Deletes the specified node.
- `search(data)`: Searches for a node by value.
- `size()`: Returns the number of nodes.
- `to_list()`: Returns a Python list of all node values.
- `print()`: Prints the list contents.

## Big-O Analysis
| Method         | Time Complexity |
| -------------- | -------------- |
| `__init__`     | O(1)           |
| `is_empty`     | O(1)           |
| `prepend`      | O(1)           |
| `append`       | O(n)           |
| `insert_after` | O(1)           |
| `delete`       | O(n)           |
| `search`       | O(n)           |
| `size`         | O(n)           |
| `to_list`      | O(n)           |
| `print`        | O(n)           |

- n = number of nodes in the list.
- Operations that require traversal (append, delete, search, size, to_list, print) are O(n).
- Operations at the head or with a given node are O(1). 