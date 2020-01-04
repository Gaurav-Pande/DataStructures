# Raw code to implement a BST in general
# insert
# find
# traversals:
# preorder
# postorder
# inorder

class TreeNode(object):
	def __init__(self,value):
		self.val = value
		self.left = None
		self.right = None


class BinarySearchTree(object):
	def __init__(self,nodes):
		self.root = TreeNode(nodes[0])
		#self.buildTree(self.root,nodes)

	def buildTree(self,root, nodes):
		for i in range(1,len(nodes)):
			self.insertNode(root,TreeNode(nodes[i]))
		return root

	def insertNode(self,root,node):
		if root.val >= node.val:
			if not root.left:
				root.left = node
			else:
				self.insertNode(root.left,node)
		else:
			if not root.right:
				root.right = node
			else:
				self.insertNode(root.right,node)
		return root

	def inroderTraversal(self,root):
		if not root:
			return None
		else:
			self.inroderTraversal(root.left)
			print(root.val)
			self.inroderTraversal(root.right)

	def postOrderTraversal(self,root):
		if not root:
			return None
		else:
			self.postOrderTraversal(root.left)
			self.postOrderTraversal(root.right)
			print(root.val)

	def preOrderTraversal(self,root):
		if not root:
			return None
		else:
			print(root.val)
			self.preOrderTraversal(root.left)
			self.preOrderTraversal(root.right)

	def searchNode(self,root,node):
		if root.val == node.val:
			return True
		else:
			if node.val < root.val:
				self.searchNode(root.left,node)
			elif node.val > root.val:
				self.searchNode(root.right,node)
			else:
				return False



if __name__ == '__main__':
	nodes = [1,2,3,4,5,6]
	ob = BinarySearchTree(nodes)
	root  = ob.buildTree(ob.root,nodes)
	print(ob.inroderTraversal(root))

