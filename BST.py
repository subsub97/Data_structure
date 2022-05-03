#BST(Binary search Tree) 이진탐색트리

class Node:
    def __init__(self,key, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


    def __str__(self):
        return str(self.key)


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    #트리 안에 key값을 갖은 노드가 있다면 출력 아니라면 부모노드 출력
    def find_loc(self, key):
        if self.size == 0: # tree is empty
            return None

        p = None # p = parent node of v
        v = self.root
        while v: # while v != None
            if v.key == key:
                return v
            else:
                if v.key < key: #BST의 성질(왼쪽은 작고 오른쪽은 큼)을 이용한 조건
                    p = v #부모노드를 기억하면서 자식 노드로 내려간다
                    v= v.right
                else:
                    p = v
                    v = v.left
        return p # 찾지 못한 경우 부모노드가 리턴

    def search(self,key): #찾는 노드가 없다면 None 부모를 출력하는 find와는 다름
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None

    def insert(self, key):
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key: # p is parent of v
                if p.key > key:
                    p.left = v
                else:
                    p.right = v
                v.parent = p #삽입된 노드의 부모 노드 설정
        self.size += 1 # 22.05.03 첫 작성시 해당라인과 리턴 위치로 에러 발생함 주의하기
        return v

T = Tree()
a,b,c,d = T.insert(1),T.insert(2),T.insert(3),T.insert(4)
print(b.key)
T.insert(10)
print(d.left.key)




