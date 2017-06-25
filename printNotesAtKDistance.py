class Node:
	def __init__(self,data):
		self.value = data
		self.left = None
		self.right = None 

def printNotesAtKDistance(root , k):
	if root is None:
		return
	if k == 0:
		print root.value
	else:
		# print k-1
		printNotesAtKDistance(root.left,k-1)
		printNotesAtKDistance(root.right,k-1)


def getLevelDiff(root):
	if root is None:
		return 0
	else:
		return root.value - getLevelDiff(root.left) - getLevelDiff(root.right)

def printLevelorder(root,label):
	if(root == None):
		return
	if (label == 1):
		print root.value

	printLevelorder(root.left, label -1)
	printLevelorder(root.right, label -1)

def heigth(root):
	if(root == None):
		return 0
	lheight = heigth(root.left) 
	rheight = heigth(root.right)	
	if(lheight > rheight):
		return lheight+1
	else:
		return rheight+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
# print heigth(root)
printNotesAtKDistance(root,0)


# Driver program to test above function
root = Node(5)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(4)
root.left.right.left = Node(3)
root.right.right = Node(8)
root.right.right.right = Node(9)
root.right.right.left = Node(7)
# printNotesAtKDistance(root,0)
# print getLevelDiff(root)

# printLevelorder(root,4)

# for i in range(0,5):
# 	printLevelorder(root,i)

# Function to  print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printGivenLevel(root, i)
        