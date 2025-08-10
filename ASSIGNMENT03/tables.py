from typing import List, Optional, Union, cast


class LinearProbingTable:
    class Record:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    def __init__(self, capacity=32):
        if capacity <= 0:
            capacity = 1
        self._cap: int = capacity
        # Slot values: None, tombstone sentinel (object), or Record
        self._slots: List[Optional[Union["LinearProbingTable.Record", object]]] = [None for _ in range(capacity)]
        self._size: int = 0
        self._TOMBSTONE: object = object()

    def capacity(self):
        return self._cap

    def __len__(self):
        return self._size

    def _index(self, key):
        return hash(key) % self._cap

    def _find_existing_index(self, key):
        start = idx = self._index(key)
        while True:
            slot = self._slots[idx]
            if slot is None:
                return None
            if slot is not self._TOMBSTONE and isinstance(slot, LinearProbingTable.Record) and slot.key == key:
                return idx
            idx += 1
            if idx == self._cap:
                idx = 0
            if idx == start:
                return None

    def search(self, key):
        idx = self._find_existing_index(key)
        if idx is None:
            return None
        slot = self._slots[idx]
        assert isinstance(slot, LinearProbingTable.Record)
        return slot.value

    def insert(self, key, value):
        # Do not insert duplicates
        existing_idx = self._find_existing_index(key)
        if existing_idx is not None:
            return False

        # Probe for an insertion spot; prefer first tombstone if encountered
        start = idx = self._index(key)
        first_tombstone_idx: Optional[int] = None
        while True:
            slot = self._slots[idx]
            if slot is None:
                target_idx = first_tombstone_idx if first_tombstone_idx is not None else idx
                self._slots[target_idx] = LinearProbingTable.Record(key, value)
                self._size += 1
                # Resize if load factor exceeds 0.7 after insertion
                if (self._size / self._cap) > 0.7:
                    self._rehash(self._cap * 2)
                return True
            elif slot is self._TOMBSTONE:
                if first_tombstone_idx is None:
                    first_tombstone_idx = idx
            # elif occupied with a different key → keep probing
            idx += 1
            if idx == self._cap:
                idx = 0
            if idx == start:
                # Table is effectively full; grow and retry
                self._rehash(self._cap * 2)
                return self.insert(key, value)

    def modify(self, key, value):
        idx = self._find_existing_index(key)
        if idx is None:
            return False
        slot = self._slots[idx]
        assert isinstance(slot, LinearProbingTable.Record)
        slot.value = value
        return True

    def remove(self, key):
        idx = self._find_existing_index(key)
        if idx is None:
            return False
        # Mark as tombstone
        self._slots[idx] = self._TOMBSTONE
        self._size -= 1
        return True

    def _rehash(self, new_capacity):
        if new_capacity <= 0:
            new_capacity = 1
        old_slots = self._slots
        self._cap = new_capacity
        self._slots = [None for _ in range(self._cap)]
        old_size = self._size
        self._size = 0
        for slot in old_slots:
            if slot is not None and slot is not self._TOMBSTONE:
                assert isinstance(slot, LinearProbingTable.Record)
                # Re-insert records without triggering recursive rehashes
                start = idx = hash(slot.key) % self._cap
                first_tombstone_idx: Optional[int] = None
                while True:
                    cur = self._slots[idx]
                    if cur is None:
                        target_idx = first_tombstone_idx if first_tombstone_idx is not None else idx
                        self._slots[target_idx] = LinearProbingTable.Record(slot.key, slot.value)
                        self._size += 1
                        break
                    elif cur is self._TOMBSTONE:
                        if first_tombstone_idx is None:
                            first_tombstone_idx = idx
                    idx += 1
                    if idx == self._cap:
                        idx = 0
        # Sanity: size preserved
        assert self._size == old_size 