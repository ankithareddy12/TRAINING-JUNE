class Treenode:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []

    def add_child(self, child_node, position=None):
        child_node.parent = self
        if position is None:
            self.children.append(child_node)
        else:
            self.children.insert(position, child_node)

    def remove_child(self, child_node):
        self.children.remove(child_node)

    def find_child(self, key_to_find):
        if self.key == key_to_find:
            return self
        for child in self.children:
            result = child.find_child(key_to_find)
            if result:
                return result
        return None

    def sum_of_keys(self):
        total = self.key
        for child in self.children:
            total += child.sum_of_keys()
        return total
    
    def is_even(self):
        return self.key%2==0
    
    def is_odd(self):
        return self.key%2!=0
    
    def sum_of_even(self):
        if self.is_even():
            total=self.key
        else:
            total=0
        for child in self.children:
            total+=child.sum_of_even()
        return total
    
    
    def sum_of_odd(self):
        if self.is_odd():
            total=self.key
        else:
            total=0
        for child in self.children:
            total+=child.sum_of_odd()
        return total
    
    def is_prime(self):
    
        if self.key <= 1:
            return False
        for i in range(2, int(self.key**0.5) + 1):
            if self.key % i == 0:
                return False
        return True

    def find_primes(self):
       
        primes = []
        if self.is_prime():
            primes.append(self.key)
        for child in self.children:
            primes.extend(child.find_primes())
        return primes

   """ def sum_of_primes(self):
        """Calculate the sum of prime numbers in the subtree rooted at the current node."""
        prime_sum = 0
        if self.is_prime():
            prime_sum += self.key
        for child in self.children:
            prime_sum += child.sum_of_primes()
        return prime_sum"""

root = Treenode(5)
node1 = Treenode(10)
node2 = Treenode(20)
node3 = Treenode(30)
node4 = Treenode(40)
node5 = Treenode(50)
node6 = Treenode(60)


root.add_child(node1)
root.add_child(node2)
root.add_child(node3)
root.add_child(node5)
root.add_child(node6)
root.add_child(node4, position=1)

print(node2.parent.key) 

key_to_find = 5
result = root.find_child(key_to_find)
if result:
    print("found")
else:
    print("not found")

total_keys = root.sum_of_keys()
print(total_keys)


print(root.is_even())
print(node1.is_even())
print(root.is_odd())

sum_even=root.sum_of_even()
print(sum_even)
sum_odd=root.sum_of_odd()
print(sum_odd)

prime_numbers = root.find_primes()
print("Prime numbers in the tree:", prime_numbers)

def print_tree(node, level=0):
    print(" " * level + str(node.key))
    for child in node.children:
        print_tree(child, level + 1)

print_tree(root)
