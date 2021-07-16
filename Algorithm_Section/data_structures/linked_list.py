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

    def append(self, node: LinkedListNode):
        assert node.free == True, "node must be free. ke nist!"  # tak par bash!
        if not self.root:
            self.root = node
            node.node_busy()
        else:
            temp = self.root
            # while temp.next:
            #     temp = temp.next
            # temp.next = node
            # node.node_busy()
            while temp:
                if not temp.next:
                    temp.next = node
                    node.node_busy()
                    break
                else:
                    temp = temp.next

    def __len__(self):
        count = 0
        if not self.root:
            return 0
        else:
            temp = self.root
            while temp:
                temp = temp.next
                count += 1
            return count

    def pop(self, index=-1):
        pass

    def insert(self, node: LinkedListNode, index: int):
        assert node.free == True, "node must be free. ke nist!"  # tak par bash!
        if not self.root:
            self.root = node
            node.node_busy()
        elif index >= len(self):
            self.append(node)
        elif index == 0:
            self.add_begin(node)
        else:
            count = 0
            temp = self.root
            while temp:
                if count == (index-1):
                    right_temp = temp.next
                    temp.next = node
                    node.next = right_temp
                    break
                count += 1
                temp = temp.next

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
node4 = LinkedListNode(8954)
l1.add_begin(node1)
l1.add_begin(node2)
l1.append(node3)
l1.insert(node4, 1)
print(l1)
print(l2)
print(len(l2))


# a = [2]
# a.insert(0, "ashkan")
# print(a)
