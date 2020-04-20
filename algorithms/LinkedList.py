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
    def insert_after_node(mid_node: Node, data):
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

    def insert_after_data(self, mid_data, data):
        """
        Insert a new node after a node with data 'mid_data'
        """
        current_node = self.head
        while current_node is not None:
            if current_node.data == mid_data:
                break
            current_node = current_node.next

        if current_node is None:
            return  # node with 'mid_data' data was not found in list

        new_node = Node(data)
        if current_node.next is not None:
            new_node.next = current_node.next
        current_node.next = new_node

    def remove_node(self, data_to_remove):
        if self.head is None:
            return

        if self.head.data == data_to_remove:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data_to_remove:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next


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
    llist.insert_after_node(llist.head.next.next.next, "wed evening")
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

    print("Insert wed night after wed evening and thus morning after Thursday")
    llist.insert_after_data("wed evening", "wed night")
    llist.insert_after_data("Sunday", "sun morning")
    llist.print_list()
