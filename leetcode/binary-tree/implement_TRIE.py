class TrieNode(object):
	def __init__(self):
		import collections
		self.children = collections.defaultdict(TrieNode)
		self.isEnd = False


class Trie(object):

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode()

	def insert(self, word):
		"""
		Inserts a word into the trie.
		:type word: str
		:rtype: void
		"""
		tmp = self.root
		for w in word:
			tmp = tmp.children[w]
		tmp.isEnd = True

	def search(self, word):
		"""
		Returns if the word is in the trie.
		:type word: str
		:rtype: bool
		"""
		tmp = self.root
		for w in word:
			tmp = tmp.children.get(w)
			if tmp is None:
				return False
		return tmp.isEnd

	def startsWith(self, prefix):
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		:type prefix: str
		:rtype: bool
		"""
		tmp = self.root

		for w in prefix:
			tmp = tmp.children.get(w)
			if tmp is None:
				return False
		return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
word = "Gaurav"
obj.insert(word)
param_2 = obj.search(word)
prefix = "Ga"
param_3 = obj.startsWith(prefix)
print(param_3)