class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None
        self.height = 0  # 높이 정보도 유지함에 유의!!

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def preorder(self, v):  # MLR
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            if v.left != None:
                self.inorder(v.left)
            print(v.key, end=' ')
            if v.right != None:
                self.inorder(v.right)

    def postorder(self, v):  # LRM
        if v != None:
            if v.left != None:
                self.postorder(v.left)
            if v.right != None:
                self.postorder(v.right)
            print(v.key, end=' ')


    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            if v.key == key:
                return v
            else:
                if v.key < key:
                    p = v
                    v = v.right
                else:
                    p = v
                    v = v.left
        return p


    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p


    def insert(self, key):
        # 노드들의 height 정보 update 필요
        v = Node(key)
        if self.size == 0:
            self.root = v
        else:
            p = self.find_loc(key)
            if p and p.key != key:
                if p.key > key:
                    p.left = v
                else:
                    p.right = v
                v.parent = p
        self.size += 1
        return v


    def deleteByMerging(self, x):
        # 노드들의 height 정보 update 필요
        key = x.key # 노드값으로 받아지는것을 search 메소드에서 사용가능하게 int형으로 변환
        d = self.search(key)
        l, r, p = d.left,d.right,d.parent
        if l == None: # 지우려고하는 노드의 왼쪽 서브트리가 없는경우
            c = r
        else:
            c = m = l
            while m.right:
                m = m.right
            m.right = r
            if r:
                r.parent = m
        if self.root == d:
            if c:
                c.parent = None
            self.root = c
        else:
            if p.left == d: # 원래 우리가 찾았던 x노드와 부무노드와의 위치 관계 판단
                p.left = c
            else:
                p.right = c
            if c:
                c.parent = p
        self.size -= 1
        #height 업데이트하는 라인 구현하기

    def deleteByCopying(self, x):
        key = x.key
        x = self.search(key)# 제거 해야할 노드 x 찾기
        l , r, p = x.left,x.right,x.parent# find max.key node in left child Node
        m = r # max를 찾아 저장할 변수 생성
        # 찾은 max 노드를 지울 x 노드로 카피하기 이과정에서 노드관계 다시 연결
        while m: #find right max
            m = m.right
        ml,mp,x = m.left,m.parent,m # m 을 옮기고 새로운 관계 형성을 위한 변수생성
        m.left,m.right,m.parent = l,r,p
        ml.parent = mp
        # 노드들의 height 정보 update 필요



    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height


    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        pass


    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        pass


    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        pass


    def rotateRight(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        pass


T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")
