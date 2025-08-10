from tables import LinearProbingTable


def expect(condition, message):
    if not condition:
        raise AssertionError(message)


def test_linear_probing_basic():
    t = LinearProbingTable(capacity=4)

    # Insert & search
    expect(t.insert("a", 1) is True, "insert a")
    expect(t.insert("b", 2) is True, "insert b")
    expect(t.search("a") == 1, "search a")
    expect(t.search("b") == 2, "search b")

    # Duplicate insert
    expect(t.insert("a", 10) is False, "duplicate a not inserted")

    # Modify
    expect(t.modify("a", 100) is True, "modify a")
    expect(t.search("a") == 100, "search a after modify")
    expect(t.modify("z", 9) is False, "modify non-existent")

    # Remove uses tombstone
    expect(t.remove("a") is True, "remove a")
    expect(t.search("a") is None, "a gone")

    # Ensure probing continues past tombstones
    # Create a cluster: force collisions by using multiple keys
    keys = ["x1", "x2", "x3", "x4"]
    for i, k in enumerate(keys):
        expect(t.insert(k, i) is True, f"insert {k}")
    # This should have triggered a resize: cap 4, after 3rd insert load 0.75 > 0.7
    expect(t.capacity() == 8, "linear probing capacity doubled to 8")

    # Find an existing key after tombstone and wrap-around
    expect(t.search("x3") == 2, "search x3")

    # Remove and re-insert to reuse tombstone slot
    expect(t.remove("x2") is True, "remove x2")
    expect(t.insert("x2", 22) is True, "reinsert x2 uses tombstone/space")
    expect(t.search("x2") == 22, "x2 updated value")


if __name__ == "__main__":
    test_linear_probing_basic()
    print("All tests passed.") 