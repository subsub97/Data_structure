# 이진트리(binary tree)를 위한 node클래스 선언
    class Node:
        def __init__(self):
            self.key = key
            self.parent = parent
            self.left = left
            self.right = right

        def __str__(self):
            return  str(self.key)

    class Tree:
        def __init__(self):
            self.root = None
            self. size = 0


        def height(self.root):
        l,r = 0,0
        if root.left:
            l = height(root.left)+1
        if root.right:
            r = height(root.right)+1
        return max(l,r)






