class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def create(self,root,x):
        if(root==None):
            return Node(x)
        elif root.data > x:
            root.left=self.create(root.left, x)
        else:
            root.right=self.create(root.right, x)
        return root

#traverse(inorder")      
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
#preorder
            
    def preorder(self, root):
        if root:
            print(root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
            
#postorder
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=' ')

    
#sum of all
    def sum_of_keys(self,node):
        if node is None:
            return 0
        t=node.data
        t+=self.sum_of_keys(node.left)
        t+=self.sum_of_keys(node.right)
        return t

 #is even   
    def is_even(self,node):
        return node.data%2==0
    
    def sum_of_even(self,node):
        t=0
        if self.is_even(node):
            t+=node.data
        if node.left:
            t+=self.sum_of_even(node.left)
        if node.right:
            t+=self.sum_of_even(node.right)
        return t
    
#sum of odd
    def is_odd(self,node):
        return node.data%2!=0
    def sum_of_odd(self,node):
        t=0
        if self.is_odd(node):
            t+=node.data
        if node.left:
            t+=self.sum_of_odd(node.left)
        if node.right:
            t+=self.sum_of_odd(node.right)
        return t

#sum of prime
    def is_prime(self,node):
        if node.data<=1:
            return False
        for i in range(2,int(node.data**0.5)+1):
            if node.data%i==0:
                return False
        return True
    def sum_of_prime_nodes(self,node):
        t=0
        if self.is_prime(node):
            t+=node.data
        if node.left:
            t+=self.sum_of_prime_nodes(node.left)
        if node.right:
            t+=self.sum_of_prime_nodes(node.right)
        return t

#add all
    def add_all(self,root):
        if(root==None):
            return 0
        return root.data+self.add_all(root.left)+self.add_all(root.right)
    

    
    
 #abs diff  even odd 
    def evn_odd(self,root):
        evn_sum=0
        odd_sum=0
        if(root==None):
            return 0,0
        if root.data%2==0:
            evn_sum+=root.data
        else:
            odd_sum+=root.data
        left_evn,left_odd =self.evn_odd(root.left)
        right_evn,right_odd =self.evn_odd(root.right)
        
        evn_sum+=left_evn +right_evn
        odd_sum+=left_odd+right_odd
        
        return evn_sum,odd_sum
    
  #height  
    def height(self,root):
        if root is None:
            return -1
        else:
            left_height=self.height(root.left)
            right_height=self.height(root.right)
            return 1 +max(left_height,right_height)
  
#abs diff(balence)
            
    def abs(self,root):

        if root is None:
            return -1,-1
        else:
            left_height=self.height(root.left)
            right_height=self.height(root.right)
            
        return left_height,right_height
    
#count of all nodes
    def leaf(self,root,c=0):
        if(root==None):
            return 0
            
        return 1+self.leaf(root.left)+self.leaf(root.right)
    
#leaf node and sum of leaf node
    
    def no_leafnode(self,root):
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            print("leaf nodes",root.data,end="")
            print()
            return root.data
        return self.no_leafnode(root.left)+self.no_leafnode(root.right)

    
#search and depth
    def search(self,root,key,d):
        if root.data is None:
            return None
        if root.data==key:
            return "Found",d
        if root.data>key:
            return self.search(root.left,key,d+1)
        return self.search(root.right,key,d+1)
        
#mirror
    def mirror(self,root):
        if root is None:
            return None
        root.left,root.right=root.right,root.left
        self.mirror(root.left)
        self.mirror(root.right)
        
#ll
    def left_rotate(self,z):
        y=z.right
        T2=y.left
        y.left=z
        z.right=T2
        return y
#RR
    def right_rotate(self,z):
        y=z.left
        T2=y.right
        y.right=z
        z.left=T2
        return y   
        
#LR
    def left_right_rotate(self,z):
        z.left=self.left_rotate(z.left)
        return self.right_rotate(z)
#RL
    def right_left_rotate(self,z):
        z.right=self.right_rotate(z.left)
        return self.left_rotate(z)
    
#right view:
    def right_view(self,root):
        if root is None:
            return None
        result=[]
        
        def func(root,level):
            if root is None:
                return  None
            if len(result)==level:
                result.append(root.data)
            func(root.left,level+1)
            func(root.right,level+1)

        
        func(root,0)
        
        return result
