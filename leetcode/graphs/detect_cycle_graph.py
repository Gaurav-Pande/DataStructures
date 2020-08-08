# vanilla code for detecting cycle in a graph using dfs

import collections
class Graph(object):
	# directed graph
	def __init__(self,vertices):
		self.graph = collections.defaultdict(list)
		self.v = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def getDic(self):
		return self.graph

	def detectCycle(self):
		# a stack to mark if a node which is already visited or not
		stack = [False]*self.v
		# a visited list to keep track of node visited
		visited = [False]*self.v

		for node in range(self.v):
			if not visited[node]:
				if self.dfs(node, stack, visited):
					return True

		return False

	def dfs(self, node, stack, visited):
		visited[node]=True
		stack[node] = True
		for children in self.graph[node]:
			if stack[children]:
				return True
			if not visited[children]:
				if self.dfs(children, stack, visited):
					return True
		stack[node]=False
		return False






class Graph2(object):
	# graph directed
	def __init__(self, edges, vertices):
		self.dic = collections.defaultdict(list)
		self.v = vertices
		for  x,y in edges:
			self.dic[x].append(y)

	def getDic(self):
		return self.dic





if __name__ == '__main__':
	ob = Graph(5)
	ob.addEdge(0,1)
	ob.addEdge(1,2)
	ob.addEdge(2,3)
	ob.addEdge(3,4)
	ob.addEdge(2,4)
	ob.addEdge(4,1)
	# ob.addEdge(3,4)
	print(ob.getDic())
	print(ob.detectCycle())
	# edges = [(0,1),(1,2),(2,3),(3,4),(2,4),(3,4)]
	# ob2 = Graph2(edges=edges, vertices=5)
	# print(ob2.getDic())
