# 이진트리(binary tree)를 위한 node클래스 선언
class Tree:
    def __init__(self):
        self.root = None
        self. size = 0

    # 순회 method 추가하기

    def preorder(self,v): #노드 v와 자손 노드를 preorder 방식으로 출력  M -> L -> R 재귀적 코드
        if v != None:
            print(v.key)
            self.preorder(v.left)
            self.preorder((v.right))


class Node:
    def __init__(self,key,parent =None, left=None,right =None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return  str(self.key)

T = Tree()
a,b,c,d = Node(1),Node(2),Node(3),Node(4)

T.root = a
a.left = b
a.right =c
c.left = d
T.preorder(T.root)




