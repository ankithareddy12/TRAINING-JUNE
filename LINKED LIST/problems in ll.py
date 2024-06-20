#mergeTwoLists
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = dummyHead = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummyHead.next = list1
                list1 = list1.next
            else:
                dummyHead.next = list2
                list2 = list2.next
            dummyHead = dummyHead.next
        
        if list1:
            dummyHead.next = list1
        if list2:
            dummyHead.next = list2
        return newHead.next
    
#reverse
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
#remove dummy
        class Solution(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def deleteDuplicates(self, head):
        current = head
        while current is not None and current.next is not None:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
#oddeven lsit
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        head_even, odd, even = head.next, head, head.next
        while odd and even and even.next:
            odd.next = even.next
            odd = odd.next
            if odd:
                even.next = odd.next
                even = even.next

        odd.next = head_even
        
        
        return head
    #PALINDROME
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        t=head
        lst=[]
        while t!=None:
            lst.append(t.val)
            t=t.next
        return lst==lst[::-1]
    
#delete element
      def remove_elements(self, value):
        while self.head is not None and self.head.data == value:
            self.head = self.head.next

        current = self.head
        while current is not None:
            if current.next is not None and current.next.data == value:
                current.next = current.next.next
            else:
                current = current.next

class LinkedList:
    # Existing methods...

    def delete_from_beginning(self):
        if self.head is None:
            return
        self.head = self.head.next

# Test deleting from beginning
l1 = LinkedList()
l1.add_back(10)
l1.add_back(20)
l1.add_back(30)

print("Original Linked List:")
l1.display()

# Delete node from beginning
l1.delete_from_beginning()
print("Linked List after deleting from beginning:")
l1.display()

class LinkedList:
    # Existing methods...

    def delete_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

# Test deleting from end
l2 = LinkedList()
l2.add_back(10)
l2.add_back(20)
l2.add_back(30)

print("Original Linked List:")
l2.display()

# Delete node from end
l2.delete_from_end()
print("Linked List after deleting from end:")
l2.display()

class LinkedList:
    # Existing methods...

    def delete_from_middle(self, position):
        if self.head is None:
            return
        if position == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 0
        while current is not None and count != position:
            prev = current
            current = current.next
            count += 1

        if current is None:
            return
        prev.next = current.next

# Test deleting from middle
l3 = LinkedList()
l3.add_back(10)
l3.add_back(20)
l3.add_back(30)
l3.add_back(40)

print("Original Linked List:")
l3.display()

# Delete node from middle
position_to_delete = 2
l3.delete_from_middle(position_to_delete)
print(f"Linked List after deleting node at position {position_to_delete}:")
l3.display()

    def remove(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If key was not present in linked list
        if temp == None:
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None