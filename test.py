from edit_distance import DistanceManager
import pickle
from timeit import default_timer as timer


def max(a, b):
    max = 0
    for i in range(0, len(a)):
        if max <= a[i]:
            max = a[i]
            ind = i
    return b[ind], max


def testA():
    T = []
    s = []
    s.append("ca")
    s.append("cas")
    s.append("casa")
    s.append("casal")
    s.append("casale")
    edit = DistanceManager()
    dizionario = pickle.load(open("dizionario.p", "rb"))
    list1 = []
    list2 = []
    length = len(s)
    for j in range(0, length):
        start = timer()
        for i in range(0, len(dizionario)):
            a = edit.indici_ngrammi(s[j])
            b = edit.indici_ngrammi(dizionario[i])
            list1.append(edit.jaccard(a, b))
            list2.append(dizionario[i])
        end = timer()
        time = end - start
        T.append(time)
        print"------------->", s[j], max(list1, list2)

def testB():
    T = []
    s = []
    s.append("ca")
    s.append("cas")
    s.append("casa")
    s.append("casal")
    s.append("casale")
    edit = DistanceManager()
    dizionario = pickle.load(open("dizionario.p", "rb"))
    list1 = []
    list2 = []
    length = len(s)
    for j in range(0, length):
        start = timer()
        for i in range(0, len(dizionario)):
            a = edit.indici_ngrammi(s[j])
            b = edit.indici_ngrammi(dizionario[i])
            list1.append(edit.jaccard(a, b))
            list2.append(dizionario[i])
        end = timer()
        time = end - start
        T.append(time)
        print"------------->", s[j], max(list1, list2)


testA()
