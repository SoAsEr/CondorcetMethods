class CondorcetMatrix:
    def __init__(self, candidateList):
        self.matrix=[[0 for x in range(len(candidateList))] for y in range(len(candidateList))]
        self.candidateIndexDict={}
        for index in range(0,len(candidateList)):
            self.candidateIndexDict.update({candidateList[index]:index})

    def add(self, candidateRow, candidateColumn, voteNumber):
        self.matrix[self.candidateIndexDict[candidateRow]][self.candidateIndexDict[candidateColumn]]+=voteNumber

    def get(self, candidateRow, candidateColumn):
        return self.matrix[self.candidateIndexDict[candidateRow]][self.candidateIndexDict[candidateColumn]]

    def getRow(self, candidateRow):
        return self.matrix[self.candidateIndexDict[candidateRow]]
