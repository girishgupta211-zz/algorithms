# In this article, a new approach is discussed that supports minimum with O(1) extra space. We define a variable minEle that stores the current minimum element in the stack. Now the interesting part is, how to handle the case when minimum element is removed. To handle this, we push “2x – minEle” into the stack instead of x so that previous minimum element can be retrieved using current minEle and its value stored in stack. Below are detailed steps and explanation of working.
#
# Push(x) : Inserts x at the top of stack.
#
# If stack is empty, insert x into the stack and make minEle equal to x.
# If stack is not empty, compare x with minEle. Two cases arise:
    # If x is greater than or equal to minEle, simply insert x.
    # If x is less than minEle, insert (2*x – minEle) into the stack and make minEle equal to x. For example,
    # let previous minEle was 3. Now we want to insert 2. We update minEle as 2 and insert 2*2 – 3 = 1 into the stack.

# Pop() : Removes an element from top of stack.
    # Remove element from top. Let the removed element be y. Two cases arise:
        # If y is greater than or equal to minEle, the minimum element in the stack is still minEle.
        # If y is less than minEle, the minimum element now becomes (2*minEle – y), so update (minEle = 2*minEle – y). This is where we retrieve previous minimum from current minimum and its value in stack. For example, let the element to be removed be 1 and minEle be 2. We remove 1 and update minEle as 2*2 – 1 = 3.
        # Important Points:

# Stack doesn’t hold actual value of an element if it is minimum so far.
# Actual minimum element is always stored in minEle

# Class to make a Node
class Node:
    # Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next = None

    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)

    # __repr__ is same as __str__
    __repr__ = __str__


class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None

    # This method returns the string representation of the object (stack).
    def __str__(self):
        temp = self.top
        out = []
        while temp:
            out.append(str(temp.value))
            temp = temp.next
        out = '\n'.join(out)
        return ('Top {} \n\nStack :\n{}'.format(self.top, out))

    # __repr__ is same as __str__
    __repr__ = __str__

    # This method is used to get minimum element of stack
    def getMin(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Minimum Element in the stack is: {}".format(self.minimum))
            return self.minimum

    # Method to check if Stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
            # If top not equal to None then stack is empty
            return False

    # This method returns length of stack
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count += 1
        return self.count

    # This method returns top of stack
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            if self.top.value < self.minimum:
                print("Top Most Element is: {}".format(self.minimum))
            else:
                print("Top Most Element is: {}".format(self.top.value))

    # This method is used to add node to stack
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value

        elif value < self.minimum:
            temp = (2 * value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
        print("Number Inserted: {}".format(value))

    # This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        else:
            removed_node = self.top.value
            self.top = self.top.next
            if removed_node < self.minimum:
                print("Top Most Element Removed :{} ".format(self.minimum))
                self.minimum = ((2 * self.minimum) - removed_node)
            else:
                print("Top Most Element Removed : {}".format(removed_node))


# Driver program to test above class
stack = Stack()

stack.push(3)  # min=3, stack: 2*3 - 3 = 3
stack.push(5)  # min=5, stack: 3,5
stack.getMin()
stack.push(2)  # min=2, stack: 3,5,2*2-3=1
stack.push(1)  # min=1 , stack: 3,5,1,2*1-2=0
print(stack)
stack.getMin()
stack.pop()  # min=2*1 - 0 = 2 , stack: 3,5,1
stack.getMin()  # min=2, stack: 33,5,1
stack.pop()  # min=2*2-1, stack: 33, 5
stack.peek()  # 5
print(stack)
