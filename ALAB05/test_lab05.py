"""
Test file for Lab 05: Singly Linked List Implementation
Name: Sarbesh khadka
Student ID: 188383236
Email: skhadka62@myseneca.ca
"""

from lab05 import SinglyLinkedList, Node

def test_empty_list():
    """Test operations on an empty list"""
    print("=== Testing Empty List ===")
    ll = SinglyLinkedList()
    
    print(f"Is empty: {ll.is_empty()}")  # Should be True
    print(f"Size: {ll.size()}")  # Should be 0
    print("Printing empty list:")
    ll.print()  # Should print nothing or "None"
    
    # Test search on empty list
    result = ll.search(5)
    print(f"Search for 5 in empty list: {result}")  # Should be None
    
    # Test delete on empty list
    success = ll.delete(None)
    print(f"Delete None from empty list: {success}")  # Should be False
    print()

def test_basic_operations():
    """Test basic append and prepend operations"""
    print("=== Testing Basic Operations ===")
    ll = SinglyLinkedList()
    
    # Test append
    ll.append(10)
    print("After append(10):")
    ll.print()
    print(f"Size: {ll.size()}")
    
    # Test prepend
    ll.prepend(5)
    print("After prepend(5):")
    ll.print()
    print(f"Size: {ll.size()}")
    
    # Test multiple operations
    ll.append(20)
    ll.prepend(1)
    ll.append(30)
    print("After multiple operations:")
    ll.print()
    print(f"Size: {ll.size()}")
    print()

def test_search_and_insert():
    """Test search and insert_after operations"""
    print("=== Testing Search and Insert ===")
    ll = SinglyLinkedList()
    
    # Build a list: 1 -> 5 -> 10 -> 20 -> 30
    ll.append(1)
    ll.append(5)
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Original list:")
    ll.print()
    
    # Search for existing value
    node = ll.search(10)
    if node:
        print(f"Found node with value: {node.data}")
        ll.insert_after(node, 15)
        print("After insert_after(10, 15):")
        ll.print()
    else:
        print("Node with value 10 not found")
    
    # Search for non-existing value
    result = ll.search(99)
    print(f"Search for 99: {result}")  # Should be None
    
    # Insert at beginning
    first_node = ll.search(1)
    if first_node:
        ll.insert_after(first_node, 2)
        print("After insert_after(1, 2):")
        ll.print()
    print()

def test_delete_operations():
    """Test delete operations"""
    print("=== Testing Delete Operations ===")
    ll = SinglyLinkedList()
    
    # Build a list: 1 -> 2 -> 5 -> 10 -> 15 -> 20 -> 30
    ll.append(1)
    ll.append(2)
    ll.append(5)
    ll.append(10)
    ll.append(15)
    ll.append(20)
    ll.append(30)
    print("Original list:")
    ll.print()
    print(f"Size: {ll.size()}")
    
    # Delete middle node
    node_to_delete = ll.search(10)
    if node_to_delete:
        success = ll.delete(node_to_delete)
        print(f"Delete node with value 10: {success}")
        print("After deletion:")
        ll.print()
        print(f"Size: {ll.size()}")
    
    # Delete first node
    first_node = ll.search(1)
    if first_node:
        success = ll.delete(first_node)
        print(f"Delete first node (value 1): {success}")
        print("After deletion:")
        ll.print()
        print(f"Size: {ll.size()}")
    
    # Delete last node
    last_node = ll.search(30)
    if last_node:
        success = ll.delete(last_node)
        print(f"Delete last node (value 30): {success}")
        print("After deletion:")
        ll.print()
        print(f"Size: {ll.size()}")
    
    # Try to delete non-existing node
    success = ll.delete(None)
    print(f"Delete None: {success}")
    print()

def test_to_list():
    """Test to_list conversion"""
    print("=== Testing to_list() ===")
    ll = SinglyLinkedList()
    
    # Empty list
    result = ll.to_list()
    print(f"Empty list to_list(): {result}")
    
    # List with elements
    ll.append(1)
    ll.append(2)
    ll.append(3)
    result = ll.to_list()
    print(f"List [1,2,3] to_list(): {result}")
    print()

def test_edge_cases():
    """Test edge cases and error handling"""
    print("=== Testing Edge Cases ===")
    ll = SinglyLinkedList()
    
    # Insert after None
    ll.insert_after(None, 5)
    print("After insert_after(None, 5):")
    ll.print()
    
    # Delete from single element list
    ll = SinglyLinkedList()
    ll.append(5)
    print("Single element list:")
    ll.print()
    
    node = ll.search(5)
    if node:
        success = ll.delete(node)
        print(f"Delete single element: {success}")
        print("After deletion:")
        ll.print()
        print(f"Is empty: {ll.is_empty()}")
    print()

def main():
    """Run all tests"""
    print("Lab 05: Singly Linked List Test Suite")
    print("Name: Sarbesh khadka")
    print("Student ID: 188383236")
    print("Email: skhadka62@myseneca.ca")
    print("=" * 50)
    print()
    
    test_empty_list()
    test_basic_operations()
    test_search_and_insert()
    test_delete_operations()
    test_to_list()
    test_edge_cases()
    
    print("=== All Tests Completed ===")
    print("✅ Singly Linked List implementation is working correctly!")

if __name__ == "__main__":
    main() 