class AANode:
    def __init__(self, key):
        self.key = key
        self.level = 1
        self.left = None
        self.right = None

    # skew operation
    @staticmethod
    def aa_skew(aa_node):
        if aa_node is None:
            return None
        elif aa_node.left is None:
            return aa_node
        elif aa_node.level == aa_node.left.level:
            left = aa_node.left
            aa_node.left = left.right
            left.right = aa_node
            aa_node = left
            return aa_node
        else:
            return aa_node

    # split operation
    @staticmethod
    def aa_split(aa_node):
        if aa_node is None:
            return None
        elif aa_node.right is None or aa_node.right.right is None:
            return aa_node
        elif aa_node.level == aa_node.right.right.level:
            right = aa_node.right
            aa_node.right = right.left
            right.left = aa_node
            aa_node = right
            aa_node.level += 1
            return aa_node
        else:
            return aa_node


class AATree:
    def __init__(self):
        self._root = None
        self.num_entries = 0

    def _find(self, node, key):
        if key is None:
            return None
        elif key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return node

    def _insert(self, node, key):
        if node is None:
            node = AANode(key)
            self.num_entries += 1
            return node
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        node = AANode.aa_skew(node)
        node = AANode.aa_split(node)
        return node

    def _is_leaf(self, node):
        return (node.left is None) and (node.right is None)

    def _successor(self, node):
        if node.right.left is None:
            return node.right
        else:
            temp_node = node.right
            while temp_node.left is not None:
                temp_node = temp_node.left
            return temp_node

    def _predecessor(self, node):
        if node.left.right is None:
            return node.left
        else:
            temp_node = node.left
            while temp_node.right is not None:
                temp_node = temp_node.right
            return temp_node

    def _decrease_level(self, node):
        should_be = min(0 if node.left is None else node.left.level, 0 if node.right is None else node.right.level) + 1
        if should_be < node.level:
            node.level = should_be
            if node.right is not None and should_be < node.right.level:
                node.right.level = should_be
        return node

    def _remove(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            self.num_entries -= 1
            if self._is_leaf(node):
                return None
            elif node.left is None:
                l = self._successor(node)
                node.right = self._remove(node.right, l.key)
                node.key = l.key
            else:
                l = self._predecessor(node)
                node.left = self._remove(node.left, l.key)
                node.key = l.key

        node = self._decrease_level(node)
        node = AANode.aa_skew(node)
        node.right = AANode.aa_skew(node.right)
        if node.right is not None:
            node.right.right = AANode.aa_skew(node.right.right)
        node = AANode.aa_split(node)
        node.right = AANode.aa_split(node.right)
        return node

    def _print_tree(self, node, level):
        if node is None:
            return
        self._print_tree(node.right, level+1)
        for i in range(level):
            print("    ", end='')
        print(str(node.key) + "\r\n", end='')
        self._print_tree(node.left, level+1)

    def find(self, key):
        return self._find(self._root, key)

    def insert(self, key):
        self._root = self._insert(self._root, key)

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def print_tree(self):
        self._print_tree(self._root, 0)


if __name__ == "__main__":
    tree = AATree()

    tree.insert(5)
    tree.insert(45)
    tree.insert(2)
    tree.insert(34)
    tree.insert(7)
    tree.insert(100)
    tree.insert(150)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)
    tree.insert(8)
    tree.insert(9)

    # tree.remove(100)
    # tree.remove(2)
    # tree.remove(4)
    # tree.remove(8)
    # tree.remove(150)
    # tree.remove(34)
    # tree.remove(1)
    # tree.remove(7)
    # tree.remove(3)
    # tree.remove(45)
    # tree.remove(5)
    # tree.remove(9)

    tree.print_tree()
