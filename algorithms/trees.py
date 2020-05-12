class TreeNode:
    def __init__(self, data):
        # assume binary tree, so there's a left and right
        self.data = data
        self.left = None
        self.right = None

    def in_order_traversal(self, root) -> list:
        return (
            (
                self.in_order_traversal(root.left)
                + [root.data]
                + self.in_order_traversal(root.right)
            )
            if root
            else []
        )

    def pre_order_traversal(self, root) -> list:
        return (
            (
                [root.data]
                + self.pre_order_traversal(root.left)
                + self.pre_order_traversal(root.right)
            )
            if root
            else []
        )

    def post_order_traversal(self, root) -> list:
        return (
            (
                self.post_order_traversal(root.left)
                + self.post_order_traversal(root.right)
                + [root.data]
            )
            if root
            else []
        )

    def print_tree(self) -> None:
        # print left, self, right
        if self.left is not None:
            self.left.print_tree()
        print(self.data)
        if self.right is not None:
            self.right.print_tree()


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(6)
    tree.right = TreeNode(1)
    tree.left.left = TreeNode(5)
    tree.right.left = TreeNode(8)
    tree.right.right = TreeNode(12)

    tree.print_tree()

    res = tree.in_order_traversal(tree)
    print(res)

    res = tree.pre_order_traversal(tree)
    print(res)

    res = tree.post_order_traversal(tree)
    print(res)
