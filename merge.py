#Question1
#Merging two binary trees

class BinaryTree():
	def __init__(self, x):
		self.rootNode = x
		self.leftNode = None
		self.rightNode = None

class MergedTree():
	def mergeFunction(self, tree1, tree2):
		if tree1 is None:
			return tree2
		if tree2 is None:
			return tree1
		#add the root node values
		tree1.rootNode += tree2.rootNode
		#add the left node values
		tree1.leftNode = self.mergeFunction(tree1.leftNode, tree2.leftNode)
		#add the right node values
		tree1.rightNode = self.mergeFunction(tree1.rightNode, tree2.rightNode)
		return tree1
