
# Assuming:
# A Table in Database named Tutorial
# Table Tutorial contains following fields : Name (Name of The tag),
# Path (Path of Tutorial file that user will refer)
from .models import Tutorial
from enum import Enum

class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    mem = [[]]
    ca = [0]
    mem.append(ca)
    ans = editDist(a, b, mem)
    return ans


def editDist(a, b):
    """Return Matrix Of Tuples"""
    ans = []
    ca = []
    """Mem is memory Matrix And It contains Only Cost"""
    mem = [[0 for i in range(len(b) + 1)] for j in range(len(a) + 1)]

    for i in range(len(a) + 1):
        mem[i][0] = i

    for i in range(len(b) + 1):
        ca.append((i, Operation.INSERTED))
        mem[0][i] = i
    """ca is Chota Answer i.e. It is a row in Matrix Ans"""
    ans.append(ca)
    for i in range(1, len(a) + 1):
        ca = []
        ca.append((i, Operation.DELETED))
        for j in range(1, len(b) + 1):
            cost = 0
            op = Operation.SUBSTITUTED
            if a[i - 1] == b[j - 1]:
                cost = int(mem[i-1][j-1])
                op = Operation.SUBSTITUTED
                mem[i][j] = cost
                ca.append((cost, op))
            else:
                ls = []
                ls.append((1 + int(mem[i-1][j]), Operation.DELETED))
                ls.append((1 + int(mem[i-1][j-1]), Operation.SUBSTITUTED))
                ls.append((1 + int(mem[i][j-1]), Operation.INSERTED))
                # print(ls)
                ls = sorted(ls, key=tf)
                # print(ls)
                mem[i][j] = ls[0][0]
                ca.append(ls[0])
        ans.append(ca)

    ans[0][0] = (0, None)
    return ans[-1][-1][0]


def tf(e):
    """Key Function For Comparsion of tuples"""
    return e[0]

def getMatchedResult(query):
    query = query.lower()
    retrivedResult = Tutorial.objects.all()
    # print(retrivedResult)
    ls = []
    for result in retrivedResult:
        # print(result.path)
        ls.append((editDist(result.name, query), result))
    ls.sort(key = lambda x : x[0])
    Suggestions = []
    for i in range(5):
        if i < len(ls):
            d = {
                "f" : ls[i][1].name,
                "s" : ls[i][1].path,
            }
            Suggestions.append(d)
    return Suggestions
