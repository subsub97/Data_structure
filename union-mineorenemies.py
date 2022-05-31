class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self #따로 정해주지 않으면 set의 대표 key 값이어야 하기에
        self.rank = 0
        self.id = None

class tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,x):
        v = Node(x)
        if v.parent == v.key:
            self.root = v

def make_set(x):
    v = Node(total[x])
    return v.key

def set_friend(x,y):
    # 모순 발생여부 확인
    while x.parent.key != x.key:
        x = x.parent
    while y.parent.key != y.key:
        y = y.parent

    if x.id == None and y.id == None: #둘 다 중립인경우
        x.id,y.id = "friend"
        if x.rank > y.rank: # rank 큰놈 밑에 작은거 보내기
            y.parent = x
        elif x.rank < y.rank:
            x.parent = y
        else: # 둘이 같은 경우
            y.parent = x
            x.rank += 1
    elif x.id == "friend" and y.id == None: # 하나만 id가 있는경우
        y.id = "friend"
    elif x.id == None and y.id == "friend":
        x.id = "friend"
    elif x.id == "enemy" and y.id ==None:
        y.id = "enemy"
    elif x.id == None and y.id == "enemy":
        x.id = "enemy"
    elif x.id == "enemy" and y.id == "enemy":
        pass
    else: # 모순 발생 적과 friend는 친구가 될수 없다.
        print("-1")

    # 누가 부모노드가 될 것인지 판단.
    # 같은 집합으로 만든다.


n = int(input())

total=[]

for i in range(n): # 번호 부여하기
    total.append(i)
    make_set(i)













'''한번 입력을 받으면 op랑 0 과 1'''




