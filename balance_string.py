class Stack:
    def __init__(self):
        self.items = []
    def push(self,val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
           print("dd")
    def top(self):
       return self.items[-1]

    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return self.__len__() ==0

def solve(A):
    count = 0
    point = 0
    if(A.count('0') == A.count('1')):
        return(len(A))
    else:
        S = Stack()
        S.push(None)
        for i in range(0,len(A)):
            if S.items[-1] == None:
                S.push(int(A[i]))
            elif S.top() == int(A[i]):
                S.push(int(A[i]))
            else:
                S.pop()
                point += 1
                count +=1
                if count >= 1

        print(len(S))
        print(count*2)



A = input().strip()
print(solve(A))