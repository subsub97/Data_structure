class Node:
    def __init__(self):

    def preoder(self):
        if self != None:
            print(self.key)
            if self.left:
                self.left.preoder()
            if self.right:
                self.right.preoder()