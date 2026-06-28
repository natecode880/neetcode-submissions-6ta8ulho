class Node():
    def __init__(self, key: int, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None
class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Node(key, val)
            return
        
        current = self.root
        while True:
            if key > current.key:
                if current.right is None:
                    current.right = Node(key,val)
                    return
                current = current.right
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key,val)
                    return
                current = current.left
            else:
                current.value = val
                return

    def get(self, key: int) -> int:
        current = self.root
        while current:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.value
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current.left:
            current = current.left
        return current.value

    def getMax(self) -> int:
        if not self.root:
            return -1
        current = self.root
        while current.right:
            current = current.right
        return current.value

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def minNode(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current
    
    def removeHelper(self, node, key):
        if not node:
            return None

        if key < node.key:
            node.left = self.removeHelper(node.left, key)
        elif key > node.key:
            node.right = self.removeHelper(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self.minNode(node.right)
                node.key = min_node.key
                node.value = min_node.value
                node.right = self.removeHelper(node.right, min_node.key)
        return node


    def getInorderKeys(self) -> List[int]:
        res = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            res.append(node.key)
            traverse(node.right)
        traverse(self.root)
        return res

