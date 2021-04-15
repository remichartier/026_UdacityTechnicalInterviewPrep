class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_from_node(new_val,self.root)

    def search(self, find_val):
        return self.search_from_node(find_val,self.root)
        
    def insert_from_node(self, new_val,node):
        if node == None:
            return
        if new_val < node.value:
            if node.left == None:
                node.left == Node(new_val)
            else:
                self.insert_from_node(new_val,node.left)
        else: # new_val < node.value
            if node.right == None:
                node.right == Node(new_val)
            else:
                self.insert_from_node(new_val,node.right)
    
    def search_from_node(self, find_val,node):
        if node == None:
            return False
        if node.value == find_val:
            return True
        if find_val < node.value:
            if node.left != None:
                return self.search_from_node(find_val,node.left)
        else: # find_val < node.value
            if node.right != None:
                return self.search_from_node(find_val,node.right)
        return False

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)