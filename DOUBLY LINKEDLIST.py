class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def display(self):
        t = self.head
        while t != None:
            print(t.data, end="->")
            t = t.next
        print()
    
    def sort(self):
        if self.head is None:
            return None
        slow = fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data 

        t1 = slow.data.next
        if t1 == None:
            t1.prev = None  
        middle.next = None  

        if t1 != None:
            self.tail.next = self.head
            self.head.prev = self.tail
            self.head = second_half 
            self.tail = middle  

        
    
            
    def reverse(self):
        t = self.tail
        while t != None:
            print(t.data, end="->")
            t = t.prev
        print()
        
    def search(self, key):
        t = self.head
        while t != None:
            if t.data == key:
                return True
            t=t.next
        return False
    

    def search1(self, key):
        t = self.head
        t1=self.tail
        while t != None and t1!=None:
            if t.data == key or t1.data == key:
                return True
            t=t.next
            t1=t1.prev
        return False
    
    def diff_even_odd(self):
        def sum_recursive(node):
            if node is None:
                return 0,0
            even_sum, odd_sum = sum_recursive(node.next)
            if node.data % 2 == 0:
                even_sum += node.data
            else:
                odd_sum += node.data
            return even_sum, odd_sum
        
        even_sum, odd_sum = sum_recursive(self.head)
        return even_sum-odd_sum
        
    def even_odd(self):
        even_sum = 0
        odd_sum = 0
        t = self.head

        while t!=None:
            if t.data % 2 == 0:
                even_sum += t.data
            else:
                odd_sum += t.data
            t = t.next
        
        return even_sum - odd_sum
    
    def is_prime(self, n):
        if n<= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    
    def find(self,node,primes):
        if node is None:
            return None
        if self.is_prime(node.data):
            primes.append(node.data)
        self.find(node.next, primes)

    def get_prime(self):
        primes = []
        self.find(self.head,primes)
        return primes
    def sum(self,i=2):
        if i==n//2:
            return False
        if is_prime(n) and is_prime(n-i):
            return True
        



    def count_prime(self,node,c):
        if node is None:
            return
        if self.is_prime(node.data):
            c+=1
        self.count_prime(node.next, c)
         
    def get_prime_count(self):
        c= 0
        self.count_prime(self.head, c)
        return c

    
    def find_middle(self):
        if self.head is None:
            return None
        slow = fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
 

           
    

    def add_back(self, x):
        if self.head == None:
            self.head = Node(x)
            self.tail = self.head
        else:
            t = Node(x)
            self.tail.next = t
            t.prev = self.tail
            self.tail = self.tail.next
            

    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    
    def palindrome(self):
        t=self.head
        lst=[]
        while t!=None:
            lst.append(t.data)
            t=t.next
        if lst==lst[::-1]:
            return True
        return False
    
    def palindrome1(self):
        t = self.head
        t1 = self.tail
        
        while t!=t1 and t!= t1.next:
            if t.data==t1.data:
                t=t.next
                t1=t1.prev
                return True
            return False
    
        
    



l1 = DoublyLinkedList()
l1.head=Node(5)
l1.tail=l1.head
l1.add_back(7)
l1.add_back(8)
l1.add_back(2)
l1.add_back(1)
l1.add_back(4)

#l1.insert_at_beg(1)
#l1.insert_at_end(70)
l1.display()
#l1.reverse()
#print(l1.diff_even_odd())
print(l1.even_odd())
print(l1.get_prime())
print(l1.get_prime_count())
#print(l1.find_middle())
#print(l1.search(50))
#print(l1.search1(50))
#print(l1.palindrome())
#print(l1.palindrome1())
#print(l1.sort())
