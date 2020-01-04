class ListNode(object):
	def __init__(self,value):
		self.val = value
		self.next = None
		self.prev = None


class DoublyLinkList(object):
	def __init__(self,l):
		self.list = l
	def buildList(self):
		head = ListNode(-1)
		temp = head
		temp2 = head
		for num in self.list:
			temp.next = ListNode(num)
			temp = temp.next
			temp.prev = head
			head = head.next
		head = temp2.next
		head.prev = None
		temp.next = None
		return head


	def printList(self,head):
		temp = head
		result = []
		while temp:
			result.append(temp.val)
			temp = temp.next
		return result

	def printReverseList(self,head):
		temp = head
		result = []
		while temp.next:
			temp = temp.next
		while temp:
			result.append(temp.val)
			temp = temp.prev
		return result

if __name__ == '__main__':
	l = [4,5,2,1,7,8,9]
	ob = DoublyLinkList(l)
	head  = ob.buildList()
	print(ob.printList(head))
	print(ob.printReverseList(head))