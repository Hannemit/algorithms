import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None

    def print_list(self):
        print_node = self.head
        while print_node is not None:
            print(print_node.data)
            print_node = print_node.next

    def create_list(self, input_arr):
        if len(input_arr) == 0:
            return

        self.head = Node(input_arr[0])
        num = len(input_arr)
        curr_node = self.head
        for i in range(1, num):
            new_node = Node(input_arr[i])
            curr_node.next = new_node
            curr_node = curr_node.next


def compare_strings(head1: Optional[Node], head2: Optional[Node]) -> int:
    """
    Given two linked lists encoding strings, e.g. ['h', 'e', 'l', 'l', 'o'], return 0 if the lists are identical, and
    otherwise return 1 if the first list comes first alphabetically, -1 if the second list comes first.
    For example, if we have lists ['h', 'i'] and ['h', 'a'] then return 1 (as the second list comes first in dict order)
    :param head1: head of first linked list, either None or Node
    :param head2: head of second linked list, either None or Node
    :return: int
    """
    while head1 is not None and head2 is not None:
        if head1.data > head2.data:
            return 1
        if head1.data < head2.data:
            return -1

        head1 = head1.next
        head2 = head2.next

    if head1 is not None:
        return 1
    if head2 is not None:
        return -1

    return 0


def reverse_list(head: Optional[Node]) -> Optional[Node]:

    prev = None
    current = head

    while current is not None:
        nex = current.next
        current.next = prev
        prev = current
        current = nex
    return prev


def sample_random_node(head: Optional[Node]):
    """
    Given a linked list, return a node (i.e. its data) at random. Each node should be equally likely to be returned
    :param head: head of input linked list, None or Node
    :return: the data of one of the nodes (sampled at random)
    """
    if head is None:
        return None

    i = 0
    while head is not None:
        rand = np.random.randint(0, i + 1)  # random number in [0, i]
        if rand == 0:
            return_node = head

        i += 1
        head = head.next
    return return_node.data


def get_kth_from_end(head: Optional[Node], k: int):
    if head is None:
        return None

    # start one pointer k steps ahead
    steps_ahead = head
    for i in range(k):
        steps_ahead = steps_ahead.next
        if steps_ahead is None:
            if i == k - 1:
                return head.data
            else:
                return

    while steps_ahead is not None:
        head = head.next
        steps_ahead = steps_ahead.next

    return head.data


def find_intersection(head1, head2):
    """
    Given two lists that may intersect (i.e. one points to a node in the other list and from then on they follow the
    same chain), find the intersection node.
    :param head1: head of first linked list
    :param head2: head of second linked list
    :return: the intersection node (or None, if no such node)
    """

    nodes_seen = set()
    while head1 is not None:
        nodes_seen.add(head1)
        head1 = head1.next

    while head2 is not None:
        if head2 in nodes_seen:
            return head2
        head2 = head2.next

    return None


def find_inters_two_points(head1, head2):
    """
    Does same as 'find_intersection' but using two pointers and being more efficient in general
    :param head1: head of first list
    :param head2: head of second list
    :return: node of intersection (or None if no intersection)
    """
    point1 = head1
    point2 = head2
    while point1 is not point2:

        point1 = point1.next
        point2 = point2.next

        if point1 is None and point2 is None:
            return None

        if point1 is None:
            point1 = head2
        if point2 is None:
            point2 = head1
    return point1


if __name__ == "__main__":

    list1 = List()
    list1.create_list(["s", "t", "a", "c", "k", "a"])
    list1.print_list()

    list2 = List()
    list2.create_list(["s", "t", "a", "c", "k"])
    list2.print_list()

    print(compare_strings(list1.head, list2.head))

    print("Printing reverse list")
    new_head = reverse_list(list2.head)
    new_list = List()
    new_list.head = new_head
    new_list.print_list()

    print("Sample from list")
    num_list = List()
    num_list.create_list(np.arange(15))

    samples = np.zeros(5000)
    for ii in range(5000):
        samples[ii] = sample_random_node(num_list.head)

    plt.hist(samples)
    plt.show()

    in_array = [1, 2, 3, 4, 5, 6, 7, 3, 2, 1]
    llist = List()
    llist.create_list(in_array)
    k = 9
    get_kth_from_end(llist.head, k)

    # try out function to find intersection  #########
    # the nodes for one of the lists
    print("++++++++++")
    one = Node(5)
    two = Node(5)
    three = Node("ab")
    four = Node([1, 2])
    five = Node(5)
    six = Node("ab")
    seven = Node(4)

    # define first list
    first_head = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = seven

    # some nodes which are part of second list
    zero = Node(4)
    bla = Node(5)
    blabla = Node([1, 2])

    # define second list
    second_head = zero
    zero.next = bla
    zero.next.next = blabla
    blabla.next = three

    # find intersection
    intersect = find_intersection(first_head, second_head)
    intersect2 = find_inters_two_points(first_head, second_head)
    print(intersect.data)
    print(intersect2.data)
    ##########################
