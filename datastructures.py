"""
Data Structures Implementation Module
==================================================
Implements three fundamental data structures: Stack, Queue, and Linked List.
Each structure includes detailed documentation and operation tracking for
educational purposes.

Author: Kaitlyn McCormick
Course: CSC506 - Design and Analysis of Algorithms
Module: 1 - Data Structures and Algorithm Complexity
"""

from typing import Any, Optional, Generator
from dataclasses import dataclass

# ======================================================
# LINKED LIST IMPLEMENTATION

# ======================================================

@dataclass
class Node:
    """
    Node class for Linked List implementation.
    
    Attributes:
       data: The value stored in the node
       next: Reference to the next node in the list
    """
    data: Any
    next: Optional['Node'] = None
    
class LinkedList:
    """
    Singly Linked List Implementation
    
    A linear data structure where elements are stored in nodes, and each node
    points to the next node in the sequence. Unlike arrays, linked lists don't 
    require contiguous memory allocation.
    
    Time Complexity:
       - Insert at head: 0(1)
       - Insert at tail: 0(n) without tail pointer, 0(1) with tail pointer
       - Delete: 0(n) - must traverse to find element
       - Search: 0(n) - linear traversal required
       - Access by index: 0(n) - no random access
    
    Space Complexity: 0(n) where n is the number of elements
    
    Use Cases:
       - When frequent insertions/deletions at the beginning are needed
       - When memory allocation needs to be dynamic
       - Implementing other data structures (stacks, queues, hash table chaining)
       - When you don't know the size of data in advance
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
        self.operations_log: list = []
    
    def _log_operation(self, operation: str, details: str = ""):
        """Log operation for educational tracking."""
        self.operations_log.append({
            'operation': operation,
            'details': details,
            'size_after': self._size
        })
    
    def insert_at_head(self, data: Any) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Time Complexity: 0(1) - constant time regardless of list size
        
        Arguments: 
           data: Value to insert
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1
        self._log_operation("insert_at_head", f"Inserted {data}")
    
    def insert_at_tail(self, data: Any) -> None:
        """
        Insert a new node at the end of the list.
        
        Time Complexity: 0(1) with tail pointer (our implementation)
                         0(n) without tail pointer
        Arguments:
           data: Value to insert
        """
        new_node = Node(data)
        
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
        self._log_operation("insert_at_tail", f"Inserted {data}")
    
    def insert_at_position(self, data: Any, position: int) -> bool:
        """
        Insert a new node at a specific position.
        
        Time Complexity: 0(n) - must traverse to position
        
        Arguments: 
           data: Value to insert
           position: Index where to insert (0-based)
        
        Returns:
           True if successful, False if position is invalid
        """
        if position < 0 or position > self._size:
            return False
        
        if position == 0:
            self.insert_at_head(data)
            return True
        
        if position == self._size:
            self.insert_at_tail(data)
            return True
        
        new_node = Node(data)
        current = self.head
        
        # Traverse to position - 1
        for _ in range(position - 1):
            current = current.next
            
        new_node.next = current.next
        current.next = new_node
        self._size += 1
        self._log_operation("insert_at_position", f"Inserted {data} at position {position}")
        return True
    
    def delete(self, data: Any) -> bool:
        """
        Delete the first occurrence of a value from the list.
        
        Time Complexity: 0(n) - must search for element
        
        Arguments: 
           data: Value to delete
        
        Returns: 
           True if element was found and deleted, False otherwise
        """
        if self.head is None:
            return False
        
        # Special case: delete head
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            self._log_operation("delete", f"Deleted {data} from head")
            return True
        
        #Search for element
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self._size -= 1
                self._log_operation("delete", f"Deleted {data}")
                return True
            current = current.next
        
        return False
    
    def search(self, data: Any) -> int:
        """
        Search for an element and return its position.
        
        Time Complexity: 0(n) - linear search required
        
        Arguments:
           data: Value to search for
           
        Returns: 
           Index of element if found, -1 otherwise
        """
        current = self.head
        index = 0
        comparisons = 0
        
        while current is not None:
            comparisons += 1
            if current.data == data:
                self._log_operation("search", f"Found {data} at index {index} after {comparisons} comparisons")
                return index
            current = current.next
            index += 1
        
        self._log_operation("search", f"Element {data} not found after {comparisons} comparisons")
        return -1
    
    def get(self, index: int) -> Optional[Any]:
        """
        Access element at a specific index.
        
        Time Complexity: 0(n) - no random access
        
        Arguments: 
           index: POsition to access
           
        Returns: 
           Value at index if valid, None otherwise
        """
        if index < 0 or index >= self._size:
            return None
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        return current.data
    
    def __len__(self) -> int:
        """Return the size of the list."""
        return self._size
    
    def __iter__(self) -> Generator[Any, None, None]:
        """Iterate through list elements."""
        current = self.head
        while current is not None:
            yield current.data
            current = current.next
    
    def to_list(self) -> list:
        """Convert linked list to Python list for display."""
        return list(self)
    
    def display(self) -> str:
        """Return string representation of the list."""
        if self.head is None:
            return "Empty List"
        return " -> ".join(str(item) for item in self) + " -> None"
    
    
# ======================================================
#STACK IMPLEMENTATION
# ======================================================

class Stack:
    """
    Stack Implementation (LIFO - Last In, First Out)
    
    A linear data structure that follows that Last In, First Out principle.
    Elements are added and removed from the same end (top of stack).
    
    Time Complexity:
       - Push: 0(1) - add to top
       - Pop: 0(1) - remove from top
       - Peek: 0(1) - view top element
       - Search: 0(n) - must traverse back
       
    Space Complexity: 0(n) where n is the number of elements
    
    Use Cases: 
      - Function call management (call stack)
      - Undo/Redo Operations in applications
      - Expression evaluation and syntax parsing
      - Backtracking algorithms (maze solving, DFS)
      - Browser history (back button)
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty stack.
        
        Arguments: 
           max_size: Optional maximum capacity (None for unlimited)
        """
        self._items: list = []
        self._max_size = max_size
        self.operations_log: list = []
    
    def _log_operation(self, operation: str, details: str = ""):
        """Log operation for educational tracking."""
        self.operations_log.append({
            'operation': operation,
            'details': details,
            'size_after': len(self._items)
        })
    
    def push(self, item: Any) -> bool:
        """
        Add an element to the top of the stack.
        
        Time Complexity: 0(1) - amortized constant time
        
        Arguments: 
           item: Value to push onto stack
           
        Returns: 
           True if successful, False if stack is full
        """
        if self._max_size and len(self._items) >= self._max_size:
            self._log_operation("push", f"Failed - stack full (max: {self._max_size})")
            return False
        
        self._items.append(item)
        self._log_operation("push", f"Pushed {item}")
        return True
    
    def pop(self) -> Optional[Any]:
        """
        Remove and return the top element from the stack. 
        
        Time Complexity: 0(1) - constant time
        
        Returns: 
           Top element if stack is not empty, None otherwise
        """
        if self.is_empty():
            self._log_operation("pop", "Failed - stack empty")
            return None
        
        item = self._items.pop()
        self._log_operation("pop", f"Popped {item}")
        return item
    
    def peek(self) -> Optional[Any]:
        """
        View the top element without removing it. 
        
        Time Complexity: 0(1) - constant time
        
        Returns: 
           Top element if stack is not empty, None otherwise.
        """
        if self.is_empty():
            return None
        return self._items[-1]
    
    def search(self, item: Any) -> int:
        """
        Search for an element in the stack. 
        
        Time Complexity: 0(n) - must traverse stack
        
        Arguments: 
           item: Value to search for
        
        Returns: 
           Distance from top (1-based) if found, -1 otherwise
        """
        comparisons = 0
        for i in range(len(self._items) - 1, -1, -1):
            comparisons += 1
            if self._items[i] == item:
                distance = len(self._items) - i
                self._log_operation("search", f"Found {item} at distance {distance} from top after {comparisons} comparisons.")
                return distance
        
        self._log_operation("search", f"Element {item} not found after {comparisons} comparisons)")
        return -1
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0
    
    def is_full(self) -> bool:
        """Check if stack is full (only relevant if max_size is set)."""
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size
    
    def __len__(self) -> int:
        """Return the size of the stack."""
        return len(self._items)
    
    def to_list(self) -> list:
        """Return copy of internal list (bottom to top)."""
        return self._items.copy()
    
    def display(self) -> str:
        """Return string representation of the stack."""
        if self.is_empty():
            return "Empty Stack"
        
        lines = ["--- TOP ---"]
        for item in reversed(self._items):
            lines.append(f"| {item:^7} |")
        lines.append("--- BOTTOM ---")
        return "\n".join(lines)
    
    
# ======================================================
#QUEUE IMPLEMENTATION
# ======================================================

class Queue:
    """
    Queue implementation (FIFO - First In, First Out)
    
    A linear data structure that follows the First In, First Out principle.
    Elements are added at the rear and removed from the front. 
    
    Time Complexity: 
       - Enqueue: 0(1) - add to rear
       - Dequeue: 0(1) - remove from front ( using deque )
       - Peek: 0(1) - view front element
       - Search: 0(n) - must traverse queue
       
    Space Complexity: 0(n) where n is the number of elements
    
    Use Cases: 
       - Task scheduling (CPU scheduling, print queue)
       - Breadth-Frist Search (BFS) in graphs
       - Message queues im distributed systems
       - Request handling in web servers
       - Buffer for data streams (ETL pipelines)
    """
    
    def __init__(self, max_size: Optional[int] = None):
        """
        Initialize an empty queue.
        
        Arguments: 
           max_size: Optional maximum capacity (None for unlimited)
        """
        from collections import deque
        self._items: deque = deque()
        self._max_size = max_size
        self.operations_log: list = []
        
    def _log_operation(self, operation: str, details: str = ""):
        """Log operation for educational tracking."""
        seslf.operations_log.append({
            'operation': operation,
            'details': details,
            'size_after': len(self._items)
        })
    
    def enqueue(self, item: Any) -> bool:
        """
        Add an element to the rear of the queue.
        
        Time Complexity: 0(1) - constant time
        
        Arguments: 
           item: Value to add to queue
           
        Returns:
           True if successful, False if queue is full
        """
        if self._max_size and len(self._items) >= self._max_size:
            self._log_operation("enqueue", f"Failed - queue full (max: {self._max_size})")
            return False
        
        self._items.append(item)
        self._log_operation("enqueue", f"Enqueued {item}")
        return True
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the front element from the queue.
        
        Time Complexity: 0(1) - constant time using deque
        
        Returns:
           Front element if queue is not empty, None otherwise
        """
        if self.is_empty():
            self._log_operation("dequeue", "Failed - queue empty")
            return None
        
        item = self._items.popleft()
        self._log_operation("dequeue", f"Dequeued {item}")
        return item
    
    def peek(self) -> Optional[Any]:
        """
        View the front element without removing it.
        
        Time Complexity: 0(1) constant time
        
        Returns:
           Front element if queue is not empty, None otherwise
        """
        if self.is_empty():
            return None
        return self._items[0]
    
    def search(self, item: Any) -> int:
        """
        Search for an element in the queue.
        
        Time Complexity: 0(n) - must traverse queue
        
        Arguments:
           item: Value to search for
           
        Returns:
           Position from front (0-based) if found, -1 otherwise
        """
        comparisons = 0
        for i, val in enumerate(self._items):
            comparisons += 1
            if val == item:
                self._log_operation("search", f"Found {item} at position {i} after {comparisons} comparisons")
                return i
        
        self._log_operation("search", f"Element {item} not found after {comparisons} comparisons")
        return -1
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._items) == 0
    
    def is_full(self) -> bool:
        """Check if queue is full (only relevant if max_size is set)."""
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size
    
    def __len__(self) -> int:
        """Return the size of the queue."""
        return len(self._items)
    
    def to_list(self) -> list:
        """Return copy of internal list (front to rear)."""
        return list(self._items)
    
    def display(self) -> str:
        """Return string representation of the queue."""
        if self.is_empty():
            return "Empty queue"
        
        items_str = " <- ".join(str(item) for item in self._items)
        return f"FRONT -> {items_str} <- REAR"
    
    
