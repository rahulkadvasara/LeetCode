# 589. N-ary Tree Preorder Traversal
# Easy

# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Example 1:
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]

# Example 2:
# Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# 0 <= Node.val <= 104
# The height of the n-ary tree is less than or equal to 1000.

# Follow up: Recursive solution is trivial, could you do it iteratively?



# sol 1 

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children
# """

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         if not root:
#             return []
#         stack = [root]
#         result = []
#         while stack:
#             node = stack.pop()
#             result.append(node.val)
#             stack.extend(reversed(node.children))
#         return result
    

# sol 2

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         # To store the output result...
#         output = []
#         self.traverse(root, output)
#         return output
#     def traverse(self, root, output):
#         # Base case: If root is none...
#         if root is None: return
#         # Append the value of the root node to the output...
#         output.append(root.val)
#         # Recursively traverse each node in the children array...
#         for child in root.children:
#             self.traverse(child, output)



# sol 3

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children
# """

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         def inorder_traversal(node, result=[]):
#             if node:
#                 result.append(node.val)     
#                 for i in node.children:
#                     inorder_traversal(i, result) 
                        
#             return result
#         return inorder_traversal(root)
        


# sol 4

# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
#         self.val = val
#         self.children = children
# """

# class Solution:
#     def preorder(self, root: 'Node') -> List[int]:
#         res = []
#         def t(node):
#             if not node:
#                 return
#             res.append(node.val)
#             for ch in node.children:
#                 t(ch)
#         t(root)
#         return res