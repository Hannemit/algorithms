class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node_to_print = self.head
        while node_to_print is not None:
            print(node_to_print)
            node_to_print = node_to_print.next

    def add_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def add_after_data(self, after_data, data):
        """
        Insert a new node after the node which has 'after_data' as data.
        :param after_data: the data (can be anything really) at some node after which we want to insert
                our new node
        :param data: the data for the new node
        :return:
        """
        if self.head is None:
            print("No data in list")
            return

        current_node = self.head
        while current_node is not None:
            if current_node.data == after_data:
                break
            current_node = current_node.next

        if current_node is None:
            return  # there was no node with 'after_data' data

        new_node = Node(data)
        new_node.prev = current_node
        new_node.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = new_node
        current_node.next = new_node
