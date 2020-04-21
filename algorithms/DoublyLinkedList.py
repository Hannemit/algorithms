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
            print(node_to_print.data)
            node_to_print = node_to_print.next

    def return_list(self) -> list:
        value = self.head
        all_vals = []
        while value is not None:
            all_vals.append(value.data)
            value = value.next
        return all_vals

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.prev = current_node

    def insert_after_data(self, after_data, data):
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

    def remove_node(self, data_to_remove):
        if self.head is None:
            return

        if self.head.data == data_to_remove:
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data_to_remove:
                if current_node.next.next is not None:
                    current_node.next.next.prev = current_node
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


if __name__ == "__main__":

    llist = DoublyLinkedList()
    tue = Node("Tuesday")
    wed = Node("Wednesday")
    thu = Node("Thursday")
    fri = Node("Friday")
    sat = Node("Saturday")

    llist.head = Node("Monday")
    llist.head.next = tue
    tue.next = wed
    wed.next = thu
    thu.next = fri
    fri.next = sat
    sat.next = Node("Sunday")

    llist.print_list()

    print("Add sunday at start")
    llist.insert_at_start("Sunday")
    llist.print_list()

    print("Add monday at end")
    llist.insert_at_end("Monday")
    llist.print_list()

    print("Remove tuesday")
    llist.remove_node("Tuesday")
    llist.print_list()

    print("Remove tuesday again (should do nothing)")
    llist.remove_node("Tuesday")
    llist.print_list()

    print("Remove Monday twice")
    llist.remove_node("Monday")
    llist.remove_node("Monday")
    llist.print_list()

    print("Insert wed night after wed evening and sun morning after Sunday")
    llist.insert_after_data("wed evening", "wed night")
    llist.insert_after_data("Sunday", "sun morning")
    llist.print_list()
