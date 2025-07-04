"""
Lab 05: Singly Linked List Implementation
Name: Sarbesh khadka
Student ID: 188383236
Email: skhadka62@myseneca.ca
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def prepend(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.count += 1

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_after(self, target, data):
        if target is None:
            return
        new_node = Node(data, target.next)
        target.next = new_node
        self.count += 1

    def delete(self, target):
        if self.is_empty() or target is None:
            return False
        if target == self.head:
            self.head = self.head.next
            self.count -= 1
            return True
        current = self.head
        while current.next:
            if current.next == target:
                current.next = target.next
                self.count -= 1
                return True
            current = current.next
        return False

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def size(self):
        return self.count

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def print(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
