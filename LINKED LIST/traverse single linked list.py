class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head
        while t!=None:
            print(t.data, end='->')
            t = t.next
        print()

    def add_back(self, x):
        if not self.head:
            self.head = Node(x)
            return
        t = self.head
        while t.next!=None:
            t = t.next
        t.next = Node(x)

    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        t = self.head
        while t!=None:
            if t.data == key:
                return True
            t = t.next
        return False

    def find_middle(self):
        slow = fast = self.head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def length(self):
        t = self.head
        c = 0
        while t!=None:
            c += 1
            t = t.next
        return "even" if c % 2 == 0 else "odd"

    def sum(self):
        t = self.head
        s = 0
        while t!=None:
            s += t.data
            t = t.next
        return s

    def print_all_pairs(self):
        pairs = []
        t = self.head
        while t!=None:
            x = t.next
            while x!=None:
                pairs.append((t.data, x.data))
                x = x.next
            t = t.next
        return pairs

    def bubbleSort(self):
        swapped = True
        while swapped==True:
            t = self.head
            swapped = False
            while t.next!=None:
                if t.data > t.next.data:
                    t.data, t.next.data = t.next.data, t.data
                    swapped = True
                
                t = t.next


    def display_sorted(self):
        self.bubbleSort()
        self.display()
    def bsort(self):
        c=0
        T=self.head
        p=None
        while (T.next!=None):
            f=0
            t=self.head
            while(t.next!=p):
                if(t.data>t.next.data):
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c=c+1
            if(f==0):
                break
            p=t
            T=T.next
            
    def reverse(self):
        t=self.head
        prev=None

        while(t!=None):
            n=t.next
            t.next=prev
            prev=t
            t=next
        self.head=prev
        
        
            
        

l1 = LinkedList()
l1.head = Node(10)
l1.add_back(30)
l1.add_back(20)
l1.add_back(40)
l1.add_back(50)

l1.display()
print(l1.search(20))
print(l1.find_middle())
print(l1.length())

print(l1.sum())
print(l1.print_all_pairs())
l1.display_sorted()
l1.bsort()
print(l1.reverse())
