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


def min(a, b):
    min = float("inf")
    for i in range(0, len(a)):
        if min >= a[i]:
            min = a[i]
            ind = i
    return b[ind], min


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
        print"A------------->", s[j], max(list1, list2)


def testB():
    T = []
    s = []
    s.append("c")
    s.append("ca")
    s.append("cas")
    s.append("casa")
    s.append("casal")
    s.append("casale")
    length = len(s)
    dizionario = pickle.load(open("dictionary.p", "rb"))
    list1 = []
    list2 = []
    for i in range(1, length):
        start = timer()
        for j in range(1, len(dizionario)):
            a = s[i]
            a = list(a)
            b = dizionario[j]
            b = list(b)
            edit = DistanceManager()
            edit.edit_distance(a, b)
            list1.append(edit.matrix[len(a)][len(b)])
            list2.append(dizionario[j])
        end = timer()
        tempo = end - start
        T.append(tempo)
        print"B------------->", s[i], min(list1, list2)
    print T





testA()
testB()
