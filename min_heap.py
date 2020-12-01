# Course: CS261 - Data Structures
# Assignment: 5
# Student: Jaime Justo
# Description: Min heap implementation using a dynamic array to store heap content.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new object to the MinHeap maintaining heap property.
        """
        # add element at the end of the array
        self.heap.append(node)

        # check if we maintained the heap property
        self.bubble_up(self.heap.length() - 1)

    def get_min(self) -> object:
        """
        Returns an object with a minimum key without removing it from the heap. If the heap is empty, the method raises
        a MinHeapException.
            :return: minimum key from the heap.
            :rtype: object.
        """
        # check if heap is empty
        if self.is_empty():
            raise MinHeapException

        return self.heap[0]

    def remove_min(self) -> object:
        """
        Returns an object with a minimum key and removes it from the heap. If the heap is empty, the method raises a
        MinHeapException.
            source: Open Data Structures 10.1.
            :return: minimum key from the heap.
            :rtype: object.
        """
        if self.is_empty():
            raise MinHeapException

        # replace root with last element
        last_element_index = self.heap.length() - 1
        self.heap.swap(0, last_element_index)

        # store and remove minimum key
        min_key = self.heap.pop()

        # swap the last element with its child until reaching the correct spot
        self.trickle_down(0)

        return min_key

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives a dynamic array with objects in any order and builds a proper MinHeap from them. Current content of
        the MinHeap is lost.
            :param DynamicArray da: collection of objects used to build a min heap.
        """
        # copy DA elements into heap content
        self.heap = DynamicArray()
        for i in range(da.length()):
            self.heap.append(da[i])

        # get first non-leaf element from the back of the array
        size = self.heap.length()
        first_non_leaf_elem = (size // 2) - 1

        # percolate down each non-leaf element moving backwards checking if it's subtrees are proper heaps
        while first_non_leaf_elem >= 0:
            right_child = 2 * first_non_leaf_elem + 2
            left_child = 2 * first_non_leaf_elem + 1

            # parent is larger than right child
            if right_child < size and self.heap[first_non_leaf_elem] > self.heap[right_child]:
                # check if the right child is the minimum child
                if self.heap[left_child] <= self.heap[right_child]:
                    # left child was the minimum child, swap with parent
                    self.heap.swap(first_non_leaf_elem, left_child)
                    first_non_leaf_elem = left_child
                else:
                    # right child was the minimum child, swap with parent
                    self.heap.swap(first_non_leaf_elem, right_child)
                    first_non_leaf_elem = right_child
            # parent is only larger than left child or no right child exists
            elif left_child < size and self.heap[first_non_leaf_elem] > self.heap[left_child]:
                # swap left child with parent
                self.heap.swap(first_non_leaf_elem, left_child)
                first_non_leaf_elem = left_child
            # subtree is a proper heap
            else:
                first_non_leaf_elem -= 1

    def bubble_up(self, new_element_index):
        """
        Compares the values of the inserted element with the values of its parent. If the value of the parent is greater
        than the value of the inserted element, the elements are swapped. The parent gets updated and the comparisons
        continue until the beginning of the array has been reached or the parent is smaller than the element.
        reference: Open Data Structures 10.1
        """
        parent_index = ((new_element_index - 1) // 2)
        # swap new element with its parent until it is no longer smaller than its parent
        while new_element_index > 0 and self.heap[new_element_index] < self.heap[parent_index]:
            # swap elements
            self.heap.swap(parent_index, new_element_index)
            # update index
            new_element_index = parent_index
            # get new parent
            parent_index = ((new_element_index - 1) // 2)

    def trickle_down(self, replacement_element_index):
        """
        Compares the values of the replacement index with the minimum value of its children. If the replacement
        element's value is greater than its minimum child's value, the two are swapped in the array and repeats until
        reaching the correct spot.
        reference: Open Data Structures 10.1
        """
        size = self.heap.length()

        # swap the replacement element with its minimum child
        while replacement_element_index >= 0:
            j = -1
            right_index = 2 * replacement_element_index + 2
            # parent is larger than the right child
            if right_index < size and self.heap[right_index] < self.heap[replacement_element_index]:
                left_index = 2 * replacement_element_index + 1
                # right child isn't the minimum child
                if self.heap[left_index] <= self.heap[right_index]:
                    j = left_index
                # right child is the minimum child
                else:
                    j = right_index
            # parent is larger than the left child or there is no right child
            else:
                left_index = 2 * replacement_element_index + 1
                if left_index < size and self.heap[left_index] < self.heap[replacement_element_index]:
                    j = left_index
            # swap parent with minimum child
            if j >= 0:
                self.heap.swap(j, replacement_element_index)
            # parent is smaller than both children
            replacement_element_index = j


# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
