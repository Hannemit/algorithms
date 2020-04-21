import pytest
from algorithms import LinkedList, DoublyLinkedList

remove_test_data = [
    (["A", "B", "C", "D", "E"], "C", ["A", "B", "D", "E"]),
    (["A", "B", "C", "D", "E"], "E", ["A", "B", "C", "D"]),
    (["A", "B", "C", "D", "E"], "A", ["B", "C", "D", "E"]),
    (["A"], "A", []),
    (["B", "C"], "D", ["B", "C"]),
    ([], "E", []),
]

insert_start_test_data = [
    (["A", 1, 3.5, 2, 6, "C"], "C", ["C", "A", 1, 3.5, 2, 6, "C"]),
    (["A", 1, 3.5, 2, 6, "C"], [2, 3], [[2, 3], "A", 1, 3.5, 2, 6, "C"]),
    (["A"], "A", ["A", "A"]),
    (["B", "C"], "D", ["D", "B", "C"]),
    ([], "E", ["E"]),
]


@pytest.mark.parametrize("input_elements, remove_value, expected", remove_test_data)
def test_remove_linked_lists(input_elements, remove_value, expected):
    singly = LinkedList.LinkedList()
    doubly = DoublyLinkedList.DoublyLinkedList()

    for in_node in input_elements:
        singly.insert_at_end(in_node)
        doubly.insert_at_end(in_node)

    singly.remove_node(remove_value)
    singly_vals = singly.return_list()
    assert singly_vals == expected

    doubly.remove_node(remove_value)
    doubly_vals = doubly.return_list()
    assert doubly_vals == expected


@pytest.mark.parametrize(
    "input_elements, insert_value, expected", insert_start_test_data
)
def test_insert_start(input_elements, insert_value, expected):
    singly = LinkedList.LinkedList()
    doubly = DoublyLinkedList.DoublyLinkedList()

    for in_node in input_elements:
        singly.insert_at_end(in_node)
        doubly.insert_at_end(in_node)

    singly.insert_at_start(insert_value)
    singly_vals = singly.return_list()
    assert singly_vals == expected

    doubly.insert_at_start(insert_value)
    doubly_vals = doubly.return_list()
    assert doubly_vals == expected
