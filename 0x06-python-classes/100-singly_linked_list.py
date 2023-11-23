#!/usr/bin/python3
"""
100-singly_linked_list.py
Module that defines a singly linked list
"""


class Node:
    """
    Node class

    Attributes:
        data (int): the data of the node
        next_node (Node): the next node

    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data

        Args:
            value (int): the data of the node

        Raises:
            TypeError: if the data is not an integer

        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next node

        Returns:
            next_node (Node): the next node

        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next node

        Args:
            value (Node): the next node

        Raises:
            TypeError: if value is not a node or empty

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Singly linked list

    """
    def __init__(self):
        """
        initialization of the class

        """
        self.__head = None

    def __str__(self):
        """
        String representation of the linked list

        """
        values = []
        current = self.__head
        while current:
            values.append(str(current.data))
            current = current.__next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """
        Insert a new node in the correct sorted position in the list

        Args:
            value (Node): the new node

        """
        new = Node(value)
        if self.__head is None:
            new.__next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.__next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.__next_node is not None and
                    current.__next_node.data < value):
                current = current.__next_node
            new.__next_node = current.__next_node
            current.__next_node = new
