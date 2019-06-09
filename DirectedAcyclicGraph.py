class Node:
    def __init__(self, name):
        self.name=name
        self.parents=[]
        self.children=[]

    def hasSomewhereInChildren(self, name):
        if(self.name==name):
            return True
        for child in self.children:
            if(child.hasSomewhereInChildren(name)):
                return True
        return False

class DirectedAcyclicGraph:
    def __init__(self, names):
        self.nameDict={}
        self.nodes=[]
        for name in names:
            nodeWithName=Node(name)
            self.nodes+=[nodeWithName]
            self.nameDict.update({name : nodeWithName})



    def addConnection(self, name1, name2):
        if(not self.nameDict[name2].hasSomewhereInChildren(name1)):
            self.nameDict[name2].parents+=[self.nameDict[name1]]
            self.nameDict[name1].children+=[self.nameDict[name2]]

    def findBigDaddy(self):
        for node in self.nodes:
            if(len(node.parents)==0):
                return node.name
