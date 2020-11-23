class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.sentinel = False


class CircularList:
    def __init__(self):
        self.__sentinel = Node(None)
        self.__sentinel.sentinel = True
        self.__head = self.__sentinel
        self.__tail = self.__sentinel
        self.__current = self.__sentinel
        self.__size = 0

    def add(self, value):
        """Add element to tail end circular list.

        Args:
            value (Any): value to be added.
        """
        newNode = Node(value)
        if self.__size == 0:
            self.__sentinel.next = newNode
            self.__sentinel.prev = newNode
            newNode.next = self.__sentinel
            newNode.prev = self.__sentinel
            self.__head = newNode
            self.__tail = newNode
            self.__size += 1
        else:
            self.__tail.next = newNode
            newNode.next = self.__sentinel
            newNode.prev = self.__tail
            self.__tail = newNode
            self.__size += 1

    def remove(self):
        """Remove element at head end circular list.

        Returns:
            Node: referance of head node.
        """

        nodeToRemove = None
        if self.__size == 0:
            return nodeToRemove
        elif self.__size == 1:
            nodeToRemove = self.__head
            self.__sentinel.next = None
            self.__sentinel.prev = None
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return nodeToRemove
        else:
            nodeToRemove = self.__head
            self.__sentinel.next = self.__head.next
            self.__head = self.__head.next
            return nodeToRemove

    def getNext(self):
        """Get next value in the circular list

        Returns:
            Any: value of the next node.
        """

        if self.__size == 0:
            return None
        elif self.__size == 1:
            return self.__sentinel.next.value
        else:
            if self.__current == self.__tail:
                self.__current = self.__head
                return self.__current.value
            else:
                self.__current = self.__current.next
                return self.__current.value

    def getPrevious(self):
        """Get previous value in the circular list

        Returns:
            Any: value of the previous node.
        """

        if self.__size == 0:
            return None
        elif self.__size == 1:
            return self.__sentinel.prev.value
        else:
            if self.__current == self.__head:
                self.__current = self.__tail
                return self.__current.value
            else:
                self.__current = self.__current.prev
                return self.__current.value

    def getCurrent(self):
        """Get current position in the list.

        Returns:
            value: value of current position.
        """

        return self.__current.value

    def getHead(self):
        """Get referance to head node in circular list.

        Returns:
            Node: referance of head node.
        """
        return self.__head

    def getTail(self):
        """Get referance to tail node in circular list.

        Returns:
            Node: referance of tail node.
        """
        return self.__tail

    def getHeadValue(self):
        """Get value of head in circular list.

        Returns:
            Element: value of head node.
        """
        return self.__head.value

    def getTailValue(self):
        """Get value of tail in circular list.

        Returns:
            Element: value of tail node.
        """
        return self.__tail.value

    def getSize(self):
        """Get size of the circular list.

        Returns:
            integer: number of elements in the queue.
        """
        return self.__size

    def isEmpty(self):
        """Check if circular list is empty.

        Returns:
            boolean: True if no elements in the stack.
        """
        return True if self.__size == 0 else False

    def __str__(self):
        """Get string representation of the circular list.

        Returns:
            String: prints string representation of the stack.
        """
        arr = []
        current = self.__head
        while current:
            if current.sentinel == True:
                break
            arr.append(current.value)
            current = current.next
        return str(arr)

    def __len__(self):
        return self.__size


if __name__ == "__main__":
    pass