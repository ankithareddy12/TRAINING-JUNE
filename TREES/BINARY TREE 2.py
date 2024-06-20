class BinaryTreeNode:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None

    def set_left_child(self, child_node):
        if self.left:
            self.left.parent = None
        self.left = child_node
        if child_node:
            child_node.parent = self

    def set_right_child(self, child_node):
        if self.right:
            self.right.parent = None
        self.right = child_node
        if child_node:
            child_node.parent = self

    def is_even(self):
        return self.key % 2 == 0

    def is_odd(self):
        return self.key % 2 != 0

    def is_prime(self):
        if self.key <= 1:
            return False
        for i in range(2, int(self.key**0.5) + 1):
            if self.key % i == 0:
                return False
        return True

    def sum_of_even_nodes(self):
        total = 0
        if self.is_even():
            total += self.key
        if self.left:
            total += self.left.sum_of_even_nodes()
        if self.right:
            total += self.right.sum_of_even_nodes()
        return total

    def sum_of_odd_nodes(self):
        total = 0
        if self.is_odd():
            total += self.key
        if self.left:
            total += self.left.sum_of_odd_nodes()
        if self.right:
            total += self.right.sum_of_odd_nodes()
        return total

    def sum_of_prime_nodes(self):
        total = 0
        if self.is_prime():
            total += self.key
        if self.left:
            total += self.left.sum_of_prime_nodes()
        if self.right:
            total += self.right.sum_of_prime_nodes()
        return total
    
    def height(self, root):
        if root is None:
            return -1 
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            return 1 + max(left_height, right_height)
        
    def depth(self, node, root, depth_value=0):
        if root is None:
            return -1  
        if root == node:
            return depth_value
        left_depth = self.depth(node, root.left, depth_value + 1)
        if left_depth != -1:
            return left_depth
        return self.depth(node, root.right, depth_value + 1)

root = BinaryTreeNode(5)
node1 = BinaryTreeNode(10)
node2 = BinaryTreeNode(20)
node3 = BinaryTreeNode(30)
node4 = BinaryTreeNode(7)
node5 = BinaryTreeNode(50)
node6 = BinaryTreeNode(60)

root.set_left_child(node1)
root.set_right_child(node2)
node1.set_left_child(node3)
node1.set_right_child(node4)
node2.set_left_child(node5)
node2.set_right_child(node6)

print("Sum of even nodes:", root.sum_of_even_nodes())
print("Sum of odd nodes:", root.sum_of_odd_nodes())
print("Sum of prime nodes:", root.sum_of_prime_nodes())

def print_binary_tree(node, level=0):
    if node:
        print(" " * level + str(node.key))
        print_binary_tree(node.left, level + 1)
        print_binary_tree(node.right, level + 1)

print("Binary Tree Structure:")
print_binary_tree(root)

print(root.height(root))
print(root.depth(node1, root))
print(root.depth(node5, root))
