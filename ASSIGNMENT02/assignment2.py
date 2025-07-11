import graphviz

class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None
        self.prev: 'Node | None' = None

class SortedLinkedList:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def insert(self, data: int):
        new_node = Node(data)
        if not self.head:  # Empty list
            self.head = self.tail = new_node
        elif data <= self.head.data:  # Insert at front
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif self.tail and data >= self.tail.data:  # Insert at end
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:  # Insert in middle
            current = self.head
            while current and current.data < data:
                current = current.next
            if current:
                prev_node = current.prev
                if prev_node:
                    prev_node.next = new_node
                    new_node.prev = prev_node
                new_node.next = current
                current.prev = new_node
        self.size += 1

    def remove(self, data):
        current = self.head
        removed = False
        while current:
            if current.data == data:
                removed = True
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.size -= 1
                temp = current.next
                del current
                current = temp
            else:
                current = current.next
        return removed

    def is_present(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def visualize(self, filename):
        dot = graphviz.Digraph(format='png')
        dot.attr(rankdir='LR')
        current = self.head
        idx = 0
        node_names = []
        while current:
            node_name = f"node{idx}"
            node_names.append(node_name)
            dot.node(node_name, str(current.data))
            current = current.next
            idx += 1
        # Add edges for next and prev
        for i in range(len(node_names) - 1):
            dot.edge(node_names[i], node_names[i+1], label='next')
            dot.edge(node_names[i+1], node_names[i], label='prev')
        dot.render(filename, cleanup=True)

if __name__ == "__main__":
    sll = SortedLinkedList()
    print("Inserting: 5, 3, 7, 1, 4")
    for value in [5, 3, 7, 1, 4]:
        sll.insert(value)
        print("List:", list(sll))
        sll.visualize(f"insert_{value}")
    print("Remove 3:", sll.remove(3))
    print("List:", list(sll))
    sll.visualize("remove_3")
    print("Remove 10 (not present):", sll.remove(10))
    print("List:", list(sll))
    sll.visualize("remove_10")
    print("Is 4 present?", sll.is_present(4))
    print("Is 10 present?", sll.is_present(10))
    print("Length:", len(sll)) 