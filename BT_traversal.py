# 이진트리(binary tree)를 위한 node클래스 선언
class Node:
    def __init__(self,key,parent =None, left=None,right =None):
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

    # 순회 method 추가하기

    def preorder(self,v): #노드 v와 자손 노드를 preorder 방식으로 출력  M -> L -> R 재귀적 코드
        if v != None:
            print(v.key,end=' ') # end = '' 를 사용하면 줄바꿈이 아니라 '' 띄어쓰기로 한줄에 가능
            self.preorder(v.left)
            self.preorder(v.right)

    def postorder(self,v): #L -> R -> M
        if v != None:
            if v.left != None:
                self.postorder(v.left)
            if v.right != None:
                self.postorder(v.right)
            print(v.key)




T = Tree()
a,b,c,d,e,f = Node(1),Node(2),Node(3),Node(4),Node(5),Node(6)

T.root = a
a.left = b
a.right =c
c.left = d
b.right = e
e.left = f

T.postorder(T.root)




