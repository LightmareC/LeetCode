# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        current = head
        carry = 0

        while l1 or l2:
        	val = carry
        	if l1:
        		val += l1.val
        		l1 = l1.next
        	if l2:
        		val += l2.val
        		l2 = l2.next

        	carry = val / 10
        	val = val % 10
        	current.next = ListNode(val)
        	current = current.next

        if carry == 1:
        	current.next = ListNode(1)

        return head.next

if __name__ == '__main__':
	l1, l1.next, l1.next.next = ListNode(2), ListNode(4), ListNode(7)
	l2, l2.next, l2.next.next = ListNode(5), ListNode(6), ListNode(4)
	result = Solution().addTwoNumbers(l1,l2)
	print_str = ""
	while result:
		print_str += str(result.val)
		result = result.next
		if result:
			print_str += " -> "

	print(print_str)



        	

