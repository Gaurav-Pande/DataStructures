# vanilla topological sorting

"""
This method is based on DFS. It is not based on in degree and out degree!
"""
import collections
class Graph(object):
	# directed graph
	def __init__(self, vertices):
		self.graph = collections.defaultdict(list)
		self.v = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def getDic(self):
		return self.graph

	def topologicalSort(self):
		stack = []
		visited = [False]*self.v
		for v in range(self.v):
			if not visited[v]:
				self.dfs(v, stack, visited)
		print(stack)

	def dfs(self, v, stack, visited):
		visited[v] = True
		for children in self.graph[v]:
			if not visited[children]:
				self.dfs(children, stack, visited)
		stack.insert(0,v)


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
	# ob.addEdge(3,4)
	print(ob.getDic())
	ob.topologicalSort()
	# edges = [(0,1),(1,2),(2,3),(3,4),(2,4),(3,4)]
	# ob2 = Graph2(edges=edges, vertices=5)
	# print(ob2.getDic())