# ======================================================
# DEMONSTRATION FUNCTIONS
# ======================================================

    def demonstrate_stacks():
        """Demonstrate stack operations with visual output."""
        print("\n" + "=" * 60)
        print("STACK DEMONSTRATION (LIFO)")
        print("=" * 60)
        
        stack = Stack()
        
        #Push operations
        print("\n1. Pushing elements: 10, 20, 30, 40")
        for val in [10, 20, 30, 40]:
            stack.push(val)
            print(f"   After push({val}): {stack.to_list()}")
        print(f"\n  Visual representation:\n{stack.display()}")
        
        #Peek
        print(f"\n2.  Peek (view top): {stack.peek()}")
        
        #Pop operations
        print("\n3. Pop operations:")
        while not stack.is_empty():
            val = stack.pop()
            print(f"  Popped: {val}, Remaining: {stack.to_list()}")
            
        return stack
    
    def demonstrate_queue():
        """Demonstrate queue operations with visual output."""
        print("\n" + "=" * 60)
        print("QUEUE DEMONSTRATION (FIFO)")
        print("=" * 60)
        
        queue = Queue()
        
        #Enqueue operations
        print("\n1. Enqueueing elements: A, B, C, D")
        for val in ['A', 'B', 'C', 'D']:
            queue.enqueue(val)
            print(f"  After enqueue('{val}'): {queue.display()}")
            
        #Peek
        print(f"\n2. Peek (view front): {queue.peek()}")
        
        #Dequeue operations
        print("\n3. Dequeue operations:")
        while not queue.is_empty():
            val = queue.dequeue()
            print(f"  Dqueued: {val}, Remaining: {queue.display()}")
            
        return queue
    
    def demonstrate_linked_list():
        """Demonstrate linked list operations with visual output."""
        print("\n" + "=" * 60)
        print("LINKED LIST DEMONSTRATION")
        print("=" * 60)
        
        ll = LinkedList()
        
        # Insert at head
        print("\n1. Insert at head: 30, 20, 10")
        for val in [30, 20, 10]:
            ll.insert_at_head(val)
            print(f"  After insert_at_head({val}): {ll.display()}")
        
        # Insert at tail
        print("\n2. Insert at tail: 40, 50")
        for val in [40, 50]:
            ll.insert_at_tail(val)
            print(f"  After insert_at_tail({val}): {ll.display()}")
            
        #insert at position
        print("\n3. Insert 25 at position 2:")
        ll.insert_at_position(25, 2)
        print(f"  Result: {ll.display()}")
        
        #search
        print("\n4. Search operations:")
        for target in [25, 50, 100]:
            result = ll.search(target)
            status = f"Found at index {result}" if result != -1 else "Not found"
            print(f"  Search({target}): {status}")
        
        #Delete
        print("\n5. Delete 25:")
        ll.delete(25)
        print(f"  Result: {ll.display()}")
        
        return ll
    
    if __name__ == "__main__":
        demonstrate_stack()
        demonstrate_queue()
        demonstrate_linked_list()