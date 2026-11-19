"""AVL Tree: self-balancing BST using rotations. insert O(log n)."""
from typing import List, Optional


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.height = 1


def h(n: Optional[Node]) -> int:
    return n.height if n else 0


def update(n: Node) -> None:
    n.height = 1 + max(h(n.left), h(n.right))


def balance(n: Node) -> int:
    return h(n.left) - h(n.right)


def rotate_right(y: Node) -> Node:
    x = y.left
    y.left, x.right = x.right, y
    update(y); update(x)
    return x


def rotate_left(x: Node) -> Node:
    y = x.right
    x.right, y.left = y.left, x
    update(x); update(y)
    return y


def insert(root: Optional[Node], key: int) -> Node:
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root
    update(root)
    b = balance(root)
    if b > 1 and key < root.left.key:        # Left-Left
        return rotate_right(root)
    if b < -1 and key > root.right.key:      # Right-Right
        return rotate_left(root)
    if b > 1:                                # Left-Right
        root.left = rotate_left(root.left)
        return rotate_right(root)
    if b < -1:                               # Right-Left
        root.right = rotate_right(root.right)
        return rotate_left(root)
    return root


def inorder(n: Optional[Node]) -> List[int]:
    return inorder(n.left) + [n.key] + inorder(n.right) if n else []


def is_balanced(n: Optional[Node]) -> bool:
    return n is None or (abs(balance(n)) <= 1 and is_balanced(n.left) and is_balanced(n.right))


if __name__ == "__main__":
    root = None
    for k in range(1, 128):          # sorted input would make a plain BST a linked list
        root = insert(root, k)
    assert inorder(root) == list(range(1, 128))
    assert is_balanced(root)
    assert root.height == 7          # perfect tree of 127 nodes
    r = None
    for k in [10, 20, 30]:           # RR case
        r = insert(r, k)
    assert r.key == 20
    r = None
    for k in [30, 10, 20]:           # LR case
        r = insert(r, k)
    assert r.key == 20
    print("All tests passed!")
