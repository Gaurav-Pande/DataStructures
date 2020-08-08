#
# in a graph detect a cycle using degree of a vertex, and if exist print all the nodes existing in a cycle
#
import collections
class Graph(object):
	def __init__(self, vertices):
		self.graph = collections.defaultdict(list)
		self.v = vertices

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def getDic(self):
		return self.graph

	def detectAndPrintCycle(self):
		queue = []