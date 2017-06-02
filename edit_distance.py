import pickle


class DistanceManager:
    def __init__(self):
        self.matrice = []
        self.operazione = []
        self.costo = [1, 1, 1, 0, 1]  # costo operazioni insert, delete, replace, copy, twiddle

    def set_costo(self, c):
        self.costo = c

    def edit_distance(self, a, b):

        self.righe = len(a) + 1
        self.colonne = len(b) + 1
        self.matrice = [[0 for k in range(self.colonne)] for k in range(self.righe)]
        self.operazione = [[0 for k in range(self.colonne)] for k in range(self.righe)]
        for riga in range(1, self.righe):
            self.matrice[riga][0] = riga * self.costo[2]
            self.operazione[riga][0] = "DELETE"
        for colonna in range(1, self.colonne):
            self.matrice[0][colonna] = colonna * self.costo[1]
            self.operazione[0][colonna] = "INSERT"
        for riga in range(1, self.righe):
            for colonna in range(1, self.colonne):
                self.matrice[riga][colonna] = float("inf")
                if a[riga - 1] == b[colonna - 1]:
                    self.matrice[riga][colonna] = self.matrice[riga - 1][colonna - 1] + self.costo[3]
                    self.operazione[riga][colonna] = "COPY"
                if a[riga - 1] != b[colonna - 1] and self.matrice[riga - 1][colonna - 1] + self.costo[2] < \
                        self.matrice[riga][colonna]:
                    self.matrice[riga][colonna] = self.matrice[riga - 1][colonna - 1] + self.costo[2]
                    self.operazione[riga][colonna] = "REPLACE by" + b[colonna - 1]
                if riga >= 2 and colonna >= 2 and a[riga - 1] == b[colonna - 2] and a[riga - 2] == b[colonna - 1] and \
                                        self.matrice[riga - 2][colonna - 2] + self.costo[4] < self.matrice[riga][
                            colonna]:
                    self.matrice[riga][colonna] = self.matrice[riga - 2][colonna - 2] + self.costo[4]
                    self.operazione[riga][colonna] = "TWIDDLE"
                if self.matrice[riga - 1][colonna] + self.costo[1] < self.matrice[riga][colonna]:
                    self.matrice[riga][colonna] = self.matrice[riga - 1][colonna] + self.costo[1]
                    self.operazione[riga][colonna] = "DELETE"
                if self.matrice[riga][colonna - 1] + self.costo[0] < self.matrice[riga][colonna]:
                    self.matrice[riga][colonna] = self.matrice[riga][colonna - 1] + self.costo[0]
                    self.operazione[riga][colonna] = "INSERT " + y[colonna - 1]

    def _sequenza_operazioni(self, i, j):

        if i == 0 and j == 0:
            return
        if self.operazione[i][j] == "COPY" or self.operazione[i][j].count("REPLACE by", 0, 12) == 1:
            k = i - 1
            s = j - 1
        elif self.operazione[i][j] == "TWIDDLE":
            k = i - 2
            s = j - 2
        elif self.operazione[i][j] == "DELETE":
            k = i - 1
            s = j
        else:
            k = i
            s = j - 1
        self._sequenza_operazioni(k, s)
        print self.operazione[i][j]

    def trova_ngrammi(self, list, n):
        return zip(*[list[i:] for i in range(n)])

    def indici_ngrammi(self, list):
        indici = []
        for i in range(len(list)):
            ngrammi = self.trova_ngrammi(list, i)
            indici += ngrammi

        return indici

    def jaccard(self, s1, s2):
        s1 = set(s1)
        s2 = set(s2)
        return float(len(s1 & s2)) / len(s1 | s2)


y = ["C", "I", "A", "O"]
x = ["C", "A", "I", "O"]
edit = DistanceManager()
edit.edit_distance(x, y)  # conversione ciao in caio
sub = "edo"
str = "edo"
A = edit.trova_ngrammi(sub, 2)
B = edit.trova_ngrammi(str, 2)
print B
print edit.jaccard(A, B)  # Prende in input due liste di n-gram e calcola il coeff.di Jaccard
print str.count(sub, 0, 40)

dizionario = open("60000_parole_italiane.txt",
                  "r")  # blocco di codice per convertire file txt in un array pickle usabile per i confronti
dizionario = dizionario.readlines()
final_list = []
for i in dizionario:
    final_list.append(i.strip())  # elimino gli /n
print final_list
pickle.dump(final_list, open("dizionario.p", "wb"))
