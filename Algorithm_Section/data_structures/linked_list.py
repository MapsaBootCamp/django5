import uuid


class LinkedListNode:
    def __init__(self, data):
        self.id = uuid.uuid4()
        self.data = data
        self.next = None
        self.free = True

    def node_free(self):
        self.free = True

    def node_busy(self):
        self.free = False

    def get_id(self):
        return self.id


class LinkedList:
    def __init__(self):
        self.root = None

    def add_begin(self, node: LinkedListNode):
        assert node.free == True, "node must be free. ke nist!"  # tak par bash!
        if not self.root:
            self.root = node
            node.node_busy()
        else:
            node.next = self.root
            self.root = node
            node.node_busy()

    def __str__(self):
        if not self.root:
            return "(]"
        temp = self.root
        result = "("
        while temp:
            result = result + str(temp.data) + (", " if temp.next else "]")
            temp = temp.next

        return result


l1 = LinkedList()
l2 = LinkedList()
node1 = LinkedListNode("ashkan")
node2 = LinkedListNode("asghar")
node3 = LinkedListNode(25)
l1.add_begin(node1)
l1.add_begin(node2)
l1.add_begin(node3)
print(l1)
print(l2)
