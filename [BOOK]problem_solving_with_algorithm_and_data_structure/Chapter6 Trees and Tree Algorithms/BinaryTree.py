import doctest


class BinaryTree(object):
    """
    >>> r = BinaryTree('a')
    >>> r.get_root_val()
    'a'
    >>> r.get_left_child()

    >>> r.insert_left('b')
    >>> r.get_left_child().get_root_val()
    'b'
    >>> r.insert_right('c')
    >>> r.get_right_child().get_root_val()
    'c'
    >>> r.get_right_child().set_root_val('hello')
    >>> r.get_right_child().get_root_val()
    'hello'
    """

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, item):
        """
        creates a new binary tree and installs it as the left child of the current node
        """
        if self.left_child:
            self.left_child = BinaryTree(item)
        else:
            t = self.left_child
            self.left_child = BinaryTree(item)
            self.left_child.left_child = t

    def insert_right(self, item):
        """
        creates a new binary tree and installs it as the right child of the current node
        """
        if self.right_child:
            self.right_child = BinaryTree(item)
        else:
            t = self.right_child
            self.right_child = BinaryTree(item)
            self.right_child.right_child = t

    def get_right_child(self):
        """
        return the binary tree corresponding to the right child of the current node
        """
        return self.right_child

    def get_left_child(self):
        """
        return the binary tree corresponding to the left child of the current node
        """
        return self.left_child

    def set_root_val(self, root):
        """
        stores the object stored in the current node
        """
        self.key = root

    def get_root_val(self):
        """
        returns the object stored in the current node
        """
        return self.key

    def pre_order(self, root):
        """
        preorder traversal
        """
        print(root.key, end=' ')
        if root.left_child:
            root.pre_order(root.left_child)
        if root.right_child:
            root.pre_order(root.right_child)

    def post_order(self, root):
        """
        postorder traversal
        """
        if root is not None:
            self.post_order(root.left_child)
            self.post_order(root.right_child)
            print(root.key, end=' ')

    def pre_order(self, root):
        """
        Preorder traversal
        """
        print(root.key, end=' ')
        if root.left_child:
            self.pre_order(root.left_child)
        if root.right_child:
            self.pre_order(root.right_child)

    def in_order(self, root):
        """
        postorder traversal
        """
        if root is not None:
            self.post_order(root.left_child)
            print(root.key, end=' ')
            self.post_order(root.right_child)

if __name__ == "__main__":
    doctest.testmod(verbose=True)
