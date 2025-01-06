# implementation of the bellman ford algorithm by SEK171

from math import *

# define the graphe
X = ["A", "B", "C", "D", "E", "F", "G"]
U = {
    "A": {"B": 30, "E": 36, "G": 180},
    "B": {"C": 60, "D": 42, "E": 27, "F": 18},
    "C": {"G": 84},
    "D": {"C": 18, "G": 90},
    "E": {"C": 48, "F": 48, "G": 126},
    "F": {"A": 33, "C": 36, "D": 12, "G": 132},
    "G": {}
}
# create the precedents dictionary
def UtoUi(U):
    Ui = {node: set() for node in U}

    for x, suivants in U.items():
        for suivant in suivants:
            if suivant not in Ui:
                Ui[suivant] = set()
            Ui[suivant].add(x)

    return Ui
# precedents
Ui = UtoUi(U)

# initialization de l'algorithme


# point initial
S = "A"
# distances de A a tout autres point
D = {n: inf for n in X}
D[S] = 0

# initializer les chemin
paths = {n: [] for n in X}
paths[S] = [S]


# une etape/iteration de l'algorithm
def Bellman(U, Ui, D, paths):
    # une copy pour fair les calcule avec les valeur de l'iteration precedent
    static_D = D.copy()
    # pour chaque sommet:
    for y in X:
        # pour chaque predecesseur
        for x in list(Ui[y]):
            # calc le distance et comparer avec la valeur dernier
            dis = static_D[x] + U[x][y]
            # si la distance est plus petit
            if dis < static_D[y]:
                # update the distance and the path
                D[y] = dis
                paths[y] = paths[x] + [y]

                # return distances and paths
    return D, paths


# l'algorithm generalement stabilise sur N-1 etape
for _ in range(len(X) - 1):
    D, paths = Bellman(U, Ui, D, paths)

for n in X:
    print(f"Distance de {S} à {n} : {D[n]}, Chemin : {' -> '.join(paths[n])}")

