### Part A — Analysis of `SortedTable` member functions

Below, n denotes the number of Records currently stored in the table.

- **Data representation**: `self.the_table` is a Python list of capacity `self.cap` that stores zero or more `Record` objects at the front, followed by `None` values.

#### insert(self, key, value)
- Steps:
  - Calls `search(key)` to check duplicates.
  - Grows the table by doubling when `len(self) == self.cap`.
  - Appends the new `Record` at index `len(self)`.
  - Re-sorts the entire occupied prefix using bubble sort.
- Complexity:
  - `search(key)`: O(n) (see below) + calls `__len__` once (O(n)). Overall still O(n).
  - Potential grow-and-copy when full: O(n) to copy existing occupied portion (code copies `cap` elements; effectively Θ(n)).
  - Bubble sort on `size = n + 1` elements: O(n^2).
  - Dominant term: O(n^2) per insertion (amortized; resizing is less significant than the sort).

#### modify(self, key, value)
- Implementation uses `while (i < len(self) and ...): i += 1`.
- Inefficiency: `len(self)` is recomputed every loop iteration and itself scans the entire table.
- Complexity:
  - In the worst case, up to n iterations, each with `__len__` = O(n) → O(n^2).

#### remove(self, key)
- Steps:
  - Computes `size = len(self)` once.
  - Linear scan to find matching key: O(n).
  - Shifts all subsequent elements left by one: O(n).
- Complexity: O(n).

#### search(self, key)
- Steps:
  - Computes `size = len(self)` once (O(n)).
  - Linear search up to `size`: O(n).
- Complexity: O(n).

#### capacity(self)
- Returns `self.cap`.
- Complexity: O(1).

#### __len__(self)
- Loops across the entire underlying list and counts non-None.
- Complexity: O(n) with respect to number of occupied cells; practically it traverses capacity, which is Θ(n) after growth. In the worst case (when capacity >> n), the work is closer to O(capacity).

### Key inefficiencies and why
- **Repeated full scans for length**: `__len__` is O(n) and is called inside loops (notably in `modify`), inflating cost to O(n^2).
- **Insertion sort via bubble sort of entire prefix**: Every insert sorts all elements, making insert O(n^2) instead of O(n) (shift-only) or O(log n) + O(n) with binary search + shift.
- **Linear search despite sorted invariant**: `search`, `modify`, and `remove` all do linear scans even though the array is kept sorted. They could use binary search in O(log n).
- **Growth copying entire capacity range**: On grow, the code copies `cap` entries including trailing `None`s. Copying only the occupied n items would be sufficient.

### How to make it significantly more efficient
- **Track size explicitly**: Maintain `self.size` that increments/decrements on insert/remove. Then:
  - `__len__`: O(1).
  - Remove repeated calls to `len(self)` inside loop conditions.
- **Binary search for lookups**: Since the table is sorted by key, use binary search to find the index in O(log n) for `search`, `modify`, and to locate the insertion/removal position.
- **Insertion by shift, not re-sort**:
  - Find insertion index by binary search in O(log n).
  - Shift the suffix right by one and place the new element: O(n) shift, total O(n).
  - Avoid bubble sort entirely.
- **Remove by shift-left**: Find index by binary search O(log n), then shift left O(n), total O(n).
- **Optimize growth copying**: When resizing, allocate the new list and copy only the first `self.size` occupied elements.

### Resulting target complexities (with the above improvements)
- `insert`: O(n) (binary search O(log n) + shift O(n)).
- `modify`: O(log n) to find via binary search, then O(1) to update.
- `remove`: O(n) (binary search O(log n) + shift O(n)).
- `search`: O(log n).
- `capacity`: O(1).
- `__len__`: O(1) with a maintained `self.size` counter. 