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

    def update_height(self, v):
        while v != None:
            left = -1
            right = -1
            if v.left:
                left = v.left.height
            if v.right:
                right = v.right.height
            if left >= right:
                v.height = left + 1
            else:
                v.height = right + 1
            v = v.parent

    def __len__(self):
        return self.size

    def preorder(self, v):  # MLR
        if v != None:
            print(v.key, end=' ')
            self.preorder(v.left)
            self.preorder(v.right)

    def inorder(self, v):
        if v != None:
            self.inorder(v.left)
            print(v.key, end=' ')
            self.inorder(v.right)

    def postorder(self, v):  # LRM
        if v != None:
            self.postorder(v.left)
            self.postorder(v.right)
            print(v.key, end=' ')


    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
        return p #Node를 return


    def search(self, key):
        p = self.find_loc(key)
        if p and p.key == key:
            return p
        else:
            return None


    def insert(self, key):
        # 노드들의 height 정보 update 필요
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            self.update_height(v)
            return v
        else:
            print("key is already in trees")
            return None

    def deleteByMerging(self, x):
        # 노드들의 height 정보 update 필요
        a, b, pt = x.left, x.right, x.parent
        if a == None:
            c = b
        else:
            c = m = a
            while m.right:
                m = m.right
            m.right = b
            if b != None:
                b.parent = m
        if self.root == x:  # c becomes a new root
            if c:
                c.parent = None
            self.root = c
        else:  # c becomes a child of pt of x
            if pt.left == x:
                pt.left = c
            else:
                pt.right = c
            if c:
                c.parent = pt
        self.size -= 1
        self.update_height(pt)
        return pt

    def deleteByCopying(self, x):
        # 노드들의 height 정보 update 필요
        if x == None:
            return
        a, b, pt = x.left, x.right, x.parent
        y = None
        if a:
            y = a
            while y.right:
                y = y.right
        elif b:
            y = b
            while y.left:
                y = y.left
        if y == None:
            if pt:
                if pt.left == x:
                    pt.left = None
                else:
                    pt.right = None
            else:
                self.root = None
        else:
            x.key = y.key
            ya, yb, ypt = y.left, y.right, y.parent
            c = ya
            if yb:
                c = yb
            if c:
                c.parent = ypt
            if ypt.left == y:
                ypt.left = c
            else:
                ypt.right = c
        self.size -= 1
        self.update_height(pt)
        return pt

    def height(self, x):  # 노드 x의 height 값을 리턴
        if x == None:
            return -1
        else:
            return x.height

    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        if x == None or self.size == 1:
            return None
        r = x.right
        while r and r.left:
            r = r.left
        if r:
            return r
        else:
            p = x.parent
            while p and p.right == x:
                x = p
                p = p.parent
            return p

    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x == None or self.size == 1:
            return None
        l = x.left
        while l and l.right:
            l = l.right
        if l:
            return l
        else:
            p = x.parent
            while p and p.left == x:
                x = p
                p = x.parent
            return p
    def height(self, x):  # 노드 x의 height 값을 리턴 리프노드가 0
        if x == None:
            return -1
        else:
            return x.height




    def succ(self, x):  # key값의 오름차순 순서에서 x.key 값의 다음 노드(successor) 리턴
        # x의 successor가 없다면 (즉, x.key가 최대값이면) None 리턴
        if x == None or self.size == 1:
            return None
        r = x.right
        while r and r.left:
            r = r.left
        if r:
            return r
        else:
            p = x.parent
            while p and p.right == x:
                x = p
                p = p.parent
            return p



    def pred(self, x):  # key값의 오름차순 순서에서 x.key 값의 이전 노드(predecssor) 리턴
        # x의 predecessor가 없다면 (즉, x.key가 최소값이면) None 리턴
        if x == None or self.size == 1:
            return None
        l = x.left
        while l and l.right:
            l = l.right
        if l:
            return l
        else:
            p = x.parent
            while p and p.left == x:
                x = p
                p = x.parent
            return p


    def rotateLeft(self, x):  # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        z = x.right
        if z == None:
            return
        b = z.left
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            if x.parent.right == x:
                x.parent.right = z
        z.left = x
        x.parent = z
        x.right = b
        if b:
            b.parent = x
        if self.root == x:
            self.root = z
        self.update_height(x)

    def rotateRight(self, x): # 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
        if x == None:
            return
        z = x.left
        if z == None:
            return
        b = z.right
        z.parent = x.parent
        if x.parent:
            if x.parent.left == x:
                x.parent.left = z
            if x.parent.right == x:
                x.parent.right = z
        z.right = x
        x.parent = z
        x.left = b
        if b:
            b.parent = x
        if self.root == x:
            self.root = z
        self.update_height(x)

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
