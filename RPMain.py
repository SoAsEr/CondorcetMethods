import csv
from CondorcetMatrix import CondorcetMatrix
import functools
from DirectedAcyclicGraph import DirectedAcyclicGraph

candidateList=[
    "Lucynda Amo",
    "Alessandro Maioli",
    "Auguste Pfeiffer",
    "Carson Giles",
    "Daniel Lin",
    "Eli Wasserman",
    "Jackson McCarthy",
    "Janki Raythattha",
    "Julia Brown",
    "Khadeeja Qureshi",
    "Kira Sehgal",
    "Liam Massey",
    "Roei Zakut",
    "Sam Bezilla",
    "Sam Harshbarger",
    "Saumya Malik",
    "Stosh Omiecinski",
    "Talia Fiester"
]

#How many winners are we looking for?
seats=3

votes=[]
with open('votes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            person = [row[2], row[3], row[4], row[5], row[6]]
            votes.append(person)
            line_count += 1




condorcetMatrix=CondorcetMatrix(candidateList)
print(len(votes))
for voteRow in votes:
    #copy it so that I can slice it
    candidateListCopy=candidateList.copy()
    for candidateWinner in voteRow:
        if(candidateWinner in candidateListCopy):
            candidateListCopy.remove(candidateWinner)
            for loser in candidateListCopy:
                condorcetMatrix.add(candidateWinner, loser, 1)

'''
#totall unecessary, but I'm doing it anyway just to see if there is a condorcet winner
winMatrix=CondorcetMatrix(candidateList)
for candidate1 in candidateList:
    for candidate2 in candidateList:
        if(condorcetMatrix.get(candidate1, candidate2)>condorcetMatrix.get(candidate2, candidate1)):
            winMatrix.add(candidate1, candidate2, 1)

for candidate1 in candidateList:
    if(all(winMatrix.getRow(candidate1))):
        print("condorcet winner: "+str(candidate1))
'''
#n by 2
majorities=[]
#back to the actual algorithm
#we're getting all the majorites
for candidate1 in candidateList:
    for candidate2 in candidateList:
        if(condorcetMatrix.get(candidate1, candidate2)>condorcetMatrix.get(candidate2, candidate1)):
            majorities+=[[candidate1, candidate2]]

#now we need to sort them:
#I wish python had a way to define custom comparison
#oh wait it does, through a special package. Because of course it does
def compareMajorities(maj1, maj2):
    if(condorcetMatrix.get(maj1[0],maj1[1])==condorcetMatrix.get(maj2[0], maj2[1])):
        if(condorcetMatrix.get(maj2[1], maj2[0])==condorcetMatrix.get(maj1[1], maj2[0])):
            return 0
        elif(condorcetMatrix.get(maj2[1], maj2[0])>condorcetMatrix.get(maj1[1], maj2[0])):
            return 1
        else:
            return -1
    if(condorcetMatrix.get(maj1[0],maj1[1])>condorcetMatrix.get(maj2[0], maj2[1])):
        return 1
    return -1

majorities.sort(key=functools.cmp_to_key(compareMajorities), reverse=True)

winners=[]

for i in range(0, seats):
    #add nodes unless would create circularity
    #the check happens in the node
    #print(majorities)
    directedGraph=DirectedAcyclicGraph(candidateList)
    for majority in majorities:
        directedGraph.addConditionalConnection(majority[0], majority[1])
    bigDaddy=directedGraph.findBigDaddy()
    winners+=[bigDaddy]

    stupid=[a for a in majorities if not bigDaddy in a]
    majorities=stupid
    candidateList.remove(bigDaddy)

print(winners)
