from .node import *

class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_start(self, data):
        # Insert at start doesn't mean list is empty
        new_node = Node(data, self.start_node)
        self.start_node = new_node

    def insert_at_end(self, data):
        # When list is zonk -> insert at start
        if self.start_node is None:
            self.insert_at_start(data)
            return


        new_node = Node(data)

        # Search for node that responsible on referencing the new node
        n = self.start_node
        while n.ref is not None:
            n = n.ref

        # Set the last node reference to hold the new node
        n.ref = new_node

    def insert_at_index(self, index, data):
        # Insert at start
        if index == 1:
            self.insert_at_start(data)

        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1

        if n is None:
            print("======Index out of bound======")
            return

        new_node = Node(data, n.ref)
        n.ref = new_node

    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.ref)

        # Searching for the node is holding the item
        while n is not None:
            if n.item == x:
                break

            n = n.ref

        if n is None:
            print("======item not in the list======")
            return

        new_node = Node(data, n.ref)
        n.ref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("======List has no element======")
            return

        # This means insert at start
        if x == self.start_node.item:
            self.insert_at_start(data)
            return

        # Searching for the next node (n+1) is holding the item
        # Searching for the node (n) that the next node (n+1) is holding the item
        n = self.start_node
        print(n.ref)
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            print("======item not in the list======")
            return

        new_node = Node(data, n.ref)
        n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("======The list has no element to delete======")
            return

        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("======The list has no element to delete======")
            return

        # Searching for the next 2 node is last node
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref

        # Delete the reference of the element that referencing the last element
        n.ref = None

    def delete_at_index(self, index):
        # delete at start
        if index == 1:
            self.delete_at_start()

        i = 1
        n = self.start_node
        while i < index - 1 and n is not None:
            n = n.ref
            i += 1

        if n is None:
            print("======Index out of bound======")
            return

        n.ref = n.ref.ref

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("======The list has no element to delete======")
            return

        # Deleting first node
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return

        # Searching for the next node (n+1) is holding the item
        # Searching for the node (n) that the next node (n+1) is holding the item
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break

            n = n.ref

        if n.ref is None:
            print("======item not found in the list======")
            return

        # Change the node reference to the next node of the node that hold the item
        n.ref = n.ref.ref

    def traverse_list(self):
        print("")
        if self.start_node is None:
            print("======List has no element======")
            return


        n = self.start_node
        while n is not None:
            print(n.item, " ")
            n = n.ref

    def get_count(self):
        if self.start_node is None:
            return 0

        n = self.start_node
        count = 0

        while n is not None:
            count += 1
            n = n.ref

        return count

    def get_sum(self):
        n = self.start_node

        if n is None:
            print("======List has no elements======")
            return

        sum = 0

        while n is not None:
            sum += n.item
            n = n.ref

        print(f"======Sum of List : {sum}======")

    def search_item(self, x):
        if self.start_node is None:
            print("======List has no elements======")
            return

        i = 1
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("======Item found======")
                print(f"======{x} at {i}======")
                return True
            i += 1
            n = n.ref

        print("======item not found======")
        return False


