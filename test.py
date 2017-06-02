from edit_distance import DistanceManager
import pickle
from timeit import default_timer as timer
from matplotlib import pyplot as plt


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
        print"testA------------->", s[j], max(list1, list2)
        pickle.dump(T, open("tA.p", "wb"))


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
    dizionario = pickle.load(open("dizionario.p", "rb"))
    list1 = []
    list2 = []
    edit = DistanceManager()
    for i in range(1, length):
        start = timer()
        for j in range(1, len(dizionario)):
            a = s[i]
            a = list(a)
            b = dizionario[j]
            b = list(b)
            edit.edit_distance(a, b)
            list1.append(edit.matrice[len(a)][len(b)])
            list2.append(dizionario[j])
        end = timer()
        tempo = end - start
        T.append(tempo)
        print"testB------------->", s[i], min(list1, list2)
    pickle.dump(T, open("tB.p", "wb"))


def testC():
    T = []
    dizionario = pickle.load(open("dizionario.p", "rb"))
    edit = DistanceManager()
    a = "parola"
    z = a
    a = edit.trova_ngrammi(a, 2)
    s = a[0]
    F = []
    Lista1 = []
    Lista2 = []
    for i in range(0, len(dizionario)):
        start = timer()
        F.append(edit.trova_ngrammi(dizionario[i], 2))
        for j in range(0, len(F[i])):
            if F[i][j] == s:
                Lista1.append(dizionario[i])
        end = timer()
        time = end - start
        T.append(time)
    for i in range(0, len(Lista1)):
        a = list(z)
        b = list(Lista1[i])
        start = timer()
        edit.edit_distance(a, b)
        end = timer()
        time = end - start
        T.append(time + T[i])
        Lista2.append(edit.matrice[len(a)][len(b)])
    print"testC------------->", min(Lista2, Lista1)
    pickle.dump(T[0:5], open("tC.p", "wb"))



def runAllTestAndPlot():
    testA()
    A=pickle.load(open("tA.p", "rb"))
    testB()
    B=pickle.load(open("tB.p", "rb"))
    testC()
    C=pickle.load(open("tC.p", "rb"))
    plt.plot(A, label="testA")
    plt.plot(B, label="testB")
    plt.plot(C, label="testC")
    plt.legend()
    plt.show()


runAllTestAndPlot()