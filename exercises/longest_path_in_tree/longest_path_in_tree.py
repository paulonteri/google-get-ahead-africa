"""
Longest Path in Tree:

Write a function that computes the length of the longest path of consecutive integers in a tree. 
A node in the tree has a value and a set of children nodes. A tree has no cycles and each node has exactly one parent.
A path where each node has a value 1 greater than its parent is a path of consecutive integers (e.g. 1,2,3 not 1,3,5). 
A few things to clarify:
    Integers are all positive
    Integers appear only once in the tree
"""


class Tree:
    def __init__(self, value, *children):
        self.value = value
        self.children = children


def longest_path_helper(tree, parent_value, curr_length, longest_length):
    if not tree:
        return longest_length

    if tree.value == parent_value + 1:
        curr_length += 1
    else:
        curr_length = 1

    longest_length = max(longest_length, curr_length)
    for child in tree.children:
        longest_length = max(longest_length, longest_path_helper(
            child, tree.value, curr_length, longest_length)
        )
    return longest_length


def longest_path(tree):
    if not tree:
        return

    return longest_path_helper(tree, float('-inf'), 0, 0)


assert longest_path(
    Tree(1,
         Tree(2,
              Tree(4)),
         Tree(3))
) == 2
assert longest_path(
    Tree(5,
         Tree(6),
         Tree(7,
              Tree(8,
                   Tree(9,
                        Tree(15),
                        Tree(10))),
              Tree(12)))
) == 4
