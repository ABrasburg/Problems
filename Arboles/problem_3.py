# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back
# into the tree.

from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """
    Serialize a binary tree to a string using level-order traversal.
    Null nodes are represented as 'n'.
    """
    if not root:
        return "n"
        
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("n")
            
    return ",".join(result)

def deserialize(s):
    """
    Deserialize a string back into a binary tree.
    """
    if s == "n":
        return None
        
    values = s.split(",")
    root = Node(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] != "n":
            node.left = Node(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] != "n":
            node.right = Node(values[i])
            queue.append(node.right)
        i += 1
            
    return root

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print(deserialize(serialize(node)).left.left.val)