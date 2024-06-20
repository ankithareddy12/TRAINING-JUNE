class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    
    def inorder_traversal(self, start, traversal):
        """In-order traversal: Left -> Root -> Right"""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.val) + " ")
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal
    
    def preorder_traversal(self, start, traversal):
        """Pre-order traversal: Root -> Left -> Right"""
        if start:
            traversal += (str(start.val) + " ")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal
    
    def postorder_traversal(self, start, traversal):
        """Post-order traversal: Left -> Right -> Root"""
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.val) + " ")
        return traversal

# Example usage
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("In-order Traversal:", tree.inorder_traversal(tree.root, ""))
print("Pre-order Traversal:", tree.preorder_traversal(tree.root, ""))
print("Post-order Traversal:", tree.postorder_traversal(tree.root, ""))
