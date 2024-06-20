class TreeNode:
    def __init__(self, key):
        self.val = key
        self.children = []

class Tree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def add_child(self, parent_key, child_key):
        parent_node = self.find(self.root, parent_key)
        if parent_node:
            parent_node.children.append(TreeNode(child_key))
        else:
            print(f"Parent node with key {parent_key} not found.")

    def delete_child(self, parent_key, child_key):
        parent_node = self.find(self.root, parent_key)
        if parent_node:
            for i, child in enumerate(parent_node.children):
                if child.val == child_key:
                    del parent_node.children[i]
                    return
            print(f"Child node with key {child_key} not found under parent with key {parent_key}.")
        else:
            print(f"Parent node with key {parent_key} not found.")

    def delete_parent(self, key):
        if self.root.val == key:
            print("Cannot delete the root of the tree.")
            return

        parent_node, child_index = self.find_parent(self.root, key)
        if parent_node:
            del parent_node.children[child_index]
        else:
            print(f"Node with key {key} not found.")

    def find(self, node, key):
        if node is None:
            return None
        if node.val == key:
            return node
        for child in node.children:
            found_node = self.find(child, key)
            if found_node:
                return found_node
        return None

    def find_parent(self, node, key, parent=None):
        if node is None:
            return None, -1
        if node.val == key:
            return parent, -1
        for i, child in enumerate(node.children):
            if child.val == key:
                return node, i
            found_node, child_index = self.find_parent(child, key, node)
            if found_node:
                return found_node, child_index
        return None, -1

    def depth_first_traversal(self, node):
        if node:
            print(node.val, end=" ")
            for child in node.children:
                self.depth_first_traversal(child)

    def breadth_first_traversal(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            for child in node.children:
                queue.append(child)

    def sum_of_nodes(self, node):
        if node is None:
            return 0
        total = node.val
        for child in node.children:
            total += self.sum_of_nodes(child)
        return total

# Example usage
tree = Tree(1)
tree.add_child(1, 2)
tree.add_child(1, 3)
tree.add_child(2, 4)
tree.add_child(2, 5)
tree.add_child(3, 6)
tree.add_child(3, 7)

print("Depth-First Traversal:")
tree.depth_first_traversal(tree.root)  # Output: 1 2 4 5 3 6 7

print("\nBreadth-First Traversal:")
tree.breadth_first_traversal()  # Output: 1 2 3 4 5 6 7

print("\nSum of Nodes:")
print(tree.sum_of_nodes(tree.root))  # Output: 28
