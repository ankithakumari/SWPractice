#Implementation of a Binary search tree

def insert(root, value):
    if value <= root.val:
        if root.left == None:
            root.left = Node(value)
        else:
            insert(root.left, value)
    else:
        if root.right == None:
            root.right = Node(value)
        else:
            insert(root.right, value)

def search(root, value):
    if root.val == value:
        return root
    elif value > root.val:
        return search(root.right, value)
    else:
        return search(root.left, value)

#Inorder traversal of BST - left-root-right - returns sorted values
def inorder(root):
    if root.left != None:
        inorder(root.left)
    print(root.val)
    if root.right != None:
        inorder(root.right)

#Pre order traversal - root - left- right
def preorder(root):
    if root != None:
        print(root.val)
    if root.left != None:
        preorder(root.left)
    if root.right != None:
        preorder(root.right)

#Post order traversal -left - right - root
def postorder(root):
    if root.left != None:
        postorder(root.left)

    if root.right != None:
        postorder(root.right)
    print(root.val)

#This function returns the node with minimum value
def minNode(root):
    min_node = root
    if root.left != None:
        min_node = minNode(root.left)
    return min_node

#Delete a node from the tree

def delete(root, value):
    if value > root.val:
        root.right = delete(root.right, value)
    elif value < root.val:
        root.left = delete(root.left, value)
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp
        temp = minNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root


def height(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 0
    return 1 +  max(height(root.left), height(root.right))

#Function to find the lowest common ancestor



class Node():
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


tree = Node(80)
insert(tree, 78)
insert(tree, 85)
insert(tree, 76)
insert(tree, 105)
insert(tree, 108)
insert(tree, 102)
insert(tree, 77)
