#left view
    def left_view(self,root):
        if root is None:
            return None
        result=[]
        
        def func(root,level):
            if root is None:
                return 
            if len(result)==level:
                result.append(root.data)

            func(root.right,level+1)
            func(root.left,level+1)
        func(root,0)
        
        return result
#top view
    def top_view(self, root):
        if root is None:
            return None
        d = {}
        q = [(root, 0)]
        while q:
            node, hd = q.pop(0)
            if hd not in d:
                d[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        for key in sorted(d):
            print(d[key], end=" ")
        print()
#bottom
    def top_view(self, root):
        if root is None:
            return None
        d = {}
        q = [(root, 0)]
        while q:
            node, hd = q.pop(0)
            if hd not in d:
                d[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        for key in sorted(d):
            print(d[key], end=" ")
        print()
    
    def bottom_view(self, root):
        if root is None:
            return None
        d = {}
        q = [(root, 0)]
        while q:
            node, hd = q.pop(0)
            d[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        for key in sorted(d):
            print(d[key], end=" ")
        print()
""" def fun(self,root):
        if root is None:
           return None
        d={}
        q=[(root,0)]
        while q:
            if root.left!=None:
                q.append((root.left,q[0][1]-1))
            if root.right!=None:
                q.append((root.right,q[0][1]+1))
           
            q[0][1]==root.data
            q.pop(0)
        for i in sorted(d):
            print(d[i],end=" ")"""
    
    
"""    def top_view(self,root):
        if root is None:
            return []
        top_view_map = {}
        queue = [(root, 0)]
        while queue:
            node, hd = queue.pop(0)
            if hd not in top_view_map:
                top_view_map[hd] = node.data
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        top_view_list = [top_view_map[hd] for hd in sorted(top_view_map.keys())]
        return top_view_list"""
#top view

            
                
        

t1=BinaryTree()

t1.root=t1.create(t1.root,10)
t1.root=t1.create(t1.root,5)
t1.root=t1.create(t1.root,15)
t1.root=t1.create(t1.root,2)
t1.root=t1.create(t1.root,7)
t1.root=t1.create(t1.root,4)
t1.root=t1.create(t1.root,11)
t1.root=t1.create(t1.root,20)
t1.root=t1.create(t1.root,3)


print("Inorder traversa:")
t1.inorder(t1.root)
print("\nPreorder ")
t1.preorder(t1.root)
print("\nPostorder")
t1.postorder(t1.root)

print()
keys=t1.sum_of_keys(t1.root)
print("sum of all noed",keys)
sum_even=t1.sum_of_even(t1.root)
print("Sum of even nodes:", sum_even)
sum_odd=t1.sum_of_odd(t1.root)
print("Sum of odd nodes:", sum_odd)
print("sum ofprime")
print(t1.sum_of_prime_nodes(t1.root))

print("add all")
print(t1.add_all(t1.root))

print("abs diff")
evn_sum,odd_sum=t1.evn_odd(t1.root)
print(abs(evn_sum-odd_sum))
print("height")
print(t1.height(t1.root))
print("left and right height")
left_height,right_height=t1.abs(t1.root)
print(left_height)
print(right_height)
print("abs")
print(abs(left_height-right_height))
print()
if abs(left_height-right_height)<=1:
    print("yes balenced")
else:
    print("no balenced")

print()

print("leaf nodes")
print(t1.leaf(t1.root))
print("total nodes")
total_nodes=t1.leaf(t1.root)
print(total_nodes)

print("leaf nodes")
leaf=(total_nodes+1)/2
print(leaf)
print(t1.no_leafnode(t1.root))
print("search for node:")
x=t1.search(t1.root,7,0)
print(x)
print("mirror")
t1.mirror(t1.root)
print("\nInorder traversal of mirrored tree:")
t1.inorder(t1.root)
print()
print("ll")
t1.root=t1.left_rotate(t1.root)
print("\nInorder traversal after left rotation:")
t1.inorder(t1.root)
t1.root=t1.right_rotate(t1.root)
print("\nInorder traversal after right rotation:")
t1.inorder(t1.root)
print("\nleft view")
x=t1.left_view(t1.root)
print(x)
print("\nright view")
x=t1.right_view(t1.root)
print(x)
print("\ntop view")
x=t1.top_view(t1.root)
print(x)
print("\nbottom view")
x=t1.bottom_view(t1.root)
print(x)

    