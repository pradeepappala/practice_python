

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.print_tree()
