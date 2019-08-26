import queue

# try:
#     raw_input  # Python 2
# except NameError:
#     raw_input = input  # Python 3


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:

    def build_tree(self):
        print("\n********Press N to stop entering at any point of time********\n")
        print("Enter the value of the root node: ", end="")
        check = input().strip().lower()
        if check == 'n':
            return None
        data = int(check)
        q = queue.Queue()
        tree_node = TreeNode(data)
        q.put(tree_node)
        while not q.empty():
            node_found = q.get()
            print("Enter the left node of %s: " % node_found.data, end="")
            check = input().strip().lower()
            if check == 'n':
                return tree_node
            left_data = int(check)
            left_node = TreeNode(left_data)
            node_found.left = left_node
            q.put(left_node)
            print("Enter the right node of %s: " % node_found.data, end="")
            check = input().strip().lower()
            if check == 'n':
                return tree_node
            right_data = int(check)
            right_node = TreeNode(right_data)
            node_found.right = right_node
            q.put(right_node)


    def pre_order_iter(self,node):
        if not isinstance(node, TreeNode) or not node:
            return
        stack = []
        n = node
        while n or stack:
            while n:  # start from root node, find its left child
                print(n.data, end=" ")
                stack.append(n)
                n = n.left
            # end of while means current node doesn't have left child
            n = stack.pop()
            # start to traverse its right child
            n = n.right


    def in_order_iter(self,node):
        if not isinstance(node, TreeNode) or not node:
            return
        stack = []
        n = node
        while n or stack:
            while n:
                stack.append(n)
                n = n.left
            n = stack.pop()
            print(n.data, end=" ")
            n = n.right


    def post_order_iter(self,node):
        if not isinstance(node, TreeNode) or not node:
            return
        stack1, stack2 = [], []
        n = node
        stack1.append(n)
        while stack1:  # to find the reversed order of post order, store it in stack2
            n = stack1.pop()
            if n.left:
                stack1.append(n.left)
            if n.right:
                stack1.append(n.right)
            stack2.append(n)
        while stack2:  # pop up from stack2 will be the post order
            print(stack2.pop().data, end=" ")
# b1 = BinaryTree()
# b1.build_tree()