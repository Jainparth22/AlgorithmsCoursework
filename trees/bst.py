"""Binary Search Tree. insert/search/delete avg O(log n), worst O(n) (skewed)."""
from typing import List, Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


def insert(root: Optional[Node], key: int) -> Node:
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root  # duplicates ignored


def search(root: Optional[Node], key: int) -> bool:
    while root:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False


def delete(root: Optional[Node], key: int) -> Optional[Node]:
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        succ = root.right  # in-order successor
        while succ.left:
            succ = succ.left
        root.key = succ.key
        root.right = delete(root.right, succ.key)
    return root


def inorder(root: Optional[Node]) -> List[int]:
    return inorder(root.left) + [root.key] + inorder(root.right) if root else []


if __name__ == "__main__":
    root = None
    for k in [50, 30, 70, 20, 40, 60, 80, 30]:
        root = insert(root, k)
    assert inorder(root) == [20, 30, 40, 50, 60, 70, 80]
    assert search(root, 60) and not search(root, 65)
    root = delete(root, 20)   # leaf
    root = delete(root, 30)   # one child
    root = delete(root, 50)   # two children
    assert inorder(root) == [40, 60, 70, 80]
    assert delete(None, 1) is None
    print("All tests passed!")
