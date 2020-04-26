import numpy as np
import matplotlib.pyplot as plt
from typing import Union


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


def compare_strings(head1: Union[None, Node], head2: Union[None, Node]) -> int:
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


def reverse_list(head: Union[None, Node]) -> Union[None, Node]:

    prev = None
    current = head

    while current is not None:
        nex = current.next
        current.next = prev
        prev = current
        current = nex
    return prev


def sample_random_node(head: Union[None, Node]):
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
    num_list.create_list(np.arange(3))

    samples = np.zeros(5000)
    for ii in range(5000):
        samples[ii] = sample_random_node(num_list.head)

    plt.hist(samples)
    plt.show()
