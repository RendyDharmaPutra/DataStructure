from .linked_list import *

def script() :
    # Latihan
    linked = LinkedList()
    linked.traverse_list()

    linked.insert_at_start(3)
    linked.insert_at_start(1)
    linked.insert_at_start(65)
    linked.insert_at_start(3)
    linked.traverse_list()


    linked.insert_at_end(10)
    linked.insert_at_end(9)
    linked.insert_at_end(12)
    linked.insert_at_end(5)
    linked.traverse_list()


    linked.insert_at_index(index=4, data=40)
    linked.insert_at_index(index=7, data=13)
    linked.traverse_list()


    linked.delete_at_start()
    linked.delete_at_end()
    linked.traverse_list()


    linked.delete_at_index(8)
    linked.delete_at_index(5)
    linked.traverse_list()
