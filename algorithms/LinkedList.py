class Node:
    """
    Each node in our linked list has some data stored (self.data), and points to the next node in the chain
    (self.next), which is another Node (or None)
    """

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    The linked list is just a chain of nodes, with a head node at the start.
    """

    def __init__(self):
        self.head = None

    def print_list(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
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

    @staticmethod
    def insert_after(mid_node: Node, data):
        """
        Insert the new node after 'mid_node' (some node somewhere 'in the middle' (i.e. not start or end)
        :param mid_node: Node
        :param data: data for new node
        :return: None
        """
        if mid_node is None:
            print("mid node did not exist")
            return

        new_node = Node(data)
        new_node.next = mid_node.next
        mid_node.next = new_node


if __name__ == "__main__":

    llist = LinkedList()
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

    print("Add wednesday evening in after wednesday")
    llist.insert_after(llist.head.next.next.next, "wed evening")
    llist.print_list()
