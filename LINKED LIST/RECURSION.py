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
        
