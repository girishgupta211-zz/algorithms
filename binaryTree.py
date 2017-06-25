class Node:
	def __init__(self,data):
		self.value = data
		self.left = None
		self.right = None 


arr =  [20,40,50,70,80,100,120,300]
start = 0
end = len(arr) -1
def createBinaryTree(arr,start,end):	
	if( start > end ):
		return None
	middle = start + (end-start)/2	
	root = Node(arr[middle])
	root.left = createBinaryTree(arr,start,middle-1)
	root.right = createBinaryTree(arr,middle+1 , end)
	return root


root = createBinaryTree(arr,start,end)

def traveserInorder(root):
	if (root == None):
		return
	
	traveserInorder(root.left)
	print root.value
	traveserInorder(root.right)

	
traveserInorder(root)