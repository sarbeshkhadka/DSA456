# Analysis of Sorted Linked List Functions

## insert(self, data)
- **Time Complexity:** O(n)
- **Reasoning:** In the worst case, the function must traverse the entire list to find the correct insertion point (when inserting at the end or in the middle). Traversal is linear in the number of nodes, n.

## remove(self, data)
- **Time Complexity:** O(n)
- **Reasoning:** The function may need to traverse the entire list to find and remove all nodes containing the target data. Each node is checked once, so the operation is linear in n.

## is_present(self, data)
- **Time Complexity:** O(n)
- **Reasoning:** The function traverses the list from head to tail, checking each node's data. In the worst case, the data is at the end or not present, requiring n checks.

## __len__(self)
- **Time Complexity:** O(1)
- **Reasoning:** The size of the list is tracked with a variable (`self.size`), so returning the length is a constant-time operation.

---

**Summary Table:**

| Function         | Time Complexity |
|------------------|----------------|
| insert           | O(n)           |
| remove           | O(n)           |
| is_present       | O(n)           |
| __len__          | O(1)           |

**Note:**
- All functions except `__len__` require traversing the list, making them linear in the number of nodes.
- Maintaining a `size` variable allows for constant-time length queries. 