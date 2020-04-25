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
    Just a chain of nodes, with a head node at the start.
    """

    def __init__(self):
        self.head = None

    def create_list(self, in_array):
        for ii, value in enumerate(in_array):
            new_node = Node(value)
            if ii == 0:
                self.head = new_node
            else:
                prev_node.next = new_node
            prev_node = new_node

    def print_list(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next

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

    def bub_sort(self):
        end = None
        while end is not self.head:
            start = self.head
            while start.next is not end:
                nextnode = start.next
                if nextnode.data < start.data:
                    start.data, nextnode.data = nextnode.data, start.data
                start = start.next
            end = start

    def merge(self, list2):
        merged_list = LinkedList()
        merged_list.head = self._merge_list(self.head, list2.head)
        return merged_list

    @staticmethod
    def _merge_list(head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        new_head = Node()
        if head1.data < head2.data:
            new_head.data = head1.data
            head1 = head1.next
        else:
            new_head.data = head2.data
            head2 = head2.next

        merged = new_head
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                new_node = Node(head1.data)
                merged.next = new_node
                head1 = head1.next
            else:
                new_node = Node(head2.data)
                merged.next = new_node
                head2 = head2.next
            merged = merged.next

        while head1 is not None:
            new_node = Node(head1.data)
            merged.next = new_node
            merged = merged.next

        while head2 is not None:
            new_node = Node(head2.data)
            merged.next = new_node
            head2 = head2.next
            merged = merged.next

        return new_head


if __name__ == "__main__":

    llist = LinkedList()
    llist.create_list(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    )
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

    print("Creating new list and sorting..")
    input_arr = [6, 3, 5, 1, 8, 6, 3, 5, 9, 2, 4, 3, 1, 8, 4, 7, 2]
    llist.create_list(input_arr)
    llist.bub_sort()
    llist.print_list()

    print("Merging sorted list with other sorted list")
    llist2 = LinkedList()
    llist2.create_list([-4, -2, 0, 0, 1, 2, 5, 9, 12])
    lmerged = llist.merge(llist2)
    lmerged.print_list()

    print("original ones")
    llist2.print_list()

    print("bla")
    llist.print_list()
